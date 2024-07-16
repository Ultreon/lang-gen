package dev.ultreon.langgen.api;

import java.util.HashSet;
import java.util.Set;

public class PackageExclusions {
    private static Set<String> packageNames = new HashSet<>();

    public static void addExclusion(String packageName) {
        if (packageName.endsWith("."))
            throw new IllegalArgumentException("Cannot end with period.");

        packageNames.add(packageName);
    }

    public static boolean isExcluded(Class<?> type) {
        if (type == String.class) return false;
        for (String name : packageNames) {
            if (type.getName().startsWith(name + "."))
                return true;
        }

        return false;
    }
}
