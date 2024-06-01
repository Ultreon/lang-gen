package dev.ultreon.langgen.javascript.ts;

import dev.ultreon.langgen.api.Converters;
import dev.ultreon.langgen.javascript.api.AnyJsClassBuilder;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

import java.lang.reflect.*;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.*;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.logging.Logger;
import java.util.stream.Collectors;

public class TsClassBuilder implements AnyJsClassBuilder {
    public static final String STUB_FORMAT = """
            %4$s
            
            /**
             * This is a wrapper for the {_%1$s} class.
             */
            export %5$sclass %1$s%2$s {
            """;
    public static final String STUB_CONSTRUCTOR_ARGS = """
            /**
             * %1$s
            %5$s
             */
            %6$sconstructor(%3$s) {
                // Stub
            }
            """;
    public static final String STUB_CONSTRUCTOR = """
            /**
             * %1$s
            %3$s
             */
            %4$sconstructor() {
                // Stub
            }
            """;
    protected final Class<?> clazz;
    protected final Set<String> imports = new LinkedHashSet<>();
    protected final Set<String> staticMembers = new LinkedHashSet<>();
    protected final Set<String> members = new LinkedHashSet<>();
    protected final Set<String> postInit = new LinkedHashSet<>();
    private final Logger logger = Logger.getLogger("TypescriptClassBuilder");

    public TsClassBuilder(Class<?> clazz) {
        this.clazz = clazz;
    }

