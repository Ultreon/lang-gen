package dev.ultreon.langgen.api;

import org.apache.logging.log4j.Logger;
import org.jetbrains.annotations.Nullable;
import org.reflections.Reflections;
import org.reflections.scanners.Scanners;
import org.reflections.util.ConfigurationBuilder;

import javax.swing.*;
import java.awt.*;
import java.io.File;
import java.io.IOError;
import java.io.IOException;
import java.lang.reflect.Modifier;
import java.net.MalformedURLException;
import java.net.URL;
import java.nio.file.*;
import java.nio.file.attribute.BasicFileAttributes;
import java.util.*;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicInteger;

public abstract class ClasspathBuilder extends ClasspathWrapper implements NameTransformer {
    private final List<Class<?>> classes = new ArrayList<>();
    private final boolean ignorePrivate;
    private @Nullable JLabel label = null;
    private @Nullable JProgressBar progressBar = null;

    static JFrame frame = new JFrame();
    static JPanel contentPane = new JPanel();

    ExecutorService executor = Executors.newFixedThreadPool(8);

    static {
        JPanel windowPane = new JPanel();
        windowPane.setLayout(new GridBagLayout());
        GridBagConstraints c = new GridBagConstraints();

        // Center panel
        c.gridx = 1;
        c.gridy = 0;
        c.gridwidth = 1;
        c.gridheight = 1;
        c.weightx = 1;
        c.weighty = 1;
        c.fill = GridBagConstraints.BOTH;
        c.anchor = GridBagConstraints.NORTHWEST;
        windowPane.add(contentPane, c);

        JSeparator separator = new JSeparator();
        c.gridx = 0;
        c.gridy = 1;
        c.gridwidth = 2;
        c.gridheight = 1;
        c.weightx = 1;
        c.weighty = 0;
        c.fill = GridBagConstraints.HORIZONTAL;
        c.anchor = GridBagConstraints.SOUTHWEST;
        windowPane.add(separator);

        // Bottom panel
        JPanel bottomPanel = new JPanel();
        bottomPanel.setLayout(new FlowLayout(FlowLayout.RIGHT, 10, 10));
        c.gridx = 0;
        c.gridy = 2;
        c.gridwidth = 2;
        c.gridheight = 1;
        c.weightx = 1;
        c.weighty = 0;
        c.fill = GridBagConstraints.HORIZONTAL;
        c.anchor = GridBagConstraints.SOUTHWEST;
        windowPane.add(bottomPanel, c);

        // Close button
        JButton closeButton = new JButton("Close");
        closeButton.addActionListener(e -> frame.dispose());
        bottomPanel.add(closeButton);

        contentPane.setLayout(new BoxLayout(contentPane, BoxLayout.Y_AXIS));
        frame.setContentPane(windowPane);
    }

    protected ClasspathBuilder(boolean ignorePrivate) {
        this.ignorePrivate = ignorePrivate;

        SwingUtilities.invokeLater(() -> {
            label = new JLabel("Generating...");
            progressBar = new JProgressBar();
            contentPane.add(label);
            contentPane.add(progressBar);
            frame.pack();
            frame.setVisible(true);
        });
    }

    @Override
    protected final void doBuild(Path outputDir)  {
        createOutputDir(outputDir);

        if (!Files.isDirectory(outputDir))
            throw new RuntimeException("Output path is not a directory: " + outputDir);

        List<URL> urls = new ArrayList<>();

        // Scan .jmod files in the JVM
        Path javaHome = Paths.get(System.getProperty("java.home"));
        Path jmodsDir = javaHome.resolve("jmods");
        if (Files.exists(jmodsDir)) visitJMods(jmodsDir, urls);

        Path libsDir = Paths.get("libs");
        if (Files.exists(libsDir)) visitLibs(libsDir, urls);

        String classPath = System.getProperty("java.class.path");
        if (classPath != null) visitClasspath(classPath, urls);

        Reflections reflections = new Reflections(new ConfigurationBuilder()
                .setUrls(Set.copyOf(urls))
                .setScanners(Scanners.SubTypes.filterResultsBy((arg0) -> true)));

        Set<String> allClasses = new HashSet<>(reflections.getAll(Scanners.SubTypes));

        if (!allClasses.contains("org.reflections.Reflections"))
            throw new NoClassDefFoundError("org.reflections.Reflections");
        if (!allClasses.contains("java.util.UUID"))
            throw new NoClassDefFoundError("java.util.UUID");

        processEntries(allClasses);
        processClasses(outputDir);
    }

