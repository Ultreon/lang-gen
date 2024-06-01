package dev.ultreon.langgen.api;

import java.io.IOException;
import java.nio.file.Path;

public abstract class ClasspathWrapper {
    public Thread build(Path output) throws IOException {
        Thread builder = new Thread(() -> {
            try {
                doBuild(output);
            } catch (GeneratorException e) {
                e.printStackTrace();
                Runtime.getRuntime().halt(1);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        });
        builder.start();
        return builder;
    }

    protected abstract void doBuild(Path output) throws IOException;
}