    @Override
    public List<String> build(StringBuilder sw) {
        for (Field field : clazz.getFields())
            if (Modifier.isStatic(field.getModifiers()) && Modifier.isFinal(field.getModifiers())) addConstField(field);
            else if (Modifier.isStatic(field.getModifiers())) addStaticField(field);
            else addField(field);
            
        Map<String, MethodInfo> methodInfos = MethodInfo.build(clazz.getMethods(), this::toTsType);
        
        for (Method method : clazz.getMethods()) {
            String name = method.getName();

            if (Modifier.isAbstract(method.getModifiers())) {
                this.addAbstractMethod(method);
                continue;
            }

            this.addMethod(method);
        }
        
        for (MethodInfo methodInfo : methodInfos.values()) {
            this.addAbstractMethod(methodInfo);
            this.addMethod(methodInfo);
        }

        for (Constructor<?> constructor : clazz.getConstructors()) {
            this.addConstructor(constructor);
        }
        this.addConstructor(MethodInfo.build(clazz.getConstructors(), this::toTsType));

        List<String> imports = new ArrayList<>(this.imports);

        sw.append("\n");

        AtomicBoolean importOnce = new AtomicBoolean(false);
        String collect = imports.stream().sorted(Comparator.reverseOrder()).collect(Collectors.joining("\n"));
        sw.append(STUB_FORMAT.formatted(
                toTsType(clazz).replace(".", "_"),
                toTsClassSignature(clazz, clazz.getSuperclass(), clazz.getInterfaces()),
                clazz.getName(),
                (importOnce.get() ? "import {import_once} from 'qjs-classpath/quantumjs-helper/core';\n" : "") + collect,
                toModifiers(clazz)));

        Set<String> staticMembers1 = staticMembers;
        if (!staticMembers1.isEmpty()) {
            sw.append("\n");
            for (String member : staticMembers1.stream().sorted((o1, o2) -> {
                if (o1.contains("constructor") && !o2.contains("constructor")) return 1;
                if (!o1.contains("constructor") && o2.contains("constructor")) return -1;

                if (o1.contains("static") && !o2.contains("static")) return 1;
                if (!o1.contains("static") && o2.contains("static")) return -1;

                if (o1.contains("abstract") && !o2.contains("abstract")) return 1;
                if (!o1.contains("abstract") && o2.contains("abstract")) return -1;

                if (o1.contains("final") && !o2.contains("final")) return 1;
                if (!o1.contains("final") && o2.contains("final")) return -1;

                if (o1.contains("private") && !o2.contains("private")) return 1;
                if (!o1.contains("private") && o2.contains("private")) return -1;

                if (o1.contains("protected") && !o2.contains("protected")) return 1;
                if (!o1.contains("protected") && o2.contains("protected")) return -1;

                if (o1.contains("public") && !o2.contains("public")) return 1;
                if (!o1.contains("public") && o2.contains("public")) return -1;

                if (o1.contains("function") && !o2.contains("function")) return 1;
                if (!o1.contains("function") && o2.contains("function")) return -1;

                String[] split = o1.trim().split("\n")[0].split("[_ ()\\[\\]\\-+/*|&^$\n\\s]");
                for (int i = 0; i < split.length; i++) {
                    var s = split[i];
                    var s1 = o2.trim().split("\n")[0].split("[_ ()\\[\\]\\-+/*|&^$\n\\s]");

                    if (i >= s1.length) return -1;

                    if (!s.equals(s1[i])) return s.compareTo(s1[i]);
                }

                return o1.compareTo(o2);
            }).toList()) {
                List<String> list = member.lines().toList();
                for (String line : list) {
                    sw.append("    ").append(line);
                    sw.append("\n");
                }
                sw.append("\n");
            }
        }
        Set<String> members1 = members;
        if (!members1.isEmpty()) {
            sw.append("\n");
            for (String member : members1.stream().sorted((o1, o2) -> {
                if (o1.contains("constructor") && !o2.contains("constructor")) return 1;
                if (!o1.contains("constructor") && o2.contains("constructor")) return -1;

                if (o1.contains("static") && !o2.contains("static")) return 1;
                if (!o1.contains("static") && o2.contains("static")) return -1;

                if (o1.contains("abstract") && !o2.contains("abstract")) return 1;
                if (!o1.contains("abstract") && o2.contains("abstract")) return -1;

                if (o1.contains("final") && !o2.contains("final")) return 1;
                if (!o1.contains("final") && o2.contains("final")) return -1;

                if (o1.contains("private") && !o2.contains("private")) return 1;
                if (!o1.contains("private") && o2.contains("private")) return -1;

                if (o1.contains("protected") && !o2.contains("protected")) return 1;
                if (!o1.contains("protected") && o2.contains("protected")) return -1;

                if (o1.contains("public") && !o2.contains("public")) return 1;
                if (!o1.contains("public") && o2.contains("public")) return -1;

                if (o1.contains("function") && !o2.contains("function")) return 1;
                if (!o1.contains("function") && o2.contains("function")) return -1;

                if (o1.contains("class") && !o2.contains("class")) return 1;
                if (!o1.contains("class") && o2.contains("class")) return -1;

                if (o1.contains("interface") && !o2.contains("interface")) return 1;
                if (!o1.contains("interface") && o2.contains("interface")) return -1;

                if (o1.contains("enum") && !o2.contains("enum")) return 1;
                if (!o1.contains("enum") && o2.contains("enum")) return -1;

                if (o1.contains("namespace") && !o2.contains("namespace")) return 1;
                if (!o1.contains("namespace") && o2.contains("namespace")) return -1;

                if (o1.contains("type") && !o2.contains("type")) return 1;
                if (!o1.contains("type") && o2.contains("type")) return -1;

                if (o1.contains("const") && !o2.contains("const")) return 1;
                if (!o1.contains("const") && o2.contains("const")) return -1;

                String[] split = o1.trim().split("\n")[0].split("[_ ()\\[\\]\\-+/*|&^$\n\\s]");
                for (int i = 0; i < split.length; i++) {
                    var s = split[i];
                    var s1 = o2.trim().split("\n")[0].split("[_ ()\\[\\]\\-+/*|&^$\n\\s]");

                    if (i >= s1.length) return -1;

                    if (!s.equals(s1[i])) return s.compareTo(s1[i]);
                }

                return o1.compareTo(o2);
            }).toList()) {
                List<String> list = member.lines().toList();
                for (String line : list) {
                    sw.append("    ").append(line);
                    sw.append("\n");
                }
                sw.append("\n");
            }
        }

        if (!postInit.isEmpty()) {
            sw.append("\n");
            for (String member : postInit) {
                List<String> list = member.lines().toList();
                for (String line : list) {
                    sw.append(line);
                    sw.append("\n");
                }
                sw.append("\n");
            }
        }

        sw.append("\n}\n");

        return List.of();
    }

    private void addConstructor(MethodInfo methodInfo) {
        this.members.add("""
                /**
                 * %1$s
                 */
                constructor(%2$s) {
                    // Stub
                }
                """.formatted(
                methodInfo.toJSDocSection(),
                methodInfo.getParameters()
        ));
    }

