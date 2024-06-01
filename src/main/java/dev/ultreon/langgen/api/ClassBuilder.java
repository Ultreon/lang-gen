package dev.ultreon.langgen.api;

import org.jetbrains.annotations.Nullable;

import java.util.List;

public interface ClassBuilder {
    List<String> build(StringBuilder sw);

    @Nullable
    String convertImport(Class<?> clazz, Class<?> type, String java, String python);
}
