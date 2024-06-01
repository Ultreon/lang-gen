package dev.ultreon.langgen.javascript.ts;

import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.stream.Collectors;

public class TsFinalClassBuilder extends TsClassBuilder {
    public TsFinalClassBuilder(Class<?> clazz) {
        super(clazz);
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

            this.addMethod(method);
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
            if (code.startsWith("#js_import\n")) {
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
                        %1$s
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
                /**
                 * This class is a wrapper for the {_%1$s} class.
                 * WARNING: THIS IS A FINAL CLASS, YOU CANNOT EXTEND THIS.
                 *
                 * @final
                 */
                export %6$sclass %1$s%5$s {
                \s""".formatted(
                toTsType(clazz).replace("'", "").replace("$", "_").replace(".", "_"),
                toTsClassSignature(clazz, clazz.getSuperclass(), clazz.getInterfaces()),
                clazz.getName().replace("$", "_"),
                collect,
                toTsClassSignature(clazz, clazz.getSuperclass(), clazz.getInterfaces()),
                toModifiers(clazz)));

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

        sw.append("}\n");

        return List.of();
    }
}