    public String toModifiers(Class<?> clazz) {
        StringBuilder sb = new StringBuilder();

        if (Modifier.isStatic(clazz.getModifiers())) sb.append("static ");
        if (Modifier.isAbstract(clazz.getModifiers()) && Modifier.isInterface(clazz.getModifiers()))
            sb.append("abstract ");

        return sb.toString();
    }

    public void addAbstractMethod(MethodInfo methodInfo) {
        if (methodInfo.getParameters().length == 0) this.members.add("""
                /**
                 * WARNING: NOT IMPLEMENTED. DO NOT CALL UNLESS ON OVERRIDDEN FUNCTION
                 * %2$s
                 */
                %4$s %1$s(): %5$s;
                """.formatted(
                toJavaMemberName(methodInfo.getName()),
                methodInfo.toGenericString(),
                methodInfo.toJSDocSection(),
                "abstract",
                methodInfo.getReturnType()
        ));

        this.members.add("""
                /**
                 * WARNING: NOT IMPLEMENTED. DO NOT CALL UNLESS ON OVERRIDDEN FUNCTION
                 * %2$s
                 */
                %5$s %1$s(%3$s): %6$s;
                """.formatted(
                toJavaMemberName(methodInfo.getName()),
                methodInfo.toGenericString(),
                methodInfo.toParameterList(),
                methodInfo.toJSDocSection(),
                "abstract",
                methodInfo.getReturnType()
        ));
    }

    public void addAbstractMethod(Method method) {
        if (method.getParameters().length == 0) this.members.add("""
                /**
                 * WARNING: NOT IMPLEMENTED. DO NOT CALL UNLESS ON OVERRIDDEN FUNCTION
                 * %2$s
                 */
                %4$s %1$s(): %5$s;
                """.formatted(
                toJavaMemberName(method.getName()),
                method.toGenericString(),
                toTsDocSignatureM(method),
                toModifiers(method),
                toTsType(method.getReturnType())
        ));

        this.members.add("""
                /**
                 * WARNING: NOT IMPLEMENTED. DO NOT CALL UNLESS ON OVERRIDDEN FUNCTION
                 * %2$s
                 */
                %5$s %1$s(%3$s): %6$s;
                """.formatted(
                toJavaMemberName(method.getName()),
                method.toGenericString(),
                toTsSignature(method.getParameters()),
                toTsDocSignatureM(method),
                toModifiers(method),
                toTsType(method.getReturnType())
        ));
    }

    public String toModifiers(Member member) {
        StringBuilder builder = new StringBuilder();

        if (Modifier.isPrivate(member.getModifiers())) builder.append("private ");
        else if (Modifier.isProtected(member.getModifiers())) builder.append("protected ");
        else if (Modifier.isPublic(member.getModifiers())) builder.append("public ");
        else builder.append("package ");

        if (Modifier.isAbstract(member.getModifiers())) builder.append("abstract ");

        if (Modifier.isStatic(member.getModifiers())) builder.append("static ");

        if (Modifier.isNative(member.getModifiers())) builder.append("/*native*/ ");

        if (Modifier.isSynchronized(member.getModifiers())) builder.append("/*synchronized*/ ");

        if (Modifier.isTransient(member.getModifiers())) builder.append("/*transient*/ ");

        if (Modifier.isVolatile(member.getModifiers())) builder.append("/*volatile*/ ");

        if (Modifier.isStrict(member.getModifiers())) builder.append("/*strictfp*/ ");

        if ((member.getModifiers() & 0x00001000) != 0) builder.append("/*synthetic*/ ");

        return builder.toString();
    }

    private String toTsDocSignatureM(Method method) {
        String formatted = """
                 * AUTOMATICALLY GENERATED. DO NOT EDIT.
                 * A wrapped Java method of %s
                """.formatted(method.getDeclaringClass().getName());

        if (Modifier.isFinal(method.getModifiers())) formatted += " * @final";

        return " " + formatted.trim();
    }

    private String toTsDocSignature(Constructor<?> constructor) {
        String formatted = """
                 * AUTOMATICALLY GENERATED. DO NOT EDIT.
                 * A wrapped Java constructor of %s
                """.formatted(constructor.getDeclaringClass().getName());

        if (Modifier.isFinal(constructor.getModifiers())) formatted += " * @final";

        return " " + formatted;
    }

    private String toTsDocSignature(Field field) {
        String formatted = """
                 * AUTOMATICALLY GENERATED. DO NOT EDIT.
                 * A wrapped Java field of %s
                """.formatted(field.getDeclaringClass().getName());

        if (Modifier.isFinal(field.getModifiers())) formatted += " * @final";

        return " " + formatted;
    }

