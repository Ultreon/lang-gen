package dev.ultreon.pyquantum.wrap;

import java.io.IOException;
import java.io.StringWriter;
import java.lang.reflect.Modifier;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.jar.JarEntry;
import java.util.jar.JarInputStream;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.stream.Collectors;

public class JarWrapperBuilder extends WrapperBuilder {
    private final JarInputStream jar;
    private final Logger logger = Logger.getLogger("JarStubBuilder");
    private final Map<String, StringWriter> pyClassBuilders = new HashMap<>();
    private final Map<String, List<String>> pyImports = new HashMap<>();
    private final Set<Class<?>> classes = new HashSet<>();
    private final Set<String> packageNames = new HashSet<>();

    public JarWrapperBuilder(Path input) throws IOException {
        this.jar = new JarInputStream(Files.newInputStream(input));
    }

    @Override
    public void build(Path output) throws IOException {
        if (!Files.exists(output)) {
            Files.createDirectories(output);
        }

        if (!Files.isDirectory(output)) {
            throw new RuntimeException("Output path is not a directory: " + output);
        }

        JarEntry entry;
        while ((entry = jar.getNextJarEntry()) != null) {
            if (!entry.isDirectory() && entry.getName().endsWith(".class")) {
                try {
                    if (entry.getName().startsWith("META-INF")
                        || entry.getName().substring(0, entry.getName().length() - 6).contains(".")
                        || entry.getName().contains("module-info")
                        || entry.getName().contains("-")
                        || entry.getName().contains("package-info")) {
                        continue;
                    }
                    this.processEntry(entry);
                } catch (ClassNotFoundException | NoClassDefFoundError e) {
                    logger.log(Level.SEVERE, e.getMessage(), e);
                }
            }
        }

        for (Class<?> clazz : classes.stream().sorted((o1, o2) -> {
            Class<?> superclass = o1.getSuperclass();
            Class<?>[] interfaces = o1.getInterfaces();

            Class<?> otherSuperclass = o2.getSuperclass();
            Class<?>[] otherInterfaces = o2.getInterfaces();

            if (superclass == o2) {
                return -1;
            } else if (otherSuperclass == o1) {
                return 1;
            }

            for (Class<?> anInterface : interfaces) {
                if (anInterface == otherSuperclass) {
                    return -1;
                }
            }

            for (Class<?> otherInterface : otherInterfaces) {
                if (otherInterface == superclass) {
                    return 1;
                }
            }

            return 0;
        }).toList()) {
            String transformedName = transformName(clazz);
            StringWriter sw1 = new StringWriter();
            StringWriter sw = this.pyClassBuilders.computeIfAbsent(transformedName, k -> sw1);

            try {
                List<String> build = new PythonFinalClassBuilder(clazz).build(sw1);

                this.pyImports.computeIfAbsent(transformedName, k -> new ArrayList<>()).addAll(build);
            } catch (Throwable e) {
                logger.log(Level.SEVERE, e.getMessage(), e);
            }

            sw.append("""
                    \s
                    \s
                    \s
                    # CLASS: %s
                    """.formatted(clazz.getName())).append(sw1.toString().trim());
        }

        for (Map.Entry<String, StringWriter> e : pyClassBuilders.entrySet()) {
            Path path = output.resolve(e.getKey().replace('.', '/') + ".py");
            String value = pyClassBuilders.get(e.getKey()).toString();
            List<String> coll = pyImports.get(e.getKey());
            if (coll == null) {
                logger.warning(e.getKey() + " has no imports");
                coll = new ArrayList<>();
            }
            Set<String> strings = Set.copyOf(coll);

            AtomicBoolean importOnce = new AtomicBoolean(false);
            String imports = (strings).stream().map(code -> {
                if (code.startsWith("#py_import\n")) {
                    String substring = code.substring("#pyimport\n".length()).replace("\n", "").replace("\r", "");
                    String s1 = null;
                    String s;
                    if (substring.startsWith("from ")) {
                        String replace = substring.replace("from ", "");
                        s1 = replace.split(" import ")[0];
                        s = replace.split(" import ")[1];
                        s1 += "." + s;
                    } else {
                        String replace = substring.replace("import ", "");
                        s1 = replace;
                        s = replace;
                    }
                    s = s.substring(s.lastIndexOf(".") + 1);
                    code = """
                            try:
                                %1$s
                            except ImportError:
                                %3$s = _import_once("%2$s")
                            """.formatted(
                            substring.replace("\n", "").replace("\r", ""),
                            s1,
                            s.replace(".", "_")
                    );

                    importOnce.set(true);
                }

                return code;
            }).collect(Collectors.joining("\n"));

            if (importOnce.get()) {
                imports = """
                        from pyquantum_helper import import_once as _import_once
                        """ + imports;
            }

            Files.createDirectories(path.getParent());
            Files.writeString(path, """
                from __future__ import annotations
                from overload import overload
                """ + imports + "\n" + value.toString());
        }
    }

