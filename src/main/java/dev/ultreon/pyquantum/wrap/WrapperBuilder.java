package dev.ultreon.pyquantum.wrap;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public abstract class WrapperBuilder {

    public static void buildPath(Path path) throws IOException {
        if (Files.isRegularFile(path) && path.getFileName().toString().endsWith(".jar")) {
            new JarWrapperBuilder(path).build(Paths.get("src/main/python"));
        }
    }

    public abstract void build(Path output) throws IOException;
}