    public String toTsClassSignature(Class<?> clazz, Class<?> superclass, Class<?>... interfaces) {
        StringBuilder builder = new StringBuilder();

        if (clazz == superclass) {
            logger.warning("Class " + clazz.getName() + " is extending itself");
        }

        if (superclass != Object.class) {
            builder.append(", ").append(toTsType(superclass));

            addImport(toTsImport(superclass));
        }

        for (Class<?> anInterface : interfaces) {
            builder.append(", ").append(toTsType(anInterface));

            addImport(toTsImport(anInterface));
        }

        String string = builder.toString();
        if (string.startsWith(", ")) {
            String s = " extends " + string.substring(2);
            if (string.substring(2).isBlank()) return "";
            return s;
        }

        if (string.isBlank()) return "";
        return " extends " + string;
    }

    public void addImport(@Nullable String code) {
        if (code == null) return;

        this.imports.add(code);
    }

    public void addConstructor(Constructor<?> constructor) {
        Parameter[] parameters = constructor.getParameters();
        String name = constructor.getDeclaringClass().getName();
        String[] split = name.split("\\.");
        name = split[split.length - 1];
        if (parameters.length == 0) this.members.add(STUB_CONSTRUCTOR.formatted(
                constructor.toGenericString(),
                name,
                toTsDocSignature(constructor),
                toModifiers(constructor)
        ));

        this.members.add(STUB_CONSTRUCTOR_ARGS.formatted(
                constructor.toGenericString(),
                name,
                toTsSignature(constructor.getParameters()),
                toTsArgumentList(parameters),
                toTsDocSignature(constructor),
                toModifiers(constructor)
        ));
    }

    public String toTsArgumentList(Parameter[] parameters) {
        StringBuilder builder = new StringBuilder();
        builder.append("\n        ");

        for (int i = 0; i < parameters.length; i++) {
            if (i != 0) builder.append(",\n        ");

            Parameter parameter = parameters[i];
            if (parameter.isVarArgs()) builder.append("...");
            builder.append(toTsArgument(parameter.getType(), parameter.getName()));
        }

        String string = builder.toString();
        return "\n        " + string.trim() + "\n    ";
    }

    public @Nullable String toTsPrimitiveType(Class<?> type) {
        if (type == int.class) return "number";
        else if (type == long.class) return "number";
        else if (type == float.class) return "number";
        else if (type == double.class) return "number";
        else if (type == boolean.class) return "boolean";
        else if (type == String.class) return "string";
        else if (type == byte[].class) return "Uint8Array";
        else if (type == Object.class) return "Object";
        else if (type == byte.class) return "number";
        else if (type == short.class) return "number";
        else if (type == char.class) return "string";
        else if (type == void.class) return "void";
        else return null;
    }

    public String toTsArgument(Class<?> type, String expr) {
        if (type == int.class) return "_int.valueOf(" + expr + ")";
        else if (type == long.class) return "_long.valueOf(" + expr + ")";
        else if (type == float.class) return "_float.valueOf(" + expr + ")";
        else if (type == double.class) return "_double.valueOf(" + expr + ")";
        else if (type == boolean.class) return "_boolean.valueOf(" + expr + ")";
        else if (type == String.class) return expr;
        else if (type == void.class) return "undefined";
        else if (type == byte[].class) return "bytes";
        else if (type == Object.class) return expr;
        else if (type == byte.class) return "_byte.valueOf(" + expr + ")";
        else if (type == short.class) return "_short.valueOf(" + expr + ")";
        else if (type == char.class) return "_char.valueOf(" + expr + ")";
        else {
            String name1 = type.getName();
            String[] split = name1.split("\\.");
            return "new " + split[split.length - 1] + "(_dynamic=" + expr + ")";
        }
    }

