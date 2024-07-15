package dev.ultreon.langgen.javascript.api;

import dev.ultreon.langgen.api.ClassBuilder;
import dev.ultreon.langgen.api.Converters;
import org.jetbrains.annotations.NotNull;

import java.util.Arrays;
import java.util.stream.Collectors;

public interface AnyJsClassBuilder extends ClassBuilder {
    default String convertImport(Class<?> owner, Class<?> target, String javaName, String targetName) {
        try {
            if (target.getName().equals(owner.getName())) return null;

            String prefix = prefix(owner);

            String name = target.getName();
            String[] split = name.split("\\.");
            String simpleName = split[split.length - 1];

            if (targetName.equals(javaName)) {
                int endIndex = targetName.lastIndexOf(".");
                if (endIndex == -1) {
                    return "import " + simpleName + " from './" + prefix + "/" + simpleName + ".mts'; // FIXME: Unchanged";
                }

                String pkg = targetName.substring(0, endIndex).replace(".", "/");
                return "import " + simpleName + " from './" + prefix + "/" + pkg + "/" + simpleName + ".mts'; // FIXME: Unchanged";
            }

            int endIndex = targetName.lastIndexOf(".");
            if (endIndex == -1) {
                return "import " + simpleName + " from './" + prefix + "/" + simpleName + ".mts';";
            }

            String pkg = targetName.substring(0, endIndex).replace(".", "/");
            return "import " + simpleName + " from './" + prefix + "/" + pkg + "/" + simpleName + ".mts';";
        } catch (Exception e) {
            throw new Error("Something went wrong", e);
        }
    }

    static @NotNull String prefix(Class<?> owner) {
        String convert = Converters.convert(owner.getName());

        if (convert == null) convert = owner.getName();
        String prefix = Arrays.stream(convert.split("\\.")).map(v -> "..").collect(Collectors.joining("/"));
        if (prefix.endsWith("/..")) prefix = prefix.substring(0, prefix.length() - 3);
        return prefix;
    }
}
