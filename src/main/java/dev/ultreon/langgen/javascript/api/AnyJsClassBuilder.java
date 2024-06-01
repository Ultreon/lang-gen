package dev.ultreon.langgen.javascript.api;

import dev.ultreon.langgen.api.ClassBuilder;

public interface AnyJsClassBuilder extends ClassBuilder {
    default String convertImport(Class<?> clazz, Class<?> type, String javaName, String jsName) {
        if (type.getName().equals(clazz.getName())) return null;

        String name = type.getName();
        String[] split = name.split("\\.");
        String simpleName = split[split.length - 1].replace("$", "_");

        if (jsName.equals(javaName)) {
            int endIndex = jsName.lastIndexOf(".");
            if (endIndex == -1) {
                return "import {" + simpleName + "} from 'qjs-classpath/" + simpleName + "'; // FIXME: Unchanged";
            }

            String pkg = jsName.substring(0, endIndex).replace(".", "/");
            return "import {" + simpleName + "} from 'qjs-classpath/" + pkg + "/" + simpleName + "'; // FIXME: Unchanged";
        }

        int endIndex = jsName.lastIndexOf(".");
        if (endIndex == -1) {
            return "import {" + simpleName + "} from 'qjs-classpath/" + simpleName + ".mjs';";
        }

        String pkg = jsName.substring(0, endIndex).replace(".", "/");
        return "import {" + simpleName + "} from 'qjs-classpath/" + pkg + "/" + simpleName + ".mjs';";
    }
}