    public Object toTsSignature(Parameter[] parameters) {
        StringBuilder builder = new StringBuilder();
        for (int i = 0, parametersLength = parameters.length; i < parametersLength; i++) {
            Parameter value = parameters[i];
            if (i != 0) builder.append(", ");

            Class<?> type = value.getType();
            if (!Modifier.isPublic(type.getModifiers()) && !Modifier.isProtected(type.getModifiers())) {
                builder.append(value.getName());
                continue;
            }

            if (value.isVarArgs()) {
                Class<?> componentType = value.getType().getComponentType();
                if (!Modifier.isPublic(componentType.getModifiers()) && !Modifier.isProtected(componentType.getModifiers())) {
                    builder.append("...").append(value.getName()).append(": Object");
                    continue;
                }

                builder.append("...").append(value.getName()).append(": ").append(toTsType(componentType));
                this.addImport(toTsImport(componentType));
                if (i != parametersLength - 1) logger.warning("VarArgs not last parameter: " + value.getName());

                continue;
            }

            String primitiveType = toTsPrimitiveType(type);
            if (primitiveType != null) builder.append("%1$s: %2$s".formatted(
                    value.getName(),
                    primitiveType
            ));
            else {
                Class<?> t = value.getType();
                while (t.isArray()) t = t.getComponentType();

                builder.append("%1$s: %2$s".formatted(
                        value.getName(),
                        toTsType(t)
                ));

                this.addImport(toTsImport(t));
            }
        }

        return builder.toString();
    }

    public void addMethod(MethodInfo method) {
        String name = method.getName();

        this.members.add("""
                /**
                 * Dynamic overload accessor for %1$s
                 */
                %1$s(%3$s): %2$s {
                    // Stub
                    return undefined;
                }
                """.formatted(
                name,
                method.getReturnType(),
                method.toParameterList()
        ));
    }

    public void addMethod(Method method) {
        Parameter[] parameters = method.getParameters();
        String name = toTsMemberName(method.getName());

        if (method.getReturnType() == void.class) {
            if (parameters.length == 0) {
                this.members.add("""
                        /**
                        %4$s
                         */
                        %5$s%1$s(): void;
                        """.formatted(
                        name,
                        method.toGenericString(),
                        toTsMemberCall(method),
                        toTsDocSignatureM(method),
                        toModifiers(method)
                ));

                return;
            }

            this.members.add("""
                    /**
                    %6$s
                     */
                    %7$s%1$s(%4$s): void;
                    """.formatted(
                    name,
                    method.toGenericString(),
                    toTsMemberCall(method),
                    toTsSignature(method.getParameters()),
                    toTsArgumentList(parameters),
                    toTsDocSignatureM(method),
                    toModifiers(method)
            ));

            return;
        }

        if (parameters.length == 0) {
            if (Number.class.isAssignableFrom(method.getReturnType()) || method.getReturnType() == String.class || method.getReturnType() == byte.class || method.getReturnType() == short.class || method.getReturnType() == int.class || method.getReturnType() == long.class || method.getReturnType() == boolean.class || method.getReturnType() == char.class || method.getReturnType() == float.class || method.getReturnType() == double.class) {
                this.addImport(toTsImport(method.getReturnType()));
                this.members.add("""
                        /*
                        %5$s
                         */
                        %6$s%1$s(): %2$s;
                        """.formatted(
                        name,
                        toTsType(method.getReturnType()),
                        method.toGenericString(),
                        toTsMemberCall(method),
                        toTsDocSignatureM(method),
                        toModifiers(method)
                ));

                this.addImport("import {transform} from 'qjs-classpath/quantumjs-helper/core/_helper';");

                return;
            }

            this.members.add("""
                    /**
                    %6$s
                     */
                    %7$s%1$s(): %2$s;
                    """.formatted(
                    name,
                    toTsType(method.getReturnType()),
                    method.toGenericString(),
                    toTsMemberCall(method),
                    toTsType(method.getReturnType()),
                    toTsDocSignatureM(method),
                    toModifiers(method)
            ));

            this.addImport(toTsImport(method.getReturnType()));
            return;
        }

        if (Number.class.isAssignableFrom(method.getReturnType()) || method.getReturnType() == String.class || method.getReturnType() == byte.class || method.getReturnType() == short.class || method.getReturnType() == int.class || method.getReturnType() == long.class || method.getReturnType() == boolean.class || method.getReturnType() == char.class || method.getReturnType() == float.class || method.getReturnType() == double.class) {
            this.addImport(toTsImport(method.getReturnType()));
            this.members.add("""
                    /**
                    %7$s
                     */
                    %8$s%1$s(%5$s): %2$s;
                    """.formatted(
                    name,
                    toTsType(method.getReturnType()),
                    method.toGenericString(),
                    toTsMemberCall(method),
                    toTsSignature(method.getParameters()),
                    toTsArgumentList(parameters),
                    toTsDocSignatureM(method),
                    toModifiers(method)
            ));

            this.addImport("import {transform} from 'qjs-classpath/quantumjs-helper/core/_helper';");

            return;
        }

        this.members.add("""
                /**
                 * %3$s
                %7$s
                 */
                %8$s%1$s(%5$s): %2$s;
                """.formatted(
                name,
                toTsType(method.getReturnType()),
                method.toGenericString(),
                toTsMemberCall(method),
                toTsSignature(method.getParameters()),
                toTsArgumentList(parameters),
                toTsDocSignatureM(method),
                toModifiers(method)
        ));

        this.addImport(toTsImport(method.getReturnType()));
    }

