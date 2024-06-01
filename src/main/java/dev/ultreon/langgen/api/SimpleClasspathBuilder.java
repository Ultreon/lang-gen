package dev.ultreon.langgen.api;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.jetbrains.annotations.Nullable;

import java.io.IOException;
import java.lang.reflect.Modifier;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.function.Function;

public final class SimpleClasspathBuilder extends ClasspathBuilder {
    private final Logger logger;
    private final String extension;
    private final Function<Class<?>, ClassBuilder> finalClassBuilder;
    private final Function<Class<?>, ClassBuilder> classBuilder;

    public SimpleClasspathBuilder(String extension, Function<Class<?>, ClassBuilder> finalClassBuilder, Function<Class<?>, ClassBuilder> classBuilder) {
        super(false);
        this.finalClassBuilder = finalClassBuilder;
        this.classBuilder = classBuilder;
        if (!extension.startsWith(".")) {
            extension = "." + extension;
        }

        this.extension = extension;
        this.logger = LogManager.getLogger("ClasspathBuilder" + extension);
    }

    @Override
    protected void writeFile(Path output, String className, String result) throws IOException {
        if (result.isBlank()) {
            throw new GeneratorException("Class " + className + " has no content");
        }

        String filePath = Converters.convert(className);
        if (filePath == null) {
            filePath = className;
        }
        Path path = output.resolve(filePath.replace('.', '/') + extension);

        Files.createDirectories(path.getParent());
        Files.writeString(path, result);
    }

    @Override
    protected @Nullable String visitClass(Class<?> clazz, StringBuilder sb) {
        StringBuilder builder = new StringBuilder();

        try {
            ClassBuilder chosen = Modifier.isFinal(clazz.getModifiers())
                    ? this.finalClassBuilder.apply(clazz)
                    : this.classBuilder.apply(clazz);

            List<String> imports = chosen.build(builder);

            for (String anImport : imports) {
                sb.append(anImport).append('\n');
            }
        } catch (GeneratorException e) {
            throw e;
        } catch (Throwable e) {
            logger.warn(e.getMessage(), e);
            return null;
        }

        String trim = builder.toString().trim();
        if (!trim.isEmpty()) {
            sb.append(trim);
        } else {
            logger.warn("{} has no content", clazz.getName());
        }

        return sb.toString();
    }

    @Override
    protected Logger getLogger() {
        return logger;
    }

    @Override
    public String transformName(Class<?> entry) {
        String convert = Converters.convert(entry.getName());
        if (convert != null && !convert.equals(entry.getName())) {
            return convert;
        }

        return entry.getName();
    }
}
