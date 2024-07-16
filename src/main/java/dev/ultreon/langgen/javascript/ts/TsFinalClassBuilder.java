package dev.ultreon.langgen.javascript.ts;

import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.stream.Collectors;

public class TsFinalClassBuilder extends TsClassBuilder {
    public TsFinalClassBuilder(Class<?> clazz) {
        super(clazz);
    }

    @Override
    public String getStubFormat() {
        return """
                %4$s
                
                /**
                 * This is a wrapper for the {%1$s} Java class.
                 * THIS CLASS IS GENERATED AND SHOULD NOT BE EDITED.
                 *
                 * THIS CLASS SHOULD NOT BE OVERRIDDEN AS IT'S FINAL IN JAVA.
                 *
                 * @final
                 */
                %5$sclass _%1$s {
                """;
    }
}