    private Object toTsMemberCall(Member member) {
        String javaMemberName = toJavaMemberName(member.getName());
        if (javaMemberName.startsWith("[")) return javaMemberName;
        return "." + javaMemberName;
    }

    public @NotNull String toTsType(@Nullable Class<?> returnType) {
        if (returnType == null) return "any";
        if (returnType.isArray()) return toTsType(returnType.getComponentType()) + "[]";

        String primitiveType = toTsPrimitiveType(returnType);
        if (primitiveType != null) return primitiveType;

        if (returnType.getPackageName().equals(clazz.getPackageName())) {
            String name = returnType.getName();
            name = name.substring(name.lastIndexOf(".") + 1);
            return name.replace("$", ".");
        }

        String name = returnType.getName();
        String[] split = name.split("\\.");

        return split[split.length - 1];
    }

    public void addField(Field field) {
        if (Modifier.isPrivate(field.getModifiers())) return;

        this.members.add("""
                /**
                 * Getter for the %1$s property.
                 *
                %4%s
                 * @returns {%2$s} - Value of %1$s
                 */
                %5$sget %1$s(): %2$s {
                    // Stub
                    return undefined;
                }
                """.formatted(
                toTsMemberName(field.getName()),
                field.getType().getSimpleName(),
                toTsMemberCall(field),
                toTsDocSignature(field),
                toModifiers(field)
        ));

        if (!Modifier.isFinal(field.getModifiers())) this.members.add("""
                /**
                 * Setter for the %1$s property.
                 *
                %5$s
                 * @param {%2$s} value - New value for %1$s
                 */
                %6$sset %1$s(value: %2$s): void {
                    // Stub
                }
                """.formatted(
                toTsMemberName(field.getName()),
                toTsType(field.getType()),
                toTsMemberAssign(field),
                toTsMemberCall(field),
                toTsDocSignature(field),
                toModifiers(field)
        ));

        this.addImport(toTsImport(field.getType()));
    }

    public void addStaticField(Field field) {
        this.members.add("""
                /**
                 * Getter for the %1$s property.
                 *
                %5$s
                 * @return {%2$s} %4%s - Value of %1$s
                 */
                %6$sget %1$s(): %2$s {
                    // Stub
                    return undefined;
                }
                """.formatted(
                toTsMemberName(field.getName()),
                field.getType().getSimpleName(),
                toJavaMemberName(field.getName()),
                toTsType(field.getDeclaringClass()),
                toTsDocSignature(field),
                toModifiers(field)
        ));

        this.members.add("""
                /**
                 * Setter for the %1$s property.
                 *
                %5$s
                 * @param {%2$s} value - Value of %1$s
                 */
                %6$sset %1$s(value: %2$s): void {
                    // Stub
                }
                """.formatted(
                toTsMemberName(field.getName()),
                toTsType(field.getType()),
                toJavaMemberName(field.getName()),
                toTsType(field.getDeclaringClass()),
                toTsDocSignature(field),
                toModifiers(field)
        ));

        this.addImport(toTsImport(field.getType()));
    }

