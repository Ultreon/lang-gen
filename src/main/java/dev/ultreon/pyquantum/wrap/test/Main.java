package dev.ultreon.pyquantum.wrap.test;

import org.reflections.Reflections;
import org.reflections.scanners.Scanners;
import org.reflections.scanners.SubTypesScanner;
import org.reflections.util.ClasspathHelper;
import org.reflections.util.ConfigurationBuilder;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.net.URL;
import java.util.Set;

public class Main {
    private static final Logger LOGGER = LoggerFactory.getLogger(Main.class);

    public static void main(String[] args) {
        Reflections reflections = new Reflections(new ConfigurationBuilder()
            .setUrls(ClasspathHelper.forJavaClassPath())
            .setScanners(Scanners.SubTypes));

        Set<String> allClasses =
            reflections.getAll(Scanners.SubTypes);

        for (String clazz : allClasses) {
            if (clazz.startsWith("java."))
                LOGGER.error(clazz);
        }
    }
}