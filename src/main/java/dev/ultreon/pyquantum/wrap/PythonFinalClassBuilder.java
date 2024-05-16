package dev.ultreon.pyquantum.wrap;

import org.apache.commons.lang3.ArrayUtils;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.StringWriter;
import java.lang.reflect.*;
import java.util.*;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.logging.Logger;
import java.util.stream.Collectors;

public class PythonFinalClassBuilder {
    private final Class<?> clazz;
    private final Set<String> imports = new HashSet<>();
    private final Set<String> staticMembers = new HashSet<>();
    private final Set<String> members = new HashSet<>();
    private final Set<String> postinit = new HashSet<>();
    private Logger logger = Logger.getLogger("PythonFinalClassBuilder");

    public PythonFinalClassBuilder(Class<?> clazz) {
        this.clazz = clazz;

        addImport(toJavaImport(clazz));
    }

    public List<String> build(StringWriter sw) {
        for (Field field : clazz.getFields()) {
            if (field.isSynthetic()) {
                continue;
            }

            Class<?> type = field.getType();
            String name = type.getName();
            if (name.startsWith("dev.ultreon.quantum.")) {
                if (Modifier.isStatic(field.getModifiers()) && Modifier.isFinal(field.getModifiers())) {
                    addConstField(field);
                } else if (Modifier.isStatic(field.getModifiers())) {
                    addStaticField(field);
                } else {
                    addField(field);
                }
            }
        }

        for (Method method : clazz.getMethods()) {
            if (method.isSynthetic()) {
                continue;
            }

            if (Modifier.isPrivate(method.getModifiers())) {
                continue;
            }

            if (Modifier.isAbstract(method.getModifiers())) {
                this.addAbstractMethod(method);
                continue;
            }

            if (Modifier.isStatic(method.getModifiers())) {
                this.addStaticMethod(method);
            } else {
                this.addMethod(method);
            }
        }

        for (Constructor<?> constructor : clazz.getConstructors()) {
            if (constructor.isSynthetic()) {
                continue;
            }

            if (Modifier.isPrivate(constructor.getModifiers())) {
                continue;
            }

            this.addConstructor(constructor);
        }

        StringWriter stringWriter = new StringWriter();
        List<String> imports = new ArrayList<>(this.imports);

        if (sw == null) {
            return imports;
        }

        try (BufferedWriter writer = new BufferedWriter(sw)) {
            writer.write("\n");

            AtomicBoolean importOnce = new AtomicBoolean(false);
            String collect = imports.stream().map(code -> {
                if (code.startsWith("#py_import\n")) {
                    String substring = code.substring("#pyimport\n".length()).replace("\n", "").replace("\r", "");
                    String s1 = null;
                    String s;
                    if (substring.startsWith("from ")) {
                        String replace = substring.replace("from ", "");
                        s1 = replace.split(" import ")[0];
                        s = replace.split(" import ")[1];
                        s1 += "." + s;
                    } else {
                        String replace = substring.replace("import ", "");
                        s1 = replace;
                        s = replace;
                    }
                    s = s.substring(s.lastIndexOf(".") + 1);
                    code = """
                            try:
                                %1$s
                            except ImportError:
                                %3$s = _import_once("%2$s")
                            """.formatted(
                            substring.replace("\n", "").replace("\r", ""),
                            s1,
                            s.replace(".", "_")
                    );

                    importOnce.set(true);
                }

                return code;
            }).collect(Collectors.joining("\n"));
            writer.write("""
                    \s
                    %4$s
                    \s
                    class %1$s(%2$s):
                        \"""%3$s\"""
                    \s
                        @staticmethod
                        def _wrap(java_value: _%1$s) -> '%1$s':
                            return %1$s(__dynamic__=java_value)
                    \s
                        #
                        # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
                        #
                        @overload
                        def __init__(self, __dynamic__: _%1$s):
                            \"""
                            Dynamic initializer for %1$s.
                            WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
                    \s
                            :param __dynamic__: The java object to wrap
                            \"""
                            self.__wrapper = __dynamic__
                    \s
                        def __getattr__(self, name: str):
                            print("Getting attribute %%s" %% name)
                            if name == "_%1$s__wrapper":
                                return object.__getattr__(self, name)
                            return getattr(self.__wrapper, name)
                    \s
                        def __setattr__(self, name: str, value: Any):
                            print("Setting attribute %%s to %%s" %% (name, value))
                            if name == "_%1$s__wrapper":
                                return object.__setattr__(self, name, value)
                            setattr(self.__wrapper, name, value)
                    \s
                        def __delattr__(self, name: str):
                            raise AttributeError("Cannot delete attribute '%%s' from %%s" %% (name, self.__wrapper.__class__.__name__))
                    \s""".formatted(
                    clazz.getSimpleName(),
                    toPyClassSignature(clazz, clazz.getSuperclass(), clazz.getInterfaces()),
                    clazz.getName().replace("$", "."),
                    (importOnce.get() ? "from pyquantum_helper import import_once as _import_once\n" : "") + collect));

            if (!staticMembers.isEmpty()) {
                writer.write("\n");
                for (String member : staticMembers) {
                    List<String> list = member.lines().toList();
                    for (String line : list) {
                        writer.write("    " + line);
                        writer.write("\n");
                    }
                    writer.write("\n");
                }
            }
            if (!members.isEmpty()) {
                writer.write("\n");
                for (String member : members) {
                    List<String> list = member.lines().toList();
                    for (String line : list) {
                        writer.write("    " + line);
                        writer.write("\n");
                    }
                    writer.write("\n");
                }
            }

            if (!postinit.isEmpty()) {
                writer.write("\n");
                for (String member : postinit) {
                    List<String> list = member.lines().toList();
                    for (String line : list) {
                        writer.write(line);
                        writer.write("\n");
                    }
                    writer.write("\n");
                }
            }

            return List.of();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    private void addAbstractMethod(Method method) {
        this.members.add("""
                @abstractmethod
                def %1$s(self, %3$s):
                    \"""%2$s\"""
                    pass
                """.formatted(
                method.getName(),
                method.toGenericString(),
                toPySignature(method.getParameters())
        ));

        this.addImport(toJavaImport(method.getDeclaringClass()));
        this.addImport("from abc import abstractmethod, ABC");
    }

    private String toPyClassSignature(Class<?> clazz, Class<?> superclass, Class<?>... interfaces) {
        StringBuilder builder = new StringBuilder();
//        if (Modifier.isInterface(clazz.getModifiers()) || Modifier.isAbstract(clazz.getModifiers())) {
//            builder.append(", ABC");
//            addImport("from abc import ABC");
//        }
//
//        if (superclass != null && superclass != Object.class) {
//            builder.append(", ").append(toPyAnno(superclass, "_").replace("'", ""))
//                    .append(", ").append(toPyAnno(superclass).replace("'", ""));
//
//            addImport(toPyImport(superclass));
//            addImport(toJavaImport(superclass));
//        }
//
//        for (Class<?> anInterface : interfaces) {
//            builder.append(", ").append(toPyAnno(anInterface, "_").replace("'", ""))
//                    .append(", ").append(toPyAnno(anInterface).replace("'", ""));
//
//            addImport(toPyImport(anInterface));
//            addImport(toJavaImport(anInterface));
//        }

        String string = builder.toString();
        if (string.startsWith(", ")) {
            return string.substring(2);
        }
        return string;
    }

    private void addImport(String code) {
        if (code == null) return;

        this.imports.add(code);
    }

    private void addConstructor(Constructor<?> constructor) {
        Parameter[] parameters = constructor.getParameters();
        if (parameters.length == 0) {
            this.members.add("""
                    @overload
                    def __init__(self):
                        \"""%1$s\"""
                        val = _%2$s()
                        self.__wrapper = val
                    """.formatted(
                    constructor.toGenericString(),
                    constructor.getDeclaringClass().getSimpleName()
            ));
        }

        this.members.add("""
                @overload
                def __init__(self, %3$s):
                    \"""%1$s\"""
                    val = _%2$s(%4$s)
                    self.__wrapper = val
                """.formatted(
                constructor.toGenericString(),
                constructor.getDeclaringClass().getSimpleName(),
                toPySignature(parameters),
                toPyArgumentList(parameters)
        ));

        this.addImport(toJavaImport(constructor.getDeclaringClass()));
    }

    private String toPyArgumentList(Parameter[] parameters) {
        StringBuilder builder = new StringBuilder();

        for (int i = 0; i < parameters.length; i++) {
            if (i != 0) {
                builder.append(", ");
            }

            Parameter parameter = parameters[i];
            builder.append(toPyArgument(parameter.getType(), parameter.getName()));

            if (parameter.getType() == int.class) {
                this.addImport("import java.lang.Integer as _int");
            } else if (parameter.getType() == long.class) {
                this.addImport("import java.lang.Long as _long");
            } else if (parameter.getType() == float.class) {
                this.addImport("import java.lang.Float as _float");
            } else if (parameter.getType() == double.class) {
                this.addImport("import java.lang.Double as _double");
            } else if (parameter.getType() == boolean.class) {
                this.addImport("import java.lang.Boolean as _boolean");
            } else if (parameter.getType() == String.class) {
                this.addImport("import java.lang.String as _string");
            } else if (parameter.getType() == byte.class) {
                this.addImport("import java.lang.Byte as _byte");
            } else if (parameter.getType() == short.class) {
                this.addImport("import java.lang.Short as _short");
            } else if (parameter.getType() == char.class) {
                this.addImport("import java.lang.Character as _char");
            } else if (parameter.getType() == void.class) {
                this.addImport("import java.lang.Void as _void");
            } else if (parameter.getType() == Object.class) {
                this.addImport("import java.lang.Object as _object");
            }
        }

        return builder.toString();
    }

    private String toPyPrimitiveType(Class<?> type) {
        if (type == int.class) {
            return "int";
        } else if (type == long.class) {
            return "int";
        } else if (type == float.class) {
            return "float";
        } else if (type == double.class) {
            return "float";
        } else if (type == boolean.class) {
            return "bool";
        } else if (type == String.class) {
            return "str";
        } else if (type == void.class) {
            return "None";
        } else if (type == byte[].class) {
            return "bytes";
        } else if (type == Object.class) {
            return "object";
        } else if (type == byte.class) {
            return "int";
        } else if (type == short.class) {
            return "int";
        } else if (type == char.class) {
            return "str";
        } else {
            return null;
        }
    }

    private String toPyArgument(Class<?> type, String name) {
        if (type == int.class) {
            return "_int.valueOf(" + name + ")";
        } else if (type == long.class) {
            return "_long.valueOf(" + name + ")";
        } else if (type == float.class) {
            return "_float.valueOf(" + name + ")";
        } else if (type == double.class) {
            return "_double.valueOf(" + name + ")";
        } else if (type == boolean.class) {
            return "_boolean.valueOf(" + name + ")";
        } else if (type == String.class) {
            return name;
        } else if (type == void.class) {
            return "None";
        } else if (type == byte[].class) {
            return "bytes";
        } else if (type == Object.class) {
            return name;
        } else if (type == byte.class) {
            return "_byte.valueOf(" + name + ")";
        } else if (type == short.class) {
            return "_short.valueOf(" + name + ")";
        } else if (type == char.class) {
            return "_char.valueOf(" + name + ")";
        } else {
            return name;
        }
    }

    private Object toPySignature(Parameter[] parameters) {
        StringBuilder builder = new StringBuilder();
        for (int i = 0, parametersLength = parameters.length; i < parametersLength; i++) {
            Parameter value = parameters[i];
            if (i != 0) {
                builder.append(", ");
            }

            Class<?> type = value.getType();
            if (!Modifier.isPublic(type.getModifiers()) && !Modifier.isProtected(type.getModifiers())) {
                builder.append(value.getName()).append(": Any");
                addImport("from typing import Any");
                continue;
            }

            if (value.isVarArgs()) {
                Class<?> componentType = value.getType().getComponentType();
                if (!Modifier.isPublic(componentType.getModifiers()) && !Modifier.isProtected(componentType.getModifiers())) {
                    builder.append("*").append(value.getName()).append(": Any");
                    addImport("from typing import Any");
                    continue;
                }

                builder.append("*").append(value.getName()).append(": ").append(toPyAnno(componentType));
                this.addImport(toPyImport(componentType));
                if (i != parametersLength - 1) {
                    logger.warning("VarArgs not last parameter: " + value.getName());
                }

                continue;
            }

            String primitiveType = toPyPrimitiveType(type);
            if (primitiveType != null) {
                builder.append("%1$s: %2$s".formatted(
                        value.getName(),
                        primitiveType
                ));
            } else {
                Class<?> t = value.getType();
                while (t.isArray()) {
                    t = t.getComponentType();
                }

                builder.append("%1$s: '%2$s'".formatted(
                        value.getName(),
                        t.getSimpleName()
                ));

                this.addImport(toPyImport(t));
            }
        }

        return builder.toString();
    }

    private void addMethod(Method method) {
        Parameter[] parameters = method.getParameters();
        String name = toLowerUnderscore(method.getName());

        String override = "";
        try {
            if (clazz.getSuperclass() != null) {
                clazz.getSuperclass().getMethod(name, method.getParameterTypes());
                override = "@override\n";
                this.addImport("from pyquantum_helper import override");
            } else {
                for (Class<?> interfaceClass : clazz.getInterfaces()) {
                    try {
                        interfaceClass.getMethod(name, method.getParameterTypes());
                        override = "@override\n";
                        this.addImport("from pyquantum_helper import override");
                    } catch (NoSuchMethodException ignored) {

                    }
                }
            }
        } catch (NoSuchMethodException e) {
            for (Class<?> interfaceClass : clazz.getInterfaces()) {
                try {
                    interfaceClass.getMethod(name, method.getParameterTypes());
                    override = "@override\n";
                    this.addImport("from pyquantum_helper import override");
                } catch (NoSuchMethodException ignored) {
                }
            }
        }

        if (method.getReturnType() == void.class) {
            if (parameters.length == 0) {
                this.members.add(override + """
                        @overload
                        def %1$s(self):
                            \"""%2$s\"""
                            super(%4$s, self).%3$s()
                        """.formatted(
                        name,
                        method.toGenericString(),
                        method.getName(),
                        toPyAnno(method.getDeclaringClass()).replace("'", "")
                ));

                this.addImport(toJavaImport(method.getDeclaringClass()));
                return;
            }

            this.members.add(override + """
                    @overload
                    def %1$s(self, %4$s):
                        \"""%2$s\"""
                        super(_%6$s, self).%3$s(%5$s)
                    """.formatted(
                    name,
                    method.toGenericString(),
                    method.getName(),
                    toPySignature(parameters),
                    toPyArgumentList(parameters),
                    toPyAnno(method.getDeclaringClass()).replace("'", "")
            ));

            this.addImport(toJavaImport(method.getDeclaringClass()));
            return;
        }

        if (parameters.length == 0) {
            if (Number.class.isAssignableFrom(method.getReturnType())) {
                this.addImport(toPyImport(method.getReturnType()));
                this.members.add(override + """
                        @overload
                        def %1$s(self) -> %2$s:
                            \"""%3$s\"""
                            return _transform(super(%5$s, self).%4$s()).%2$sValue()
                        """.formatted(
                        name,
                        toPyAnno(method.getReturnType()),
                        method.toGenericString(),
                        method.getName(),
                        toPyAnno(method.getDeclaringClass()).replace("'", "")
                ));

                this.addImport(toJavaImport(method.getDeclaringClass()));
                this.addImport("from pyquantum_helper import transform as _transform");

                return;
            }

            this.members.add(override + """
                    @overload
                    def %1$s(self) -> %2$s:
                        \"""%3$s\"""
                        return %2$s._wrap(super(%5$s, self).%4$s())
                    """.formatted(
                    name,
                    toPyAnno(method.getReturnType()),
                    method.toGenericString(),
                    method.getName(),
                    toPyAnno(method.getDeclaringClass()).replace("'", "")
            ));

            this.addImport(toPyImport(method.getReturnType()));
            this.addImport(toJavaImport(method.getReturnType()));
            this.addImport(toJavaImport(method.getDeclaringClass()));
            return;
        }

        if (Number.class.isAssignableFrom(method.getReturnType())) {
            this.addImport(toPyImport(method.getReturnType()));
            this.members.add(override + """
                    @overload
                    def %1$s(self, %5$s) -> %2$s:
                        \"""%3$s\"""
                        return _transform(super(_%7$s, self).%4$s(%6$s)).%2$sValue()
                    """.formatted(
                    name,
                    toPyAnno(method.getReturnType()),
                    method.toGenericString(),
                    method.getName(),
                    toPySignature(parameters),
                    toPyArgumentList(parameters),
                    toPyAnno(method.getDeclaringClass()).replace("'", "")
            ));

            this.addImport(toJavaImport(method.getDeclaringClass()));
            this.addImport("from pyquantum_helper import transform as _transform");

            return;
        }

        this.members.add("""
                @overload
                def %1$s(self, %5$s) -> %2$s:
                    \"""%3$s\"""
                    return %2$s._wrap(super(_%7$s, self).%4$s(%6$s))
                """.formatted(
                name,
                toPyAnno(method.getReturnType()),
                method.toGenericString(),
                method.getName(),
                toPySignature(parameters),
                toPyArgumentList(parameters),
                toPyAnno(method.getDeclaringClass()).replace("'", "")
        ));

        this.addImport(toPyImport(method.getReturnType()));
        this.addImport(toJavaImport(method.getReturnType()));
        this.addImport(toJavaImport(method.getDeclaringClass()));
    }

    private void addStaticMethod(Method method) {
        String s = toLowerUnderscore(method.getName());
        Parameter[] parameters = method.getParameters();
        if (method.getReturnType() == void.class) {
            if (parameters.length == 0) {
                this.members.add("""
                            @staticmethod
                            @overload
                            def %1$s():
                                \"""%2$s\"""
                                _%3$s.%4$s()
                        """.formatted(
                        s,
                        method.toGenericString(),
                        method.getDeclaringClass().getSimpleName(),
                        method.getName()
                ));

                this.addImport(toJavaImport(method.getDeclaringClass()));
                return;
            }

            this.members.add("""
                    @staticmethod
                    @overload
                    def %1$s(%5$s):
                        \"""%2$s\"""
                        _%3$s.%4$s(%6$s)
                    """.formatted(
                    s,
                    method.toGenericString(),
                    method.getDeclaringClass().getSimpleName(),
                    method.getName(),
                    toPySignature(parameters),
                    toPyArgumentList(parameters)
            ));

            this.addImport(toJavaImport(method.getDeclaringClass()));
            return;
        }

        if (parameters.length == 0) {
            if (Number.class.isAssignableFrom(method.getReturnType())) {
                this.addImport(toPyImport(method.getReturnType()));
                this.members.add("""
                        @staticmethod
                        @overload
                        def %1$s() -> %2$s:
                            \"""%3$s\"""
                            return _transform(_%4$s.%5$s()).%2$sValue()
                        """.formatted(
                        s,

                        toPyAnno(method.getReturnType()),
                        method.toGenericString(),
                        method.getDeclaringClass().getSimpleName(),
                        method.getName()
                ));

                this.addImport(toJavaImport(method.getReturnType()));
                this.addImport(toJavaImport(method.getDeclaringClass()));

                return;
            }

            this.members.add("""
                    @staticmethod
                    @overload
                    def %1$s() -> %2$s:
                        \"""%3$s\"""
                        return %6$s._wrap(_%4$s.%5$s())
                    """.formatted(
                    s,
                    toPyAnno(method.getReturnType()),
                    method.toGenericString(),
                    method.getDeclaringClass().getSimpleName(),
                    method.getName(),
                    toPyAnno(method.getReturnType()).replace("'", "")
            ));

            this.addImport(toPyImport(method.getReturnType()));
            this.addImport(toJavaImport(method.getReturnType()));
            this.addImport(toJavaImport(method.getDeclaringClass()));
            return;
        }

        if (Number.class.isAssignableFrom(method.getReturnType())) {
            this.addImport(toPyImport(method.getReturnType()));
            this.members.add("""
                    @staticmethod
                    @overload
                    def %1$s(%5$s) -> %2$s:
                        \"""%3$s\"""
                        return _transform(_%7$s.%4$s(%6$s)).%2$sValue()
                    """.formatted(
                    s,
                    toPyAnno(method.getReturnType()),
                    method.toGenericString(),
                    method.getDeclaringClass().getSimpleName(),
                    method.getName(),
                    toPySignature(parameters),
                    toPyArgumentList(parameters)
            ));

            this.addImport(toJavaImport(method.getDeclaringClass()));
            return;
        }

        this.members.add("""
                @staticmethod
                @overload
                def %1$s(%6$s) -> %2$s:
                    \"""%3$s\"""
                    return %8$s._wrap(_%4$s.%5$s(%7$s))
                """.formatted(
                s,
                toPyAnno(method.getReturnType()),
                method.toGenericString(),
                method.getDeclaringClass().getSimpleName(),
                method.getName(),
                toPySignature(parameters),
                toPyArgumentList(parameters),
                toPyAnno(method.getReturnType()).replace("'", "")
        ));

        this.addImport(toPyImport(method.getReturnType()));
        this.addImport(toJavaImport(method.getReturnType()));
        this.addImport(toJavaImport(method.getDeclaringClass()));
    }

    private String toPyAnno(Class<?> returnType) {
        if (returnType.isArray()) {
            String s = "List[" + toPyAnno(returnType.getComponentType()) + "]";
            this.addImport("from typing import List");
            return s;
        }

        String primitiveType = toPyPrimitiveType(returnType);
        if (primitiveType != null) {
            return primitiveType;
        }

        if (returnType.getPackageName().equals(clazz.getPackageName())) {
            return "'" + returnType.getSimpleName() + "'";
        }

        String pyImport = toPyImport(returnType);
        if (pyImport == null) {
            return null;
        }

        if (pyImport.startsWith("#py_import\n")) {
            pyImport = pyImport.substring("#py_import\n".length()).replace("\n", "").replace("\r", "").trim();

            if (pyImport.startsWith("import ")) {
                pyImport = pyImport.substring("import ".length());
            } else if (pyImport.startsWith("from ")) {
                pyImport = pyImport.substring("from ".length()).replace(" import ", ".");
            }
        } else if (pyImport.startsWith("#")) {
            logger.warning("Unknown import: " + pyImport);
            return null;
        } else if (pyImport.startsWith("import ")) {
            pyImport = pyImport.substring("import ".length());
        } else if (pyImport.startsWith("from ")) {
            pyImport = pyImport.substring("from ".length()).replace(" import ", ".");
        }

        pyImport = pyImport.replaceAll(" as .*", "");

        String simpleName = pyImport.replace("$", "::");

        if (pyImport.equals(returnType.getName())) {
            int endIndex = simpleName.lastIndexOf(".");
            simpleName = simpleName.substring(endIndex == -1 ? simpleName.length() : endIndex + 1);
            simpleName = simpleName.replace("::", "_");

            return "'" + simpleName + "'";
        }

        int endIndex = simpleName.lastIndexOf(".");
        String tempName = simpleName.substring(0, endIndex == -1 ? 0 : endIndex + 1);
        int endIndex2 = tempName.lastIndexOf(".");
        String name = returnType.getName();
        simpleName = simpleName.substring(endIndex2 == -1 ? tempName.length() : endIndex2 + 1) + "." + name.substring(name.lastIndexOf(".") + 1);
        simpleName = simpleName.replace("::", ".");

        return "'" + simpleName + "'";
    }

    private String toPyAnno(Class<?> returnType, String prefix) {
        if (returnType.isArray()) {
            String s = "List[" + toPyAnno(returnType.getComponentType()) + "]";
            this.addImport("from typing import List");
            return s;
        }

        String primitiveType = toPyPrimitiveType(returnType);
        if (primitiveType != null) {
            return prefix + primitiveType;
        }

        if (returnType.getPackageName().equals(clazz.getPackageName())) {
            return "'" + prefix + returnType.getSimpleName() + "'";
        }

        String pyImport = toPyImport(returnType);
        if (pyImport == null) {
            return null;
        }

        if (pyImport.startsWith("#py_import\n")) {
            pyImport = pyImport.substring("#py_import\n".length()).replace("\n", "").replace("\r", "").trim();

            if (pyImport.startsWith("import ")) {
                pyImport = pyImport.substring("import ".length());
            } else if (pyImport.startsWith("from ")) {
                pyImport = pyImport.substring("from ".length()).replace(" import ", ".");
            }
        } else if (pyImport.startsWith("#")) {
            logger.warning("Unknown import: " + pyImport);
            return null;
        } else if (pyImport.startsWith("import ")) {
            pyImport = pyImport.substring("import ".length());
        } else if (pyImport.startsWith("from ")) {
            pyImport = pyImport.substring("from ".length()).replace(" import ", ".");
        }

        pyImport = pyImport.replaceAll(" as .*", "");

        String simpleName = returnType.getName().replace("$", "::");
        int endIndex = simpleName.lastIndexOf(".");
        simpleName = simpleName.substring(endIndex == -1 ? simpleName.length() : endIndex + 1);
        simpleName = simpleName.replace("::", "_");

        simpleName = prefix + simpleName;

        if (pyImport.equals(returnType.getName())) {
            return "'" + simpleName + "'";
        }

        int endIndex1 = pyImport.lastIndexOf(".");
        String substring = pyImport.substring(0, endIndex1 == -1 ? pyImport.length() : endIndex1);
        int i = substring.lastIndexOf(".");
        simpleName = substring.substring(i == -1 ? 0 : i + 1) + "." + simpleName;

        return "'" + simpleName + "'";
    }

    private void addField(Field field) {
        if (Modifier.isPrivate(field.getModifiers())) {
            return;
        }

        this.members.add("""
                @property
                def %1$s(self) -> %2$s:
                    return %2$s._wrap(super(_%4$s).%3$s())
                """.formatted(
                toLowerUnderscore(field.getName()),
                field.getType().getSimpleName(),
                field.getName(),
                field.getDeclaringClass().getSimpleName()
        ));

        if (!Modifier.isFinal(field.getModifiers())) {
            this.members.add("""
                    @property
                    def %1$s(self, value: %2$s):
                        super(_%4$s).%3$s(value)
                    """.formatted(
                    toLowerUnderscore(field.getName()),
                    toPyAnno(field.getType()),
                    field.getName(),
                    field.getDeclaringClass().getSimpleName()
            ));
        }

        this.addImport(toPyImport(field.getType()));
        this.addImport(toJavaImport(field.getType()));
    }

    private void addStaticField(Field field) {
        if (Modifier.isPrivate(field.getModifiers())) {
            return;
        }

        this.members.add("""
                @staticmethod
                @property
                def %1$s_() -> %2$s:
                    \"""
                    Getter for the %1$s property.
                \s
                    :return: Value of %1$s
                    \"""
                \s
                    return super(%2$s).%3$s()
                """.formatted(
                toLowerUnderscore(field.getName()),
                field.getType().getSimpleName(),
                field.getName()
        ));

        this.members.add("""
                @staticmethod
                @property
                def %1$s_(value: %2$s):
                    \"""
                    Setter for the %1$s property.
                \s
                    :param value: Value to set for the %1$s property. 
                    \"""
                \s
                    super(%2$s).%3$s(value)
                """.formatted(
                toLowerUnderscore(field.getName()),
                toPyAnno(field.getType()),
                field.getName()
        ));

        this.addImport(toPyImport(field.getType()));
        this.addImport(toJavaImport(field.getType()));
    }

    private String toLowerUnderscore(String name) {
//        boolean lastUpper = true;
//        StringBuilder builder = new StringBuilder();
//        for (int i = 0; i < name.length(); i++) {
//            if (Character.isUpperCase(name.charAt(i)) && !lastUpper) {
//                builder.append("_");
//                lastUpper = true;
//            } else {
//                lastUpper = false;
//            }
//
//            builder.append(Character.toLowerCase(name.charAt(i)));
//        }

        return name;
    }

    private void addConstField(Field field) {
        if (field.getType().equals(field.getDeclaringClass())) {
            this.postinit.add("""
                    %1$s.%2$s = %1$s._wrap(_%2$s.%3$s)
                    """.formatted(
                    toPyAnno(field.getDeclaringClass()).replace("'", ""),
                    field.getName(),
                    field.getName()
            ));

            return;
        }

        this.staticMembers.add("""
                # %4$s
                %1$s: '%2$s' = _wrap(_%2$s.%3$s)""".formatted(
                field.getName(),
                toPyAnno(field.getType()).replace("'", ""),
                field.getName(),
                field.toGenericString()
        ));

        this.addImport(toPyImport(field.getType()));
    }

    private String toJavaImport(Class<?> type) {
        if (type.isArray()) {
            return toJavaImport(type.getComponentType());
        }

        if (type.isPrimitive()) {
            return null;
        }

        String simpleName = type.getSimpleName();
        String[] name = type.getName().split("\\.");
        String importName = name[name.length - 1].replace("$", "_");
        String s = "import " + type.getName().split("\\$")[0] + " as _" + importName;
        String[] split = type.getName().split("\\.");
        String s1 = split[split.length - 1];
        String replace = s1.replace("$", "_");
        if (s1.contains("$")) {
            s += "\n_" + simpleName + " = _" + replace + "." + String.join(".", ArrayUtils.remove(s1.split("\\$"), 0));
        } else {
            s += "\n_" + simpleName + " = _" + replace;
        }

        return s;
    }

    private String toPyImport(Class<?> type) {
        if (type.isArray()) {
            return toPyImport(type.getComponentType());
        }

        try {
            if (type == int.class) {
                return "from builtins import int";
            } else if (type == long.class) {
                return "from builtins import int";
            } else if (type == float.class) {
                return "from builtins import float";
            } else if (type == double.class) {
                return "from builtins import float";
            } else if (type == boolean.class) {
                return "from builtins import bool";
            } else if (type == String.class) {
                return "from builtins import str";
            } else if (type == void.class) {
                return null;
            } else if (type == Object.class) {
                return "from builtins import object";
            } else if (type == Class.class) {
                return "from builtins import type";
            } else if (type == short.class) {
                return "from builtins import int";
            } else if (type == byte.class) {
                return "from builtins import int";
            } else if (type == char.class) {
                return "from builtins import str";
            } else if (type.getName().startsWith("dev.ultreon.quantum.")) {
                return convert(clazz, type, "dev.ultreon.quantum", "pyquantum");
            } else if (type.getName().startsWith("dev.ultreon.xeox.loader.")) {
                return convert(clazz, type, "dev.ultreon.xeox.loader", "pyxeox");
            } else if (type.getName().startsWith("dev.ultreon.libs")) {
                return convert(clazz, type, "dev.ultreon.libs", "pycorelibs");
            } else if (type.getName().startsWith("dev.ultreon.data.")) {
                return convert(clazz, type, "dev.ultreon.data", "pydata");
            } else if (type.getName().startsWith("dev.ultreon.ubo.")) {
                return convert(clazz, type, "dev.ultreon.ubo", "pyubo");
            } else if (type.getName().startsWith("com.badlogic.gdx")) {
                return convert(clazz, type, "com.badlogic.gdx", "pygdx");
            } else if (type.getName().startsWith("com.badlogic")) {
                return convert(clazz, type, "com.badlogic", "pygdx");
            } else if (type.getName().startsWith("org.apache.commons.")) {
                return convert(clazz, type, "org.apache.commons", "pyapache");
            } else if (type.getName().startsWith("org.apache.logging.log4j")) {
                return convert(clazz, type, "org.apache.logging.log4j", "log4py");
            } else if (type.getName().startsWith("org.lwjgl.opengl.")) {
                return convert(clazz, type, "org.lwjgl.opengl", "pyopengl");
            } else if (type.getName().startsWith("org.lwjgl.glfw.")) {
                return convert(clazz, type, "org.lwjgl.glfw", "pyglfw");
            } else if (type.getName().startsWith("org.lwjgl.opencl.")) {
                return convert(clazz, type, "org.lwjgl.opencl", "pyopencl");
            } else if (type.getName().startsWith("org.lwjgl.stb.")) {
                return convert(clazz, type, "org.lwjgl.stb", "pyglstb");
            } else if (type.getName().startsWith("org.lwjgl.vulkan.")) {
                return convert(clazz, type, "org.lwjgl.vulkan", "pyvulkan");
            } else if (type.getName().startsWith("org.lwjgl.egl.")) {
                return convert(clazz, type, "org.lwjgl.egl", "pyegl");
            } else if (type.getName().startsWith("org.lwjgl.system.")) {
                return convert(clazz, type, "org.lwjgl.system", "pyglsystem");
            } else if (type.getName().startsWith("org.lwjgl.nuklear.")) {
                return convert(clazz, type, "org.lwjgl.nuklear", "pynuklear");
            } else if (type.getName().startsWith("org.lwjgl.nanovg.")) {
                return convert(clazz, type, "org.lwjgl.nanovg", "pynanovg");
            } else if (type.getName().startsWith("org.lwjgl.util.")) {
                return convert(clazz, type, "org.lwjgl.util", "pyglutil");
            } else if (type.getName().startsWith("org.lwjgl.assimp.")) {
                return convert(clazz, type, "org.lwjgl.assimp", "pyassimp");
            } else if (type.getName().startsWith("org.lwjgl.")) {
                return convert(clazz, type, "org.lwjgl", "pygl");
            } else if (type.getName().startsWith("com.google.gson")) {
                return convert(clazz, type, "com.google.gson", "pygson");
            } else if (type.getName().startsWith("com.google.protobuf")) {
                return convert(clazz, type, "com.google.protobuf", "pyprotobuf");
            } else if (type.getName().startsWith("com.google.common.collect")) {
                return convert(clazz, type, "com.google.common.collect", "pygcollect");
            } else if (type.getName().startsWith("com.google.common")) {
                return convert(clazz, type, "com.google.common", "pygcommon");
            } else if (type.getName().startsWith("space.earlygrey.shapedrawer")) {
                return convert(clazz, type, "space.earlygrey.shapedrawer", "pyshapedrawer");
            } else if (type.getName().startsWith("org.slf4j.")) {
                return convert(clazz, type, "org.slf4j", "slf4py");
            } else {
                return "import " + type.getName().replace("$", ".") + " as " + type.getSimpleName();
            }
        } catch (Exception e) {
            throw new RuntimeException("Failed to import: " + type.getName(), e);
        }
    }

    private String convert(Class<?> clazz, Class<?> type, String java, String python) {
        String simpleName = type.getName();
        simpleName = simpleName.substring(simpleName.lastIndexOf(".") + 1);
        simpleName = simpleName.replace("$", "_");

        if (type.getPackageName().equals(clazz.getPackageName())) {
            return null;
        }
        if (type.getPackageName().equals(java)) {
            int endIndex = python.lastIndexOf(".");
            String packageName = python.substring(0, endIndex == -1 ? python.length() : endIndex);
            simpleName = python.substring(endIndex + 1);

            if (!packageName.contains(".")) {
                return "#py_import\nimport " + packageName;
            }

            return "#py_import\nfrom " + packageName + " import " + simpleName;
        }

        python += type.getPackageName().substring(java.length());
        int endIndex = python.lastIndexOf(".");
        String packageName = python.substring(0, endIndex == -1 ? python.length() : endIndex);
        simpleName = python.substring(endIndex + 1);

        return "#py_import\nfrom " + packageName + " import " + simpleName;
    }
}