    public String toJavaMemberName(String name) {
        return switch (name) {
            case "and" -> "['and']";
            case "or" -> "['or']";
            case "xor" -> "['xor']";
            case "not" -> "['not']";
            case "in" -> "['in']";
            case "is" -> "['is']";
            case "==" -> "['eq']";
            case "!=" -> "['ne']";
            case "===" -> "['eeq']";
            case "!==" -> "['ene']";
            case "null" -> "['null']";
            case "true" -> "['true']";
            case "false" -> "['false']";
            case "class" -> "['class']";
            case "function" -> "['function']";
            case "get" -> "['get']";
            case "set" -> "['set']";
            case "new" -> "['new']";
            case "delete" -> "['delete']";
            case "break" -> "['break']";
            case "case" -> "['case']";
            case "catch" -> "['catch']";
            case "continue" -> "['continue']";
            case "debugger" -> "['debugger']";
            case "default" -> "['default']";
            case "do" -> "['do']";
            case "else" -> "['else']";
            case "enum" -> "['enum']";
            case "export" -> "['export']";
            case "extends" -> "['extends']";
            case "instanceof" -> "['instanceof']";
            case "let" -> "['let']";
            case "package" -> "['package']";
            case "private" -> "['private']";
            case "protected" -> "['protected']";
            case "public" -> "['public']";
            case "static" -> "['static']";
            case "super" -> "['super']";
            case "switch" -> "['switch']";
            case "this" -> "['this']";
            case "typeof" -> "['typeof']";
            case "var" -> "['var']";
            case "void" -> "['void']";
            case "implements" -> "['implements']";
            case "interface" -> "['interface']";
            case "except" -> "['except']";
            case "finally" -> "['finally']";
            case "for" -> "['for']";
            case "from" -> "['from']";
            case "global" -> "['global']";
            case "if" -> "['if']";
            case "import" -> "['import']";
            case "throw" -> "['throw']";
            case "return" -> "['return']";
            case "try" -> "['try']";
            case "while" -> "['while']";
            case "with" -> "['with']";
            case "yield" -> "['yield']";
            case "as" -> "['as']";
            case "constructor" -> "['constructor']";
            case "prototype" -> "['prototype']";
            case "arguments" -> "['arguments']";
            case "eval" -> "['eval']";
            case "undefined" -> "['undefined']";
            case "NaN" -> "['NaN']";
            case "Infinity" -> "['Infinity']";
            default -> name;
        };
    }

    public String toTsMemberName(String name) {
        return switch (name) {
            case "and" -> "and_";
            case "or" -> "or_";
            case "xor" -> "xor_";
            case "not" -> "not_";
            case "in" -> "in_";
            case "is" -> "is_";
            case "==" -> "eq_";
            case "!=" -> "ne_";
            case "===" -> "eeq_";
            case "!==" -> "ene_";
            case "null" -> "null_";
            case "true" -> "true_";
            case "false" -> "false_";
            case "class" -> "class_";
            case "function" -> "function_";
            case "get" -> "get_";
            case "set" -> "set_";
            case "new" -> "new_";
            case "delete" -> "delete_";
            case "break" -> "break_";
            case "case" -> "case_";
            case "catch" -> "catch_";
            case "continue" -> "continue_";
            case "debugger" -> "debugger_";
            case "default" -> "default_";
            case "do" -> "do_";
            case "else" -> "else_";
            case "enum" -> "enum_";
            case "export" -> "export_";
            case "extends" -> "extends_";
            case "instanceof" -> "instanceof_";
            case "let" -> "let_";
            case "package" -> "package_";
            case "private" -> "private_";
            case "protected" -> "protected_";
            case "public" -> "public_";
            case "static" -> "static_";
            case "super" -> "super_";
            case "switch" -> "switch_";
            case "this" -> "this_";
            case "typeof" -> "typeof_";
            case "var" -> "var_";
            case "void" -> "void_";
            case "implements" -> "implements_";
            case "interface" -> "interface_";
            case "except" -> "except_";
            case "finally" -> "finally_";
            case "for" -> "for_";
            case "from" -> "from_";
            case "global" -> "global_";
            case "if" -> "if_";
            case "import" -> "import_";
            case "throw" -> "throw_";
            case "return" -> "return_";
            case "try" -> "try_";
            case "while" -> "while_";
            case "with" -> "with_";
            case "yield" -> "yield_";
            case "as" -> "as_";
            case "constructor" -> "constructor_";
            case "prototype" -> "prototype_";
            case "arguments" -> "arguments_";
            case "eval" -> "eval_";
            case "undefined" -> "undefined_";
            case "NaN" -> "NaN_";
            case "Infinity" -> "Infinity_";
            default -> name;
        };
    }

