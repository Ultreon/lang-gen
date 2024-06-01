package dev.ultreon.langgen.api;

import joptsimple.OptionSet;

import java.nio.file.Path;

public interface LangGenerator {
    @SuppressWarnings("SpellCheckingInspection")
    void registerConverters();

    void write(OptionSet options, Path output);
}
