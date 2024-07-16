package dev.ultreon.langgen.javascript.js;

import dev.ultreon.langgen.api.PackageExclusions;
import dev.ultreon.langgen.javascript.JavascriptGen;
import dev.ultreon.langgen.api.Converters;
import dev.ultreon.langgen.javascript.api.AnyJsClassBuilder;
import kotlin.Pair;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

import java.lang.reflect.*;
import java.util.*;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.logging.Logger;
import java.util.stream.Collectors;

public class JsClassBuilder implements AnyJsClassBuilder {
    public static final String CLASS_FORMAT = """
                    
            class Wrapper {
                constructor(java_value) {
                    this._wrapper = java_value
                }
            }
                        
            function _wrap(java_value) {
                return new %1$s(new Wrapper(java_value))
            }
                        
            function doesExtend(ChildClass, ParentClass) {
                // Access the prototype of the ChildClass
                let prototype = ChildClass.prototype;
                        
                // Loop through the prototype chain
                while (prototype != null) {
                    // Check if the current prototype is the same as the ParentClass prototype
                    if (prototype === ParentClass.prototype) {
                        return true; // ChildClass extends ParentClass
                    }
                    // Move up the prototype chain
                    prototype = Object.getPrototypeOf(prototype);
                }
                        
                return false; // ChildClass does not extend ParentClass
            }
                        
            function convertArray(array, clazz) {
                let i = 0;
                for (const elem in array) {
                    array[i] = new (clazz)(clazz.$$$WRAPPER$$$(elem));
                    i++;
                }
                        
                return array;
            }
            
            function isOfArrayType(array, type) {
                if (!Array.isArray(array)) {
                    return false;
                }
                          
                const elementTypes = array.map(element => Object.prototype.toString.call(element));
                const areSameType = elementTypes.every(type => type === elementTypes[0]);
                          
                return areSameType && elementTypes[0] === type.prototype.toString.call(element);
            }
               
            function toOverload(array) {
                if (!Array.isArray(array)) {
                    throw new TypeError("Invalid data given to method! Overload check ultimately failed!");
                }
                          
                return "(" + array.map(element => Object.prototype.toString.call(element)).join(", ") + ")";
            }
               
            /**
             * This is a wrapper for the {_%1$s} class.
             */
            class %1$s {
                constructor() {        
                    %4$s
                        
                    let args = [];
                    for (let _i = 0; _i < arguments.length; _i++) {
                        args[_i] = arguments[_i];
                    }
                        
                    // Check for argument 0 being Wrapper (in this .mjs file)
                    if (args[0] instanceof Wrapper) {
                        return args[0]._wrapper;
                    }
                        
                    if (Object.getPrototypeOf(this) !== %2$s.prototype) {
                        const dyn = new (Java.extend(Java.type("%3$s")))(this);
                        this["< dynamic >"] = dyn;
                        
                        Object.keys(dyn).forEach(key => {
                            if (this[key] !== undefined) {
                                return;
                            }
                            if (key === "< dynamic >") {
                                throw new Error("Cannot overwrite the dynamic object");
                            }
                            if (key.startsWith("_")) {
                                return;
                            }
                            Object.defineProperty(this, key, {
                                get: function() {
                                    return dyn[key];
                                },
                                set: function(v) {
                                    dyn[key] = v;
                                }
                            });
                        });
                        
            %5$s
                        return;
                    }
                        
                    const dyn = new (Java.type("%3$s"))(...args);
                    this["< dynamic >"] = dyn;
                    
                    Object.keys(this["< dynamic >"]).forEach(key => {
                        if (this[key] !== undefined) {
                            return;
                        }
                        if (key === "< dynamic >") {
                            throw new Error("Cannot overwrite the dynamic object");
                        }
                        if (key.startsWith("_")) {
                            return;
                        }
                        Object.defineProperty(this, key, {
                            get: function() {
                                return this["< dynamic >"][key];
                            },
                            set: function(v) {
                                this["< dynamic >"][key] = v;
                            }
                        });
                    });
                    
            %6$s
                }
                        
                static $$$WRAPPER$$$(element) {
                    return _wrap(element);
                }
            """;
    public static final String STUB_FORMAT = """
                        
            %4$s
            /**
             * This is a wrapper for the {_%1$s} class.
             */
            export class %1$s {
            """;
    protected final Class<?> clazz;
    protected final Set<String> imports = new HashSet<>();
    protected final Set<String> staticMembers = new HashSet<>();
    protected final Set<String> members = new HashSet<>();
    protected final Set<String> postinit = new HashSet<>();
    private final Logger logger = Logger.getLogger("JavascriptClassBuilder");
    private final String className;
    private final String name;

    public JsClassBuilder(Class<?> clazz) {
        this.clazz = clazz;

        addImport(toJavaImport(clazz));

        className = clazz.getName();
        String[] classNameSplit = className.split("\\.");
        name = classNameSplit[classNameSplit.length - 1];
    }