    public void addConstField(Field field) {
        if (field.getType().equals(void.class)) return;

        if (Number.class.isAssignableFrom(field.getType()) && !field.getType().equals(BigInteger.class) && !field.getType().equals(BigDecimal.class)) {
            this.staticMembers.add("""
                    static readonly %2$s: number = undefined; // Stub
                    """.formatted(
                    toTsType(field.getDeclaringClass()),
                    toJavaMemberName(field.getName())
            ));
            return;
        }

        if (String.class.isAssignableFrom(field.getType())) {
            this.staticMembers.add("""
                    static readonly %2$s: string = undefined; // Stub
                    """.formatted(
                    toTsType(field.getDeclaringClass()),
                    toJavaMemberName(field.getName())
            ));
            return;
        } else if (field.getType().equals(Boolean.class)) {
            this.staticMembers.add("""
                    static readonly %2$s: boolean = undefined; // Stub
                    """.formatted(
                    toTsType(field.getDeclaringClass()),
                    toJavaMemberName(field.getName())
            ));
            return;
        } else if (field.getType().equals(Character.class)) {
            this.staticMembers.add("""
                    static readonly %2$s: string = undefined; // Stub
                    """.formatted(
                    toTsType(field.getDeclaringClass()),
                    toJavaMemberName(field.getName())
            ));
            return;
        } else if (field.getType().equals(Byte.class) || field.getType().equals(Short.class) || field.getType().equals(Integer.class) || field.getType().equals(Long.class)) {
            this.staticMembers.add("""
                    static readonly %2$s: number = undefined; // Stub
                    """.formatted(
                    toTsType(field.getDeclaringClass()),
                    toJavaMemberName(field.getName())
            ));
            return;
        } else if (field.getType().equals(Float.class) || field.getType().equals(Double.class)) {
            this.staticMembers.add("""
                    static readonly %2$s: number = undefined; // Stub
                    """.formatted(
                    toTsType(field.getDeclaringClass()),
                    toJavaMemberName(field.getName())
            ));
            return;
        } else if (field.getType().equals(Object.class)) {
            this.staticMembers.add("""
                    static readonly %2$s: object = undefined; // Stub
                    """.formatted(
                    toTsType(field.getDeclaringClass()),
                    toJavaMemberName(field.getName())
            ));
            return;
        }

        if (field.getType().equals(boolean.class)) {
            this.staticMembers.add("""
                    static readonly %2$s: boolean = undefined; // Stub
                    """.formatted(
                    toTsType(field.getDeclaringClass()),
                    toJavaMemberName(field.getName())
            ));
            return;
        } else if (field.getType().equals(char.class)) {
            this.staticMembers.add("""
                    static readonly %2$s: string = undefined; // Stub
                    """.formatted(
                    toTsType(field.getDeclaringClass()),
                    toJavaMemberName(field.getName())
            ));
            return;
        } else if (field.getType() == byte.class || field.getType() == short.class || field.getType() == int.class || field.getType() == long.class) {
            this.staticMembers.add("""
                    static readonly %2$s: number = undefined; // Stub
                    """.formatted(
                    toTsType(field.getDeclaringClass()),
                    toJavaMemberName(field.getName())
            ));
            return;
        } else if (field.getType() == float.class || field.getType() == double.class) {
            this.staticMembers.add("""
                    static readonly %2$s: number = undefined; // Stub
                    """.formatted(
                    toTsType(field.getDeclaringClass()),
                    toJavaMemberName(field.getName())
            ));
            return;
        }

        this.staticMembers.add("""
                static readonly %2$s: %3$s = undefined; // Stub
                """.formatted(
                toTsType(field.getDeclaringClass()),
                toJavaMemberName(field.getName()),
                toTsType(field.getType())

        ));

        this.addImport(toTsImport(field.getType()));
    }

    private String toTsMemberAssign(Member member) {
        String javaMemberName = toJavaMemberName(member.getName());
        if (javaMemberName.startsWith("[")) return javaMemberName;
        return "." + javaMemberName;
    }

    public @Nullable String toTsImport(@Nullable Class<?> type) {
        if (type == null) return null;
        if (type.isArray()) return toTsImport(type.getComponentType());

        try {
            if (type == int.class || type == long.class || type == float.class || type == double.class
                    || type == boolean.class || type == String.class || type == void.class || type == Object.class
                    || type == short.class || type == byte.class || type == char.class)
                return null;
            else {
                String name = type.getName();
                String convert = Converters.convert(name);
                if (convert == null) convert = name;
                return convertImport(clazz, type, type.getPackageName(), convert);
            }
        } catch (Exception e) {
            throw new RuntimeException("Failed to import: " + type.getName(), e);
        }
    }
}