    private void processEntry(JarEntry entry) throws ClassNotFoundException {
        ClassLoader classLoader = Thread.currentThread().getContextClassLoader();
        Class<?> clazz = Class.forName(entry.getName().substring(0, entry.getName().length() - 6).replace('/', '.'), false, classLoader);

        if (clazz.isSynthetic()) {
            return;
        } else if (Modifier.isPrivate(clazz.getModifiers())) {
            return;
        } else if (!Modifier.isPublic(clazz.getModifiers()) && !Modifier.isProtected(clazz.getModifiers())) {
            return;
        }

        this.packageNames.add(clazz.getPackageName());

        this.classes.add(clazz);
    }

    private String transformName(Class<?> entry) {
        String packageName = entry.getPackageName();
        String name = packageName;
        if (name.startsWith("dev.ultreon.quantum."))
            name = "pyquantum." + name.substring("dev.ultreon.quantum.".length());
        else if (name.startsWith("dev.ultreon.xeox.loader."))
            name = "pyxeox." + name.substring("dev.ultreon.xeox.loader.".length());
        else if (name.startsWith("dev.ultreon.libs."))
            name = "pycorelibs." + name.substring("dev.ultreon.libs.".length());
        else if (name.startsWith("dev.ultreon.data."))
            name = "pydata." + name.substring("dev.ultreon.data.".length());
        else if (name.startsWith("dev.ultreon.ubo."))
            name = "pyubo." + name.substring("dev.ultreon.ubo.".length());
        else if (name.startsWith("com.badlogic.gdx."))
            name = "pygdx." + name.substring("com.badlogic.gdx.".length());
        else if (name.startsWith("java.lang."))
            name = "pyjlang." + name.substring("java.lang.".length());
        else if (name.startsWith("java.util."))
            name = "pyjutil." + name.substring("java.util.".length());
        else if (name.startsWith("java.io."))
            name = "pyjio." + name.substring("java.io.".length());
        else if (name.startsWith("java.nio."))
            name = "pyjnio." + name.substring("java.nio.".length());
        else if (name.startsWith("java.awt."))
            name = "pyjawt." + name.substring("java.awt.".length());
        else if (name.startsWith("java.net."))
            name = "pyjnet." + name.substring("java.net.".length());
        else if (name.startsWith("java.security."))
            name = "pyjsec." + name.substring("java.security.".length());
        else if (name.startsWith("java.text."))
            name = "pyjtext." + name.substring("java.text.".length());
        else if (name.startsWith("java.math."))
            name = "pyjmath." + name.substring("java.math.".length());
        else if (name.startsWith("java.time."))
            name = "pyjtime." + name.substring("java.time.".length());
        else if (name.startsWith("java.sql."))
            name = "pyjsql." + name.substring("java.sql.".length());
        else if (name.startsWith("java.util.concurrent."))
            name = "pyjconc." + name.substring("java.util.concurrent.".length());
        else if (name.startsWith("java.util.logging."))
            name = "pyjlog." + name.substring("java.util.logging.".length());
        else if (name.startsWith("java.util.zip."))
            name = "pyjzip." + name.substring("java.util.zip.".length());
        else if (name.startsWith("java.lang.reflect."))
            name = "pyjreflect." + name.substring("java.lang.reflect.".length());
        else if (name.startsWith("java.util.regex."))
            name = "pyjregex." + name.substring("java.util.regex.".length());
        else if (name.startsWith("java.util.function."))
            name = "pyjfunc." + name.substring("java.util.function.".length());
        else if (name.startsWith("java.util.stream."))
            name = "pyjstream." + name.substring("java.util.stream.".length());
        else if (name.startsWith("org.apache.logging.log4j."))
            name = "log4py." + name.substring("org.apache.logging.log4j.".length());
        else if (name.startsWith("org.apache.commons."))
            name = "pyapache." + name.substring("org.apache.commons.".length());
        else if (name.startsWith("org.lwjgl.glfw."))
            name = "pyglfw." + name.substring("org.lwjgl.glfw.".length());
        else if (name.startsWith("org.lwjgl.opengl."))
            name = "pyopengl." + name.substring("org.lwjgl.opengl.".length());
        else if (name.startsWith("org.lwjgl.egl."))
            name = "pyegl." + name.substring("org.lwjgl.egl.".length());
        else if (name.startsWith("org.lwjgl.system."))
            name = "pyglsystem." + name.substring("org.lwjgl.system.".length());
        else if (name.startsWith("org.lwjgl.vulkan."))
            name = "pyvulkan." + name.substring("org.lwjgl.vulkan.".length());
        else if (name.startsWith("org.lwjgl.assimp."))
            name = "pyassimp." + name.substring("org.lwjgl.assimp.".length());
        else if (name.startsWith("org.lwjgl."))
            name = "pygl." + name.substring("org.lwjgl.".length());
        else if (name.startsWith("com.google.code.gson."))
            name = "pygson." + name.substring("com.google.code.gson.".length());
        else if (name.startsWith("com.google.protobuf."))
            name = "pyprotobuf." + name.substring("com.google.protobuf.".length());
        else if (name.startsWith("com.google.gson."))
            name = "pygson." + name.substring("com.google.gson.".length());
        else if (name.startsWith("com.google.common."))
            name = "pygcommon." + name.substring("com.google.common.".length());
        else if (name.startsWith("com.google."))
            name = "pygoogle." + name.substring("com.google.".length());
        else if (name.startsWith("com.badlogic.gdx."))
            name = "pygdx." + name.substring("com.badlogic.gdx.".length());
        else if (name.startsWith("com.badlogic."))
            name = "pygdx." + name.substring("com.badlogic.".length());
        else if (name.startsWith("space.earlygrey.shapedrawer."))
            name = "pyshapedrawer." + name.substring("space.earlygrey.shapedrawer.".length());
        else if (name.startsWith("org.slf4j."))
            name = "slf4py." + name.substring("org.slf4j.".length());

        name = switch (name) {
            case "org.apache.logging.log4j" -> "log4py";
            case "org.apache.commons" -> "pyapache";
            case "org.lwjgl.opengl" -> "pyopengl";
            case "org.lwjgl.glfw" -> "pyglfw";
            case "org.lwjgl.opencl" -> "pyopencl";
            case "org.lwjgl.stb" -> "pyglstb";
            case "org.lwjgl.vulkan" -> "pyvulkan";
            case "org.lwjgl.egl" -> "pyegl";
            case "org.lwjgl.system" -> "pyglsystem";
            case "org.lwjgl" -> "pygl";
            case "com.google.gson" -> "pygson";
            case "com.google.protobuf" -> "pyprotobuf";
            case "com.google.common.collect" -> "pygcollect";
            case "com.google.common" -> "pygcommon";
            case "java" -> "java";
            case "dev.ultreon.quantum" -> "pyquantum";
            case "dev.ultreon.libs" -> "pycorelibs";
            case "dev.ultreon.data" -> "pydata";
            case "dev.ultreon.ubo" -> "pyubo";
            case "dev.ultreon.xeox.loader" -> "pyxeox";
            case "com.badlogic.gdx" -> "pygdx";
            case "com.badlogic" -> "pygdx";
            case "space.earlygrey.shapedrawer" -> "pyshapedrawer";
            case "org.slf4j" -> "slf4py";
            default -> name;
        };

        int endIndex = name.lastIndexOf('.');
        String parentModule = name.substring(0, endIndex == -1 ? name.length() : endIndex);
        if (packageNames.stream().anyMatch(p -> {
            if (!p.contains("."))
                return true;

            int endIndex2 = p.lastIndexOf('.');
            if (!p.contains("."))
                return true;
            p = p.substring(0, endIndex2 == -1 ? p.length() : endIndex2);
            return p.equals(packageName);
        })) {
            return name + ".__init__";
        }

        return name;
    }
}