    private static void createOutputDir(Path outputDir) {
        if (!Files.exists(outputDir)) {
            try {
                Files.createDirectories(outputDir);
            } catch (IOException e) {
                throw new IOError(e);
            }
        }
    }

    private void processClasses(Path output) {
        int total = classes.size();
        AtomicInteger count = new AtomicInteger();
        for (Class<?> clazz : classes) {
            CompletableFuture.runAsync(() -> {
                if (label != null && progressBar != null) {
                    SwingUtilities.invokeLater(() -> {
                        label.setText("Processing " + (100 * count.get() / total) + "% (" + count.get() + "/" + total + ") " + clazz.getSimpleName());
                        progressBar.setMaximum(total);
                        progressBar.setValue(count.incrementAndGet());
                    });
                }
                if (!Modifier.isPublic(clazz.getModifiers()) && !Modifier.isProtected(clazz.getModifiers())) return;
                if ((clazz.getModifiers() & 0x0000100) != 0) return;

                try {
                    StringBuilder sw = new StringBuilder();
                    String result = this.visitClass(clazz, sw);
                    if (result == null) return;
                    this.writeFile(output, clazz.getName(), result);
                } catch (GeneratorException e) {
                    throw e;
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }, executor);
        }
    }

    private void processEntries(Set<String> allClasses) {
        for (String className : allClasses) {
            if (label != null && progressBar != null) {
                SwingUtilities.invokeLater(() -> {
                    label.setText("Pre-processing " + className);
                    progressBar.setMaximum(allClasses.size());
                    progressBar.setValue(progressBar.getValue() + 1);
                });
            }

            try {
                processEntry(className);
            } catch (ClassNotFoundException | NoClassDefFoundError e) {
                getLogger().warn("Class not found: {}", className);
            } catch (Exception e) {
                getLogger().error("Failed to process class: {}", className, e);
            }
        }
    }

    private static void visitClasspath(String classPath, List<URL> urls) {
        for (String path : classPath.split(File.pathSeparator)) {
            if (!path.endsWith(".jar") && !path.endsWith(".jmod") && !path.endsWith(".zip")) continue;
            try {
                urls.add(new File(path).toURI().toURL());
            } catch (MalformedURLException e) {
                throw new IOError(e);
            }
        }
    }

    private static void visitLibs(Path libsDir, List<URL> urls) {
        try {
            Files.walkFileTree(libsDir, new SimpleFileVisitor<>() {
                @Override
                public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) throws IOException {
                    if (file.getFileName().toString().endsWith(".jar")) {
                        urls.add(file.toUri().toURL());
                    }

                    return FileVisitResult.CONTINUE;
                }
            });
        } catch (IOException e) {
            throw new IOError(e);
        }
    }

    private static void visitJMods(Path root, List<URL> urls) {
        try {
            Files.walkFileTree(root, new SimpleFileVisitor<>() {
                @Override
                public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) throws IOException {
                    if (file.getFileName().toString().endsWith(".jmod")) {
                        try (FileSystem fs = FileSystems.newFileSystem(file, Collections.emptyMap())) {
                            urls.add(fs.getPath("/").toUri().toURL());
                        }
                    }

                    return FileVisitResult.CONTINUE;
                }
            });
        } catch (IOException e) {
            throw new IOError(e);
        }
    }

    protected abstract void writeFile(Path output, String className, String result) throws IOException;

    protected abstract @Nullable String visitClass(Class<?> clazz, StringBuilder classBuilders);

    protected abstract Logger getLogger();

    private void processEntry(String className) throws ClassNotFoundException {
        ClassLoader classLoader = Thread.currentThread().getContextClassLoader();
        Class<?> clazz = Class.forName(className, false, classLoader);

        if (this.ignorePrivate && !Modifier.isPublic(clazz.getModifiers()) && !Modifier.isProtected(clazz.getModifiers())) {
            return;
        }

        this.classes.add(clazz);
    }
}
