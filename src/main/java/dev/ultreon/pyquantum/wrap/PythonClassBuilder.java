package dev.ultreon.pyquantum.wrap;

import org.apache.commons.lang3.ArrayUtils;
import org.jetbrains.annotations.NotNull;

import java.io.BufferedWriter;
import java.io.IOException;
import java.lang.reflect.*;
import java.util.*;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.logging.Logger;
import java.util.stream.Collectors;

public class PythonClassBuilder {
    protected final Class<?> clazz;
    protected final Set<String> imports = new HashSet<>();
    protected final Set<String> staticMembers = new HashSet<>();
    protected final Set<String> members = new HashSet<>();
    protected final Set<String> postinit = new HashSet<>();
    private final Logger logger = Logger.getLogger("PythonClassBuilder");

    public PythonClassBuilder(Class<?> clazz) {
        this.clazz = clazz;

        addImport(toJavaImport(clazz));
    }

    public List<String> build(StringBuilder sw) {
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

        List<String> imports = new ArrayList<>(this.imports);

        if (sw == null) {
            return imports;
        }

        sw.append("\n");

        AtomicBoolean importOnce = new AtomicBoolean(false);
        String collect = imports.stream().map(code -> {
            if (code.startsWith("#py_import\n")) {
                String substring = code.substring("#pyimport\n".length()).replace("\n", "").replace("\r", "");
                String s1;
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
        sw.append("""
                \s
                %4$s
                \s
                class %1$s(%2$s):
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
                        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
                        \"""
                        self.__wrapper = __dynamic__
                \s
                    def __delattr__(self, name: str):
                        raise AttributeError("Cannot delete attribute '%%s' from %%s" %% (name, self.__wrapper.__class__.__name__))
                \s""".formatted(
                toPyAnno(clazz).replace("'", "").replace("$", "_").replace(".", "_"),
                toPyClassSignature(clazz, clazz.getSuperclass(), clazz.getInterfaces()),
                clazz.getName().replace("$", "_"),
                (importOnce.get() ? "from pyquantum_helper import import_once as _import_once\n" : "") + collect));

        if (!staticMembers.isEmpty()) {
            sw.append("\n");
            for (String member : staticMembers) {
                List<String> list = member.lines().toList();
                for (String line : list) {
                    sw.append("    ").append(line);
                    sw.append("\n");
                }
                sw.append("\n");
            }
        }
        if (!members.isEmpty()) {
            sw.append("\n");
            for (String member : members) {
                List<String> list = member.lines().toList();
                for (String line : list) {
                    sw.append("    ").append(line);
                    sw.append("\n");
                }
                sw.append("\n");
            }
        }

        if (!postinit.isEmpty()) {
            sw.append("\n");
            for (String member : postinit) {
                List<String> list = member.lines().toList();
                for (String line : list) {
                    sw.append(line);
                    sw.append("\n");
                }
                sw.append("\n");
            }
        }

        return List.of();
    }

    public void addAbstractMethod(Method method) {
        this.members.add("""
                @abstractmethod
                def %1$s(self, %3$s):
                    pass
                """.formatted(
                toJavaMemberName(method),
                method.toGenericString(),
                toPySignature(method.getParameters())
        ));

        this.addImport(toJavaImport(method.getDeclaringClass()));
        this.addImport("from abc import abstractmethod, ABC");
    }

    public String toPyClassSignature(Class<?> clazz, Class<?> superclass, Class<?>... interfaces) {
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

        builder.append(", ").append(toPyAnno(clazz, "_").replace("'", ""));

        String string = builder.toString();
        if (string.startsWith(", ")) {
            return string.substring(2);
        }
        return string;
    }

    public void addImport(String code) {
        if (code == null) return;

        this.imports.add(code);
    }

    public void addConstructor(Constructor<?> constructor) {
        Parameter[] parameters = constructor.getParameters();
        if (parameters.length == 0) {
            this.members.add("""
                    @overload
                    def __init__(self):
                    %3$s
                        val = _%2$s()
                        self.__wrapper = val
                    """.formatted(
                    constructor.toGenericString(),
                    constructor.getDeclaringClass().getSimpleName(),
                    importJava(constructor.getDeclaringClass())
            ));
        }

        this.members.add("""
                @overload
                def __init__(self, %3$s):
                %5$s
                    val = _%2$s(%4$s)
                    self.__wrapper = val
                """.formatted(
                constructor.toGenericString(),
                constructor.getDeclaringClass().getSimpleName(),
                toPySignature(parameters),
                toPyArgumentList(parameters),
                importJava(constructor.getDeclaringClass())
        ));

        this.addImport(toJavaImport(constructor.getDeclaringClass()));
    }

    public String importJava(Class<?> member) {
        String javaImport = toJavaImport(member);
        if (javaImport == null) return "# NULL_IMPORT";
        return javaImport.lines().map(line -> "    " + line).collect(Collectors.joining("\n"));
    }

    public String importPyJava(Class<?> member) {
        String javaImport0 = toJavaImport0(member);
        if (javaImport0 == null) return "# NULL_IMPORT";
        return javaImport0.lines().map(line -> "    " + line).collect(Collectors.joining("\n"));
    }

    public String importPy(Class<?> member) {
        String pyImport = toPyImport(member);
        if (pyImport == null) return "# NULL_IMPORT";
        return pyImport.lines().map(line -> "    " + line).collect(Collectors.joining("\n"));
    }

    public String toPyArgumentList(Parameter[] parameters) {
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

    public String toPyPrimitiveType(Class<?> type) {
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

    public String toPyArgument(Class<?> type, String name) {
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

    public Object toPySignature(Parameter[] parameters) {
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

    public void addMethod(Method method) {
        Parameter[] parameters = method.getParameters();
        String name = toPyMemberName(method);

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
                            self.__wrapper.%3$s()
                        """.formatted(
                        name,
                        method.toGenericString(),
                        toJavaMemberName(method)
                ));

                return;
            }

            this.members.add(override + """
                    @overload
                    def %1$s(self, %4$s):
                        self.__wrapper.%3$s(%5$s)
                    """.formatted(
                    name,
                    method.toGenericString(),
                    toJavaMemberName(method),
                    toPySignature(parameters),
                    toPyArgumentList(parameters)
            ));

            return;
        }

        if (parameters.length == 0) {
            if (Number.class.isAssignableFrom(method.getReturnType())) {
                this.addImport(toPyImport(method.getReturnType()));
                this.members.add(override + """
                        @overload
                        def %1$s(self) -> %2$s:
                            # method wrapping and transform number to primitive %2$s
                            return _transform(self.__wrapper.%4$s()).%2$sValue()
                        """.formatted(
                        name,
                        toPyAnno(method.getReturnType()).replace("'", ""),
                        method.toGenericString(),
                        toJavaMemberName(method),
                        toPyAnno(clazz).replace("'", "")
                ));

                this.addImport("from pyquantum_helper import transform as _transform");

                return;
            }

            this.members.add(override + """
                    @overload
                    def %1$s(self) -> %2$s:
                        # import %2$s for return value
                    %6$s
                        # method wrapping
                        return %5$s._wrap(self.__wrapper.%4$s())
                    """.formatted(
                    name,
                    toPyAnno(method.getReturnType()),
                    method.toGenericString(),
                    toJavaMemberName(method),
                    toPyAnno(method.getReturnType()).replace("'", ""),
                    importPy(method.getReturnType())
            ));

            this.addImport(toPyImport(method.getReturnType()));
            this.addImport(toJavaImport(method.getReturnType()));
            return;
        }

        if (Number.class.isAssignableFrom(method.getReturnType())) {
            this.addImport(toPyImport(method.getReturnType()));
            this.members.add(override + """
                    @overload
                    def %1$s(self, %5$s) -> '%2$s':
                        return _transform(self.__wrapper.%4$s(%6$s)).%2$sValue()
                    """.formatted(
                    name,
                    toPyAnno(method.getReturnType()).replace("'", ""),
                    method.toGenericString(),
                    toJavaMemberName(method),
                    toPySignature(parameters),
                    toPyArgumentList(parameters)
            ));

            this.addImport("from pyquantum_helper import transform as _transform");

            return;
        }

        this.members.add("""
                @overload
                def %1$s(self, %5$s) -> %2$s:
                    \"""%3$s\"""
                    # import %2$s for return value
                %7$s
                \s
                    # method wrapping
                    return %2$s._wrap(self.__wrapper.%4$s(%6$s))
                """.formatted(
                name,
                toPyAnno(method.getReturnType()).replace("'", ""),
                method.toGenericString(),
                toJavaMemberName(method),
                toPySignature(parameters),
                toPyArgumentList(parameters),
                importPy(method.getReturnType())
        ));

        this.addImport(toPyImport(method.getReturnType()));
        this.addImport(toJavaImport(method.getReturnType()));
        this.addImport(toJavaImport(method.getDeclaringClass()));
    }

    public void addStaticMethod(Method method) {
        String s = toPyMemberName(method);
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
                        toJavaMemberName(method)
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
                    toJavaMemberName(method),
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
                        toPyAnno(method.getReturnType()).replace("'", ""),
                        method.toGenericString(),
                        method.getDeclaringClass().getSimpleName(),
                        toJavaMemberName(method)
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
                    toPyAnno(method.getReturnType()).replace("'", ""),
                    method.toGenericString(),
                    method.getDeclaringClass().getSimpleName(),
                    toJavaMemberName(method),
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
                    def %1$s(%6$s) -> %2$s:
                        \"""%3$s\"""
                        return _transform(%4$s.%5$s(_%7$s)).%2$sValue()
                    """.formatted(
                    s,
                    toPyAnno(method.getReturnType()).replace("'", ""),
                    method.toGenericString(),
                    method.getDeclaringClass().getSimpleName(),
                    toJavaMemberName(method),
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
                toPyAnno(method.getReturnType()).replace("'", ""),
                method.toGenericString(),
                method.getDeclaringClass().getSimpleName(),
                toJavaMemberName(method),
                toPySignature(parameters),
                toPyArgumentList(parameters),
                toPyAnno(method.getReturnType()).replace("'", "")
        ));

        this.addImport(toPyImport(method.getReturnType()));
        this.addImport(toJavaImport(method.getReturnType()));
        this.addImport(toJavaImport(method.getDeclaringClass()));
    }

    public @NotNull String toPyAnno(Class<?> returnType) {
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
            String name = returnType.getName();
            name = name.substring(name.lastIndexOf(".") + 1);
            String replace = name.replace("$", ".");
            return "'" + replace + "'";
        }

        String pyImport = toPyImport0(returnType);
        if (pyImport == null) {
            throw new RuntimeException("Failed to import: " + returnType.getName());
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
            addImport("from typing import Any");
            return "Any";
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

            return "'" + simpleName.replace("$", "_") + "'";
        }

        if (!returnType.getPackageName().equals(pyImport)) {
            int endIndex = simpleName.lastIndexOf(".");
            simpleName = simpleName.substring(endIndex == -1 ? 0 : endIndex + 1);
            simpleName = simpleName.replace("::", "_");

            return "'" + simpleName.replace("$", "_") + "'";
        }

        int endIndex = simpleName.lastIndexOf(".");
        String tempName = simpleName.substring(0, endIndex == -1 ? 0 : endIndex + 1);
        int endIndex2 = tempName.lastIndexOf(".");
        String name = returnType.getName();
        simpleName = simpleName.substring(endIndex2 == -1 ? tempName.length() : endIndex2 + 1) + "." + name.substring(name.lastIndexOf(".") + 1);
        simpleName = simpleName.replace("::", ".");

        return "'" + simpleName.replace("$", "_") + "'";
    }

    public String toPyAnno(Class<?> returnType, String prefix) {
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

        String pyImport = toPyImport0(returnType);
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

    public void addField(Field field) {
        if (Modifier.isPrivate(field.getModifiers())) {
            return;
        }

        this.members.add("""
                @property
                def %1$s(self) -> %2$s:
                    return %2$s._wrap(super(_%4$s).%3$s())
                """.formatted(
                toPyMemberName(field),
                field.getType().getSimpleName(),
                toJavaMemberName(field),
                field.getDeclaringClass().getSimpleName()
        ));

        if (!Modifier.isFinal(field.getModifiers())) {
            this.members.add("""
                    @property
                    def %1$s(self, value: %2$s):
                        super(_%4$s).%3$s(value)
                    """.formatted(
                    toPyMemberName(field),
                    toPyAnno(field.getType()),
                    toJavaMemberName(field),
                    field.getDeclaringClass().getSimpleName()
            ));
        }

        this.addImport(toPyImport(field.getType()));
        this.addImport(toJavaImport(field.getType()));
    }

    public void addStaticField(Field field) {
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
                    return _%4$s.%3$s
                """.formatted(
                toPyMemberName(field),
                field.getType().getSimpleName(),
                toJavaMemberName(field),
                toPyAnno(field.getDeclaringClass()).replace("'", "")
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
                    _%4$s.%3$s = value
                """.formatted(
                toPyMemberName(field),
                toPyAnno(field.getType()),
                toJavaMemberName(field),
                toPyAnno(field.getDeclaringClass()).replace("'", "")
        ));

        this.addImport(toPyImport(field.getType()));
        this.addImport(toJavaImport(field.getType()));
    }

    public String toJavaMemberName(Member field) {
        return switch (field.getName()) {
            case "and" -> "__getattr__(\"and\")";
            case "or" -> "__getattr__(\"or\")";
            case "xor" -> "__getattr__(\"xor\")";
            case "not" -> "__getattr__(\"not\")";
            case "in" -> "__getattr__(\"in\")";
            case "is" -> "__getattr__(\"is\")";
            case "None" -> "__getattr__(\"None\")";
            case "True" -> "__getattr__(\"True\")";
            case "False" -> "__getattr__(\"False\")";
            case "class" -> "__getattr__(\"class\")";
            case "def" -> "__getattr__(\"def\")";
            case "del" -> "__getattr__(\"del\")";
            case "elif" -> "__getattr__(\"elif\")";
            case "else" -> "__getattr__(\"else\")";
            case "except" -> "__getattr__(\"except\")";
            case "finally" -> "__getattr__(\"finally\")";
            case "for" -> "__getattr__(\"for\")";
            case "from" -> "__getattr__(\"from\")";
            case "global" -> "__getattr__(\"global\")";
            case "if" -> "__getattr__(\"if\")";
            case "import" -> "__getattr__(\"import\")";
            case "lambda" -> "__getattr__(\"lambda\")";
            case "nonlocal" -> "__getattr__(\"nonlocal\")";
            case "pass" -> "__getattr__(\"pass\")";
            case "raise" -> "__getattr__(\"raise\")";
            case "return" -> "__getattr__(\"return\")";
            case "try" -> "__getattr__(\"try\")";
            case "while" -> "__getattr__(\"while\")";
            case "with" -> "__getattr__(\"with\")";
            case "yield" -> "__getattr__(\"yield\")";
            case "as" -> "__getattr__(\"as\")";
            default -> field.getName().replace('$', '_');
        };
    }

    public String toPyMemberName(String javaMemberName) {
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

        return javaMemberName;
    }

    public String toPyMemberName(Member field) {
        return switch (field.getName()) {
            case "and" -> "and_";
            case "or" -> "or_";
            case "xor" -> "xor_";
            case "not" -> "not_";
            case "in" -> "in_";
            case "is" -> "is_";
            case "None" -> "None_";
            case "True" -> "True_";
            case "False" -> "False_";
            case "class" -> "class_";
            case "def" -> "def_";
            case "del" -> "del_";
            case "elif" -> "elif_";
            case "else" -> "else_";
            case "except" -> "except_";
            case "finally" -> "finally_";
            case "for" -> "for_";
            case "from" -> "from_";
            case "global" -> "global_";
            case "if" -> "if_";
            case "import" -> "import_";
            case "lambda" -> "lambda_";
            case "nonlocal" -> "nonlocal_";
            case "pass" -> "pass_";
            case "raise" -> "raise_";
            case "return" -> "return_";
            case "try" -> "try_";
            case "while" -> "while_";
            case "with" -> "with_";
            case "yield" -> "yield_";
            case "as" -> "as_";
            default -> field.getName().replace('$', '_');
        };
    }

    public void addConstField(Field field) {
        if (field.getType().equals(field.getDeclaringClass())) {
            this.postinit.add("""
                    %1$s.%2$s = %1$s._wrap(_%1$s.%3$s)
                    """.formatted(
                    toPyAnno(field.getDeclaringClass()).replace("'", ""),
                    toJavaMemberName(field),
                    toJavaMemberName(field)
            ));

            return;
        }

        this.staticMembers.add("""
                # %4$s
                %1$s: '%2$s' = _wrap(_%2$s.%3$s)""".formatted(
                toJavaMemberName(field),
                toPyAnno(field.getType()).replace("'", ""),
                toJavaMemberName(field),
                field.toGenericString()
        ));

        this.addImport(toPyImport(field.getType()));
    }

    public String toJavaImport(Class<?> type) {
        if (type.isArray()) {
            return toJavaImport(type.getComponentType());
        }

        if (type.isPrimitive()) {
            return null;
        }

        String extra = "";
        if (Objects.equals(toPyImport(type), toJavaImport0(type))) {
            extra = "\n" + toJavaImport0(type);
        }

        String module = type.getName();
        int endIndex = module.lastIndexOf('$');
        module = module.substring(0, endIndex == -1 ? module.length() : endIndex);
        int i = module.lastIndexOf('.');
        String importName = module.substring(i == -1 ? 0 : i + 1).replace("$", "_");
        return "import " + module + " as _" + importName + extra;
    }

    public String toJavaImport0(Class<?> type) {
        if (type.isArray()) {
            return toJavaImport(type.getComponentType());
        }

        if (type.isPrimitive()) {
            return null;
        }

        String simpleName = type.getSimpleName();
        String[] name = type.getName().split("\\.");
        String importName = name[name.length - 1].replace("$", "_");
        String replace1 = type.getName().split("\\$")[0];
        String s = "import " + replace1 + " as " + importName;
        String[] split = type.getName().split("\\.");
        String s1 = split[split.length - 1];
        String replace = s1.replace("$", "_");
        if (s1.contains("$")) {
            s += "\n" + simpleName + " = " + replace + "." + String.join(".", ArrayUtils.remove(s1.split("\\$"), 0));
        } else {
            s += "\n" + simpleName + " = " + replace;
        }

        return s;
    }

    public String toPyImport(Class<?> type) {
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
            } else {
                String convert = Converters.convert(type.getName());
                if (convert != null) {
                    return convert(clazz, type, type.getPackageName(), convert.substring(0, convert.lastIndexOf(".")));
                }
                return toJavaImport0(type);
            }
        } catch (Exception e) {
            throw new RuntimeException("Failed to import: " + type.getName(), e);
        }
    }

    public String toPyImport0(Class<?> type) {
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
            } else {
                String convert = Converters.convert(type.getName());
                if (convert != null) {
                    return convert(clazz, type, type.getPackageName(), convert.substring(0, convert.lastIndexOf(".")));
                }
                return "import " + type.getName().replace("$", "_") + " as " + type.getSimpleName();
            }
        } catch (Exception e) {
            throw new RuntimeException("Failed to import: " + type.getName(), e);
        }
    }

    public String convert(Class<?> clazz, Class<?> type, String java, String python) {
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
