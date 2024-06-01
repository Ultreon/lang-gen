package dev.ultreon.langgen.python;

import java.lang.reflect.*;
import java.util.*;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.stream.Collectors;

public class PyFinalClassBuilder extends PyClassBuilder {
    public PyFinalClassBuilder(Class<?> clazz) {
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
                @final
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
                toPyAnno(clazz).replace("'", "").replace("$", "_").replace(".", "_"),
                toPyClassSignature(clazz, clazz.getSuperclass(), clazz.getInterfaces()),
                clazz.getName().replace("$", "_"),
                (importOnce.get() ? """
                        from pyquantum_helper import import_once as _import_once
                        from pyquantum_helper import final
                        """ : "") + collect));

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
}
