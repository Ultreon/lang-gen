package dev.ultreon.langgen;

import dev.ultreon.langgen.javascript.JavascriptGen;
import dev.ultreon.langgen.python.PythonGen;
import joptsimple.OptionParser;
import joptsimple.OptionSet;
import joptsimple.OptionSpec;
import joptsimple.ValueConverter;
import joptsimple.util.PathConverter;
import org.checkerframework.checker.regex.qual.Regex;
import org.intellij.lang.annotations.Language;
import org.intellij.lang.annotations.Pattern;

import java.io.File;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        OptionParser parser = new OptionParser(true);
        OptionSpec<Boolean> py = parser.acceptsAll(List.of("py", "python"), "Generate Python files").withOptionalArg().ofType(Boolean.class).defaultsTo(false);
        OptionSpec<Boolean> js = parser.acceptsAll(List.of("js", "javascript"), "Generate Javascript files").withOptionalArg().ofType(Boolean.class).defaultsTo(false);
        OptionSpec<Boolean> debug = parser.acceptsAll(List.of("debug"), "Debug mode").withOptionalArg().ofType(Boolean.class).defaultsTo(false);
        OptionSpec<Boolean> stub = parser.acceptsAll(List.of("stub"), "Stub mode").withOptionalArg().ofType(Boolean.class).defaultsTo(false);
        OptionSpec<Boolean> help = parser.acceptsAll(List.of("help"), "Help").withOptionalArg().ofType(Boolean.class).defaultsTo(false);
        OptionSpec<Path> output = parser.acceptsAll(List.of("o", "output"), "Output directory").withRequiredArg().ofType(File.class).withValuesConvertedBy(new PathConverter());

        OptionSet options = parser.parse(args);

        if (options.has(help) || args.length == 0) {
            parser.printHelpOn(System.out);
            System.exit(0);
            return;
        }

        if (options.has("py") || options.has("python")) {
            new PythonGen().write(options, output.value(options));
        } else {
            new JavascriptGen().write(options, output.value(options));

        }
    }
}