    @Override
    public List<String> build(StringBuilder sw) {
        String methodInjectors12 = toInjectors(clazz.getMethods(), clazz.getFields(), clazz, 12, false);
        String methodInjectors8 = toInjectors(clazz.getMethods(), clazz.getFields(), clazz, 8, false);

        for (Field field : clazz.getFields()) {
            if (Modifier.isStatic(field.getModifiers()) && Modifier.isFinal(field.getModifiers())) {
                addConstField(field);
            } else if (Modifier.isStatic(field.getModifiers())) {
                addStaticField(field);
            }
        }

        for (Method field : clazz.getMethods()) {
            if (Modifier.isStatic(field.getModifiers())) {
                addStaticMethod(field);
            }
        }

        List<String> imports = new ArrayList<>(this.imports);

        sw.append("\n");

        AtomicBoolean importOnce = new AtomicBoolean(false);
        String collect = imports.stream().sorted(Comparator.reverseOrder()).collect(Collectors.joining("\n"));
        sw.append((JavascriptGen.isStub() ? STUB_FORMAT : CLASS_FORMAT).formatted(
                name,
                toJsClassSignature(clazz, clazz.getSuperclass(), clazz.getInterfaces()),
                clazz.getName(),
                (importOnce.get() ? "import {import_once} from 'quantum-js/quantum-js/core';\n" : "") + collect,
                methodInjectors12,
                methodInjectors8));

        Set<String> staticMembers1 = staticMembers;
        if (!staticMembers1.isEmpty()) {
            sw.append("\n");
            for (String member : staticMembers1.stream().sorted((o1, o2) -> {
                if (o1.contains("constructor") && !o2.contains("constructor")) {
                    return 1;
                }
                if (!o1.contains("constructor") && o2.contains("constructor")) {
                    return -1;
                }

                if (o1.contains("static") && !o2.contains("static")) {
                    return 1;
                }
                if (!o1.contains("static") && o2.contains("static")) {
                    return -1;
                }

                if (o1.contains("abstract") && !o2.contains("abstract")) {
                    return 1;
                }
                if (!o1.contains("abstract") && o2.contains("abstract")) {
                    return -1;
                }

                if (o1.contains("final") && !o2.contains("final")) {
                    return 1;
                }
                if (!o1.contains("final") && o2.contains("final")) {
                    return -1;
                }

                if (o1.contains("private") && !o2.contains("private")) {
                    return 1;
                }
                if (!o1.contains("private") && o2.contains("private")) {
                    return -1;
                }

                if (o1.contains("protected") && !o2.contains("protected")) {
                    return 1;
                }
                if (!o1.contains("protected") && o2.contains("protected")) {
                    return -1;
                }

                if (o1.contains("public") && !o2.contains("public")) {
                    return 1;
                }
                if (!o1.contains("public") && o2.contains("public")) {
                    return -1;
                }

                if (o1.contains("function") && !o2.contains("function")) {
                    return 1;
                }
                if (!o1.contains("function") && o2.contains("function")) {
                    return -1;
                }

                String[] split = o1.trim().split("\n")[0].split("[_ ()\\[\\]\\-+/*|&^$\n\\s]");
                for (int i = 0; i < split.length; i++) {
                    var s = split[i];
                    var s1 = o2.trim().split("\n")[0].split("[_ ()\\[\\]\\-+/*|&^$\n\\s]");

                    if (i >= s1.length) {
                        return -1;
                    }

                    if (!s.equals(s1[i])) {
                        return s.compareTo(s1[i]);
                    }
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
                if (o1.contains("constructor") && !o2.contains("constructor")) {
                    return 1;
                }
                if (!o1.contains("constructor") && o2.contains("constructor")) {
                    return -1;
                }

                if (o1.contains("static") && !o2.contains("static")) {
                    return 1;
                }
                if (!o1.contains("static") && o2.contains("static")) {
                    return -1;
                }

                if (o1.contains("abstract") && !o2.contains("abstract")) {
                    return 1;
                }
                if (!o1.contains("abstract") && o2.contains("abstract")) {
                    return -1;
                }

                if (o1.contains("final") && !o2.contains("final")) {
                    return 1;
                }
                if (!o1.contains("final") && o2.contains("final")) {
                    return -1;
                }

                if (o1.contains("private") && !o2.contains("private")) {
                    return 1;
                }
                if (!o1.contains("private") && o2.contains("private")) {
                    return -1;
                }

                if (o1.contains("protected") && !o2.contains("protected")) {
                    return 1;
                }
                if (!o1.contains("protected") && o2.contains("protected")) {
                    return -1;
                }

                if (o1.contains("public") && !o2.contains("public")) {
                    return 1;
                }
                if (!o1.contains("public") && o2.contains("public")) {
                    return -1;
                }

                if (o1.contains("function") && !o2.contains("function")) {
                    return 1;
                }
                if (!o1.contains("function") && o2.contains("function")) {
                    return -1;
                }

                String[] split = o1.trim().split("\n")[0].split("[_ ()\\[\\]\\-+/*|&^$\n\\s]");
                for (int i = 0; i < split.length; i++) {
                    var s = split[i];
                    var s1 = o2.trim().split("\n")[0].split("[_ ()\\[\\]\\-+/*|&^$\n\\s]");

                    if (i >= s1.length) {
                        return -1;
                    }

                    if (!s.equals(s1[i])) {
                        return s.compareTo(s1[i]);
                    }
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

        sw.append("""
                }
                
                """);

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

        if (!JavascriptGen.isStub()) {
            sw.append("""
                    export default %1$s
                
                    /**
                     * Creates a new wrapper for the given java class
                     *
                     * @param {string} javaClassName - the name of the java class
                     * @param {...string} extending - the names of the classes to extend
                     */
                    function createJavaWrapper(javaClassName, ...extending) {
                        let JavaClass = Java.type(javaClassName);
                        if (extending.length > 0) {
                            JavaClass = Java.extend(javaClass, ...extending);
                        }
                    
                        return function(...args) {
                            return new JavaClass(...args);
                        }
                    }
                    """.formatted(name));
        }
        return List.of();
    }

    private String toInjectors(Method[] methods, Field[] fields, Class<?> clazz, int indent, boolean isStatic) {
        StringBuilder builder = new StringBuilder();
        LinkedHashMap<String, List<Pair<String, Method>>> methodsByName = new LinkedHashMap<>();
        LinkedHashMap<String, List<Pair<String, Field>>> fieldsByName = new LinkedHashMap<>();

        for (Method method : methods) {
            if (Modifier.isStatic(method.getModifiers()) != isStatic) continue;
            if ((method.getName().equals("apply") || method.getName().equals("call") || method.getName().equals("bind")) && isStatic) continue;
            StringBuilder paramBuilder = new StringBuilder();
            paramBuilder.append("(");
            for (Class<?> paramType : method.getParameterTypes()) {
                paramBuilder.append(paramType.getName()).append(",");
            }
            if (!paramBuilder.isEmpty())
                paramBuilder.deleteCharAt(paramBuilder.length() -1);

            methodsByName.computeIfAbsent(method.getName(), v -> new ArrayList<>()).add(new Pair<>(paramBuilder + ")", method));
        }

        for (Field field : fields) {
            if (Modifier.isStatic(field.getModifiers()) != isStatic) continue;
            if ((field.getName().equals("apply") || field.getName().equals("call") || field.getName().equals("bind")) && isStatic) continue;
            fieldsByName.computeIfAbsent(field.getName(), v -> new ArrayList<>()).add(new Pair<>(field.getName(), field));
        }

        for (var entry : methodsByName.sequencedEntrySet()) {
            String name = entry.getKey();
            List<Pair<String, Method>> value = entry.getValue();
//            if (fieldsByName.containsKey(name)) {
//                builder.append("dyn['").append(name).append("']").append(" = function() {\n    func = function(...args) {\n        ");
//
//                for (int i = 0, valueSize = value.size(); i < valueSize; i++) {
//                    var methodData = value.get(i);
//                    String signature = methodData.getFirst();
//                    Method method = methodData.getSecond();
//
//                    if (i != 0) builder.append(" else ");
//                    builder.append("if (args.length === ").append(method.getParameterCount());
//
//                    Class<?>[] parameterTypes = method.getParameterTypes();
//                    for (int idx = 0, parameterTypesLength = parameterTypes.length; idx < parameterTypesLength; idx++) {
//                        var type = parameterTypes[idx];
//                        if (type.isArray())
//                            builder.append(" && ").append("isOfArrayType(args[").append(idx).append("], ").append(toJsType(type.getComponentType())).append(")");
//                        else
//                            builder.append(" && ").append("args[").append(idx).append("] instanceof ").append(toJsType(type));
//                    }
//
//                    builder.append(") {\n            ").append("func = dyn['").append(name).append("(").append(signature).append(")'](...args)").append("\n    }");
//                }
//
//                builder.append("    }");
//                builder.append("    function _get() { dyn['").append(name).append("'] }");
//
//                builder.append("""
//                            return
//                        }()
//                        """);
//
//                continue;
//            }

            builder.append("dyn['").append(name).append("'] = function(...args) {\n    ");

            for (int i = 0, valueSize = value.size(); i < valueSize; i++) {
                var methodData = value.get(i);
                String signature = methodData.getFirst();
                Method method = methodData.getSecond();

                if (i != 0) builder.append(" else ");
                builder.append("if (args.length === ").append(method.getParameterCount());

                Class<?>[] parameterTypes = method.getParameterTypes();
                for (int idx = 0, parameterTypesLength = parameterTypes.length; idx < parameterTypesLength; idx++) {
                    var type = parameterTypes[idx];
                    if (type.isArray())
                        builder.append(" && ").append("isOfArrayType(args[").append(idx).append("], ").append(toJsType(type.getComponentType())).append(")");
                    else
                        builder.append(" && ").append("args[").append(idx).append("] instanceof ").append(toJsType(type));
                }

                builder.append(") {\n        ").append("return dyn['").append(name).append("(").append(signature).append(")'](...args)").append("\n    }");
            }

            builder.append(" else { throw new TypeError(`No matching overload found for: ${toOverload(args)}`); }");
            builder.append("\n}\n\n");
        }

        if (isStatic) {

        }

        return builder.toString().indent(indent);
    }

    public void addAbstractMethod(Method method) {
        if (method.getParameters().length == 0) {
            this.members.add("""
                    /**
                     * WARNING: NOT IMPLEMENTED. DO NOT CALL UNLESS ON OVERRIDDEN FUNCTION
                     * %2$s
                     *
                    %3$s
                     */
                    %1$s() {
                        throw new Error("Not implemented");
                    }
                    """.formatted(
                    toJavaMemberName(method),
                    method.toGenericString(),
                    toJsDocSignature(method)
            ));
        }

        this.members.add("""
                /**
                 * WARNING: NOT IMPLEMENTED. DO NOT CALL UNLESS ON OVERRIDDEN FUNCTION
                 * %2$s
                 *
                %4$s
                 */
                %1$s() {
                
                }
                """.formatted(
                toJavaMemberName(method),
                method.toGenericString(),
                toJsSignature(method.getParameters()),
                toJsDocSignature(method)
        ));

        this.addImport(toJavaImport(method.getDeclaringClass()));
    }

    private String toJsDocSignature(Method method) {
        StringBuilder builder = new StringBuilder();

        builder.append(" * AUTOMATICALLY GENERATED. DO NOT EDIT.\n");
        builder.append(" * An wrapped Java method of ").append(method.getDeclaringClass().getName()).append("\n");
        builder.append(" * \n");

        if (Modifier.isAbstract(method.getModifiers())) {
            builder.append(" * @abstract\n");
        }

        if (Modifier.isFinal(method.getModifiers())) {
            builder.append(" * @final\n");
        }

        if (Modifier.isPrivate(method.getModifiers())) {
            builder.append(" * @private\n");
        }

        if (Modifier.isProtected(method.getModifiers())) {
            builder.append(" * @protected\n");
        }

        if (Modifier.isPublic(method.getModifiers())) {
            builder.append(" * @public\n");
        }

        if (!Modifier.isStatic(method.getModifiers())) {
            builder.append(" * @instance\n");
        }

        if (!Modifier.isPrivate(method.getModifiers()) && !Modifier.isProtected(method.getModifiers()) && !Modifier.isPublic(method.getModifiers())) {
            builder.append(" * @package\n");
        }

        if (Modifier.isStatic(method.getModifiers())) {
            builder.append(" * @static\n");
        }

        if (method.isAnnotationPresent(Override.class)) {
            builder.append(" * @override\n");
        }

        builder.append(" * @param {...args} any[] - AUTO GENERATED STUB\n");

        Class<?> returnType = method.getReturnType();
        if (returnType != void.class) {
            String name = returnType.getName();
            String[] split = name.split("\\.");
            name = split[split.length - 1];

            String primitiveType = toJsPrimitiveType(returnType);
            builder.append(primitiveType != null
                    ? " * @returns {" + primitiveType + "} - AUTO GENERATED STUB\n"
                    : " * @returns {" + name + "} - AUTO GENERATED STUB\n");
        }

        return builder.substring(0, builder.length() - 1);
    }

    public String toJsClassSignature(Class<?> clazz, Class<?> superclass, Class<?>... interfaces) {
        StringBuilder builder = new StringBuilder();
        builder.append(", ").append(toJavaType(clazz, "_"));

        String string = builder.toString();
        if (string.startsWith(", ")) {
            return string.substring(2);
        }
        return string;
    }

    public void addImport(@Nullable String code) {
        if (code == null) return;

        this.imports.add(code);
    }

    public String toJsArgumentList(Parameter[] parameters) {
        StringBuilder builder = new StringBuilder();
        builder.append("\n        ");

        for (int i = 0; i < parameters.length; i++) {
            if (i != 0) {
                builder.append(",\n        ");
            }

            Parameter parameter = parameters[i];
            if (parameter.isVarArgs()) {
                builder.append("...");
            }
            builder.append(toJsArgument(parameter.getType(), parameter.getName()));

            if (parameter.getType() == int.class) {
                this.addImport("const _int = Java.type('java.lang.Integer')");
            } else if (parameter.getType() == long.class) {
                this.addImport("const _long = Java.type('java.lang.Long')");
            } else if (parameter.getType() == float.class) {
                this.addImport("const _float = Java.type('java.lang.Float')");
            } else if (parameter.getType() == double.class) {
                this.addImport("const _double = Java.type('java.lang.Double')");
            } else if (parameter.getType() == boolean.class) {
                this.addImport("const _boolean = Java.type('java.lang.Boolean')");
            } else if (parameter.getType() == String.class) {
                this.addImport("const _string = Java.type('java.lang.String')");
            } else if (parameter.getType() == byte.class) {
                this.addImport("const _byte = Java.type('java.lang.Byte')");
            } else if (parameter.getType() == short.class) {
                this.addImport("const _short = Java.type('java.lang.Short')");
            } else if (parameter.getType() == char.class) {
                this.addImport("const _char = Java.type('java.lang.Character')");
            } else if (parameter.getType() == void.class) {
                this.addImport("const _void = Java.type('java.lang.Void')");
            } else if (parameter.getType() == Object.class) {
                this.addImport("const _object = Java.type('java.lang.Object')");
            } else {
                this.addImport(toJavaImport(parameter.getType()));
            }

            this.addImport(toJsImport(parameter.getType()));
        }

        String string = builder.toString();
        return "\n        " + string.trim() + "\n    ";
    }

    @Nullable
    public String toJsPrimitiveType(Class<?> type) {
        if (type == int.class) {
            return "number";
        } else if (type == long.class) {
            return "number";
        } else if (type == float.class) {
            return "number";
        } else if (type == double.class) {
            return "number";
        } else if (type == boolean.class) {
            return "boolean";
        } else if (type == String.class) {
            return "string";
        } else if (type == byte[].class) {
            return "Uint8Array";
        } else if (type == Object.class) {
            return "Any";
        } else if (type == byte.class) {
            return "number";
        } else if (type == short.class) {
            return "number";
        } else if (type == char.class) {
            return "string";
        } else if (type == void.class) {
            return "void";
        } else {
            return null;
        }
    }

    public String toJsArgument(Class<?> type, String expr) {
        if (type.isArray()) {
            return "convertArray(" + toJsArgument(type.getComponentType(), expr) + ", " + toJsType(type.getComponentType()) + ")";
        }

        if (type == int.class) {
            return "_int.valueOf(" + expr + ")";
        } else if (type == long.class) {
            return "_long.valueOf(" + expr + ")";
        } else if (type == float.class) {
            return "_float.valueOf(" + expr + ")";
        } else if (type == double.class) {
            return "_double.valueOf(" + expr + ")";
        } else if (type == boolean.class) {
            return "_boolean.valueOf(" + expr + ")";
        } else if (type == String.class) {
            return expr;
        } else if (type == void.class) {
            return "undefined";
        } else if (type == byte[].class) {
            return "bytes";
        } else if (type == Object.class) {
            return expr;
        } else if (type == byte.class) {
            return "_byte.valueOf(" + expr + ")";
        } else if (type == short.class) {
            return "_short.valueOf(" + expr + ")";
        } else if (type == char.class) {
            return "_char.valueOf(" + expr + ")";
        } else {
            return toJsType(type) + ".$$$WRAPPER$$$(" + expr + ")";
        }
    }

    public Object toJsSignature(Parameter[] parameters) {
        StringBuilder builder = new StringBuilder();
        for (int i = 0, parametersLength = parameters.length; i < parametersLength; i++) {
            Parameter value = parameters[i];
            if (i != 0) {
                builder.append(", ");
            }

            Class<?> type = value.getType();
            if (!Modifier.isPublic(type.getModifiers()) && !Modifier.isProtected(type.getModifiers())) {
                builder.append(value.getName());
                continue;
            }

            if (value.isVarArgs()) {
                Class<?> componentType = value.getType().getComponentType();
                if (!Modifier.isPublic(componentType.getModifiers()) && !Modifier.isProtected(componentType.getModifiers())) {
                    builder.append("...").append(value.getName()).append(": Any");
                    continue;
                }

                builder.append("...").append(value.getName()).append(": ").append(toJsType(componentType));
                this.addImport(toJsImport(componentType));
                if (i != parametersLength - 1) {
                    logger.warning("VarArgs not last parameter: " + value.getName());
                }

                continue;
            }

            String primitiveType = toJsPrimitiveType(type);
            if (primitiveType != null) {
                builder.append("%1$s".formatted(
                        value.getName(),
                        primitiveType
                ));
            } else {
                Class<?> t = value.getType();
                while (t.isArray()) {
                    t = t.getComponentType();
                }

                builder.append("%1$s".formatted(
                        value.getName(),
                        toJsType(t)
                ));

                this.addImport(toJsImport(t));
            }
        }

        return builder.toString();
    }

    public void addMethod(Method method) {
        Parameter[] parameters = method.getParameters();
        String name = toJsMemberName(method);

        String override = "";
        try {
            if (clazz.getSuperclass() != null) {
                clazz.getSuperclass().getMethod(name, method.getParameterTypes());
            } else {
                for (Class<?> interfaceClass : clazz.getInterfaces()) {
                    try {
                        interfaceClass.getMethod(name, method.getParameterTypes());
                    } catch (NoSuchMethodException ignored) {

                    }
                }
            }
        } catch (NoSuchMethodException e) {
            for (Class<?> interfaceClass : clazz.getInterfaces()) {
                try {
                    interfaceClass.getMethod(name, method.getParameterTypes());
                } catch (NoSuchMethodException ignored) {

                }
            }
        }

        if (method.getReturnType() == void.class) {
            if (parameters.length == 0) {
                this.members.add(override + """
                        /**
                        %4$s
                         */
                        %1$s() {
                            // Stub
                        }
                        """.formatted(
                        name,
                        method.toGenericString(),
                        toJsMemberCall(method),
                        toJsDocSignature(method)
                ));

                return;
            }

            this.members.add(override + """
                    /**
                    %6$s
                     */
                    %1$s(%4$s) {
                        // Stub
                    }
                    """.formatted(
                    name,
                    method.toGenericString(),
                    toJsMemberCall(method),
                    toJsSignature(parameters),
                    toJsArgumentList(parameters),
                    toJsDocSignature(method)
            ));

            return;
        }

        if (parameters.length == 0) {
            if (Number.class.isAssignableFrom(method.getReturnType()) || method.getReturnType() == String.class || method.getReturnType() == byte.class || method.getReturnType() == short.class || method.getReturnType() == int.class || method.getReturnType() == long.class || method.getReturnType() == boolean.class || method.getReturnType() == char.class || method.getReturnType() == float.class || method.getReturnType() == double.class) {
                this.addImport(toJsImport(method.getReturnType()));
                this.members.add(override + """
                        /*
                        %5$s
                         */
                        %1$s() {
                            // Stub
                        }
                        """.formatted(
                        name,
                        toJsType(method.getReturnType()),
                        method.toGenericString(),
                        toJsMemberCall(method),
                        toJsDocSignature(method)
                ));

                this.addImport("import {transform} from 'quantum-js/quantum-js/core/_helper';");

                return;
            }

            this.members.add(override + """
                    /**
                    %6$s
                     */
                    %1$s() {
                        // Stub
                    }
                    """.formatted(
                    name,
                    toJsType(method.getReturnType()),
                    method.toGenericString(),
                    toJsMemberCall(method),
                    toJsType(method.getReturnType()),
                    toJsDocSignature(method)
            ));

            this.addImport(toJsImport(method.getReturnType()));
            this.addImport(toJavaImport(method.getReturnType()));
            return;
        }

        if (Number.class.isAssignableFrom(method.getReturnType()) || method.getReturnType() == String.class || method.getReturnType() == byte.class || method.getReturnType() == short.class || method.getReturnType() == int.class || method.getReturnType() == long.class || method.getReturnType() == boolean.class || method.getReturnType() == char.class || method.getReturnType() == float.class || method.getReturnType() == double.class) {
            this.addImport(toJsImport(method.getReturnType()));
            this.members.add(override + """
                    /**
                    %7$s
                     */
                    %1$s(%5$s) {
                        // Stub
                    }
                    """.formatted(
                    name,
                    toJsType(method.getReturnType()),
                    method.toGenericString(),
                    toJsMemberCall(method),
                    toJsSignature(parameters),
                    toJsArgumentList(parameters),
                    toJsDocSignature(method)
            ));

            this.addImport("import {transform} from 'quantum-js/quantum-js/core/_helper';");

            return;
        }

        this.members.add("""
                /**
                 * %3$s
                %7$s
                 */
                %1$s(%5$s) {
                    // Stub
                }
                """.formatted(
                name,
                toJsType(method.getReturnType()),
                method.toGenericString(),
                toJsMemberCall(method),
                toJsSignature(parameters),
                toJsArgumentList(parameters),
                toJsDocSignature(method)
        ));

        this.addImport(toJsImport(method.getReturnType()));
        this.addImport(toJavaImport(method.getReturnType()));
        this.addImport(toJavaImport(method.getDeclaringClass()));
    }

    private Object toJsMemberCall(Member member) {
        String javaMemberName = toJavaMemberName(member);
        if (javaMemberName.startsWith("[")) {
            return javaMemberName;
        }
        return "." + javaMemberName;
    }

    public void addStaticMethod(Method method) {
        if (method.getDeclaringClass() != clazz) return;

        String s = toJsMemberName(method);
        Parameter[] parameters = method.getParameters();
        if (method.getReturnType() == void.class) {
            this.members.add("""
                    /**
                     * %2$s
                     *
                    %7$s
                     */
                    static %1$s(...args) {
                        %3$s.%1$s(...args)
                    }
                    """.formatted(
                    s,
                    method.toGenericString(),
                    toJavaType(clazz),
                    toJsMemberCall(method),
                    toJsSignature(parameters),
                    toJsArgumentList(parameters),
                    toJsDocSignature(method)
            ));

            this.addImport(toJavaImport(method.getDeclaringClass()));
            return;
        }

        if (Number.class.isAssignableFrom(method.getReturnType()) || method.getReturnType() == String.class || method.getReturnType() == byte.class || method.getReturnType() == short.class || method.getReturnType() == int.class || method.getReturnType() == long.class || method.getReturnType() == boolean.class || method.getReturnType() == char.class || method.getReturnType() == float.class || method.getReturnType() == double.class) {
            this.addImport(toJsImport(method.getReturnType()));
            this.members.add("""
                    /**
                     * %3$s
                     *
                    %8$s
                     */
                    static %1$s(...args) {
                        return %4$s.%1$s(...args)
                    }
                    """.formatted(
                    s,
                    toJsType(method.getReturnType()),
                    method.toGenericString(),
                    toJavaType(method.getReturnType()),
                    toJsMemberCall(method),
                    toJsSignature(parameters),
                    toJsArgumentList(parameters),
                    toJsDocSignature(method)
            ));

            this.addImport(toJavaImport(method.getDeclaringClass()));
            return;
        }

        if (method.getReturnType().isArray()) {
            if (Number.class.isAssignableFrom(method.getReturnType()) || method.getReturnType().getComponentType() == String.class || method.getReturnType().getComponentType() == byte.class || method.getReturnType().getComponentType() == short.class || method.getReturnType().getComponentType() == int.class || method.getReturnType().getComponentType() == long.class || method.getReturnType().getComponentType() == boolean.class || method.getReturnType().getComponentType() == char.class || method.getReturnType().getComponentType() == float.class || method.getReturnType().getComponentType() == double.class) {

                this.members.add("""
                    /**
                     * %3$s
                     *
                    %9$s
                     */
                    static %1$s(...args) {
                        return %4$s.%1$s(...args)
                    }
                    """.formatted(
                        s,
                        toJsType(method.getReturnType().getComponentType()),
                        method.toGenericString(),
                        toJavaType(method.getDeclaringClass()),
                        toJsMemberCall(method),
                        toJsSignature(parameters),
                        toJsArgumentList(parameters),
                        toJsType(method.getReturnType()),
                        toJsDocSignature(method)
                ));
                return;
            }
            this.members.add("""
                    /**
                     * %3$s
                     *
                    %9$s
                     */
                    static %1$s(...args) {
                        return convertArray(%2$s.$$$WRAPPER$$$(%4$s.%1$s(...args)))
                    }
                    """.formatted(
                    s,
                    toJsType(method.getReturnType().getComponentType()),
                    method.toGenericString(),
                    toJavaType(method.getDeclaringClass()),
                    toJsMemberCall(method),
                    toJsSignature(parameters),
                    toJsArgumentList(parameters),
                    toJsType(method.getReturnType()),
                    toJsDocSignature(method)
            ));

            return;
        }

        this.members.add("""
                /**
                 * %3$s
                 *
                %9$s
                 */
                static %1$s(...args) {
                    return %2$s.$$$WRAPPER$$$(%4$s.%1$s(...args))
                }
                """.formatted(
                s,
                toJsType(method.getReturnType()),
                method.toGenericString(),
                toJavaType(method.getDeclaringClass()),
                toJsMemberCall(method),
                toJsSignature(parameters),
                toJsArgumentList(parameters),
                toJsType(method.getReturnType()),
                toJsDocSignature(method)
        ));

        this.addImport(toJsImport(method.getReturnType()));
        this.addImport(toJavaImport(method.getReturnType()));
        this.addImport(toJavaImport(method.getDeclaringClass()));
    }

    @Nullable
    private String toJavaImport1(Class<?> returnType) {
        if (returnType.equals(clazz)) return "";
        return toJavaImport(returnType);
    }

    public @NotNull String toJsType(Class<?> returnType) {
        if (PackageExclusions.isExcluded(returnType)) return "Object";

        if (returnType.isArray()) {
            return toJsType(returnType.getComponentType()) + "[]";
        }

        String primitiveType = toJsPrimitiveType(returnType);
        if (primitiveType != null) {
            return primitiveType;
        }

        if (returnType == clazz) {
            return this.name;
        }

        String name = Converters.convert(returnType.getName());
        if (name == null) name = returnType.getName();

        addImport(toJsImport(returnType));
        return name.replace(".", "$");
    }

    public @Nullable String toJavaType(Class<?> returnType, String prefix) {
        if (returnType.isArray()) {
            return toJsType(returnType.getComponentType()) + "[]";
        }

        String primitiveType = toJsPrimitiveType(returnType);
        if (primitiveType != null) {
            return null;
        }

        String name = returnType.getName();
        if (prefix == "_")
            addImport(toJavaImport(returnType));
        return prefix + name.replace(".", "$");
    }

    public void addField(Field field) {
        if (Modifier.isPrivate(field.getModifiers())) {
            return;
        }

        this.members.add("""
                /**
                 * Getter for the %1$s property.
                 *
                 * @instance
                 * @return %2$s - Value of %1$s
                 */
                get %1$s() {
                    return %2$s._wrap(this._wrapper%3$s);
                }
                """.formatted(
                toJsMemberName(field),
                field.getType().getSimpleName(),
                toJsMemberCall(field)
        ));

        if (!Modifier.isFinal(field.getModifiers())) {
            this.members.add("""
                    /**
                     * Setter for the %1$s property.
                     *
                     * @instance
                     * @param {%2$s} value - New value for %1$s
                     */
                    set %1$s(value) {
                        super%3$s = value._wrapper%4$s;
                    }
                    """.formatted(
                    toJsMemberName(field),
                    toJsType(field.getType()),
                    toJsMemberAssign(field),
                    toJsMemberCall(field)
            ));
        }

        this.addImport(toJsImport(field.getType()));
        this.addImport(toJavaImport(field.getType()));
    }

    public void addStaticField(Field field) {
        this.members.add("""
                /**
                 * Getter for the %1$s property.
                 *
                 * @static
                 * @return {%2$s} %4%s - Value of %1$s
                 */
                static get %1$s() {
                    return _%4$s.%3$s;
                }
                """.formatted(
                toJsMemberName(field),
                field.getType().getSimpleName(),
                toJavaMemberName(field),
                toJsType(field.getDeclaringClass())
        ));

        this.members.add("""
                /**
                 * Setter for the %1$s property.
                 *
                 * @static
                 * @param {%2$s} value - Value of %1$s
                 */
                static set %1$s(value) {
                    _%4$s.%3$s = value;
                }
                """.formatted(
                toJsMemberName(field),
                toJsType(field.getType()),
                toJavaMemberName(field),
                toJsType(field.getDeclaringClass())
        ));

        this.addImport(toJsImport(field.getType()));
        this.addImport(toJavaImport(field.getType()));
    }

    public String toJavaMemberName(Member field) {
        return switch (field.getName()) {
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
            default -> field.getName().replace('$', '_');
        };
    }

    public String toJsMemberName(Member field) {
        return switch (field.getName()) {
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
            default -> field.getName().replace('$', '_');
        };
    }

    public void addConstField(Field field) {
        if (field.getType() == byte.class ||
            field.getType() == short.class ||
            field.getType() == int.class ||
            field.getType() == long.class ||
            field.getType() == float.class ||
            field.getType() == double.class ||
            field.getType() == Object.class ||
            field.getType() == void.class ||
            field.getType() == String.class
        ) {
            this.staticMembers.add("""
                    /**
                     * @static
                     * @readonly
                     * @type {%3$s}
                     */
                    static %2$s
                    """.formatted(
                    toJavaType(field.getDeclaringClass()),
                    toJavaMemberName(field),
                    toJsType(field.getType())

            ));
            this.postinit.add("""
                    /**
                     * @static
                     * @readonly
                     * @type {%3$s}
                     */
                    %4$s.%2$s = %1$s.%2$s
                    """.formatted(
                    toJavaType(field.getDeclaringClass()),
                    toJavaMemberName(field),
                    toJsType(field.getType()),
                    toJsType(field.getDeclaringClass())
            ));
            return;
        }

        if (field.getType().isArray()) {
            if (field.getType().getComponentType() == byte.class ||
                field.getType().getComponentType() == short.class ||
                field.getType().getComponentType() == int.class ||
                field.getType().getComponentType() == long.class ||
                field.getType().getComponentType() == float.class ||
                field.getType().getComponentType() == double.class ||
                field.getType().getComponentType() == Object.class ||
                field.getType().getComponentType() == void.class ||
                field.getType().getComponentType() == String.class
            ) {
                this.staticMembers.add("""
                        /**
                         * @static
                         * @readonly
                         * @type {%3$s}
                         */
                        static %2$s
                        """.formatted(
                        toJavaType(field.getDeclaringClass()),
                        toJavaMemberName(field),
                        toJsType(field.getType())

                ));
                this.postinit.add("""
                    /**
                     * @static
                     * @readonly
                     * @type {%3$s}
                     */
                    %4$s.%2$s = %1$s.%2$s
                    """.formatted(
                        toJavaType(field.getDeclaringClass()),
                        toJavaMemberName(field),
                        toJsType(field.getType()),
                        toJsType(field.getDeclaringClass())
                ));
                return;
            }

            this.staticMembers.add("""
                    /**
                     * @static
                     * @readonly
                     * @type {%3$s}
                     */
                    static %2$s
                    """.formatted(
                    toJavaType(field.getDeclaringClass()),
                    toJavaMemberName(field),
                    toJsType(field.getType().getComponentType())
            ));
            this.postinit.add("""
                    /**
                     * @static
                     * @readonly
                     * @type {%3$s}
                     */
                    %4$s.%2$s = convertArray(%1$s.%2$s, %3$s)
                    """.formatted(
                    toJavaType(field.getDeclaringClass()),
                    toJavaMemberName(field),
                    toJsType(field.getType().getComponentType()),
                    toJsType(field.getDeclaringClass())
            ));
            return;
        }

        this.staticMembers.add("""
                /**
                 * @static
                 * @readonly
                 * @type {%3$s}
                 */
                static %2$s
                """.formatted(
                toJavaType(field.getDeclaringClass()),
                toJavaMemberName(field),
                toJsType(field.getType())
        ));

        this.postinit.add("""
                    /**
                     * @static
                     * @readonly
                     * @type {%3$s}
                     */
                    %4$s.%2$s = %3$s.$$$WRAPPER$$$(%1$s.%2$s)
                    """.formatted(
                toJavaType(field.getDeclaringClass()),
                toJavaMemberName(field),
                toJsType(field.getType()),
                toJsType(field.getDeclaringClass())
        ));
    }

    private @Nullable String toJavaType(Class<?> declaringClass) {
        return toJavaType(declaringClass, "_");
    }

    private Object toJsMemberAssign(Member member) {
        String javaMemberName = toJavaMemberName(member);
        if (javaMemberName.startsWith("[")) {
            return javaMemberName;
        }
        return "." + javaMemberName;
    }

    public @Nullable String toJavaImport(@Nullable Class<?> type) {
        if (type == null) {
            return null;
        }

        if (PackageExclusions.isExcluded(type)) {
            return null;
        }

        if (type.isArray()) {
            return toJavaImport(type.getComponentType());
        }

        if (type.isPrimitive()) {
            return null;
        }

        String extra = "";
        if (Objects.equals(toJsImport(type), toJavaImport0(type))) {
            extra = "\n" + toJavaImport0(type);
        }

        String importName = type.getName().replace(".", "$");
        return "const _" + importName + " = Java.type('" + type.getName() + "');" + extra;
    }

    public @Nullable String toJavaImport0(@Nullable Class<?> type) {
        if (type == null) return null;
        if (type.isArray()) return toJavaImport(type.getComponentType());
        if (type.isPrimitive()) return null;

        String replace1 = type.getName().split("\\$")[0];
        return "const " + replace1 + " = Java.type('" + type.getName() + "');";
    }

    public @Nullable String toJsImport(@Nullable Class<?> type) {
        if (type == null) return null;
        if (type.isArray()) return toJsImport(type.getComponentType());
        if (type.isPrimitive()) return null;
        if (PackageExclusions.isExcluded(type)) return null;

        try {
            if (type == String.class || type == void.class || type == Object.class)
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
