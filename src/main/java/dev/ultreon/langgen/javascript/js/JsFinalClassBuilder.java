package dev.ultreon.langgen.javascript.js;

import java.lang.reflect.*;
import java.util.*;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.stream.Collectors;

public class JsFinalClassBuilder extends JsClassBuilder {
    public JsFinalClassBuilder(Class<?> clazz) {
        super(clazz);

        addImport(toJavaImport(clazz));
    }

    @Override
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

        sw.append("\n");

        String collect = String.join("\n", imports);
        sw.append("""
                \s
                %4$s
                \s
                function _wrap(java_value) {
                    return %1$s(__dynamic__=java_value)
                }
                \s
                /**
                 * This class is a wrapper for the {_%1$s} class.
                 * WARNING: THIS IS A FINAL CLASS, YOU CANNOT EXTEND THIS.
                 *
                 * @final
                 * @class
                 */
                export class %1$s {
                    /**
                     * WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
                     *
                     * @param {_%1$s} _dynamic - The object to wrap
                     * @constructor
                     */
                    constructor(_dynamic) {
                        this._wrapper = _dynamic
                
                        // Replace this class with the actual class
                        let customInstance = new _%1$s();
                        Object.keys(customInstance).forEach((key) => {
                          this[key] = customInstance[key];
                        });
                    }
                \s""".formatted(
                toJsType(clazz).replace("'", "").replace("$", "_").replace(".", "_"),
                toJsClassSignature(clazz, clazz.getSuperclass(), clazz.getInterfaces()),
                clazz.getName().replace("$", "_"),
                collect));

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

        sw.append("}\n");

        return List.of();
    }
}
