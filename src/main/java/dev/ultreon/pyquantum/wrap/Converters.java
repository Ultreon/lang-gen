package dev.ultreon.pyquantum.wrap;

import groovyjarjarantlr4.v4.misc.OrderedHashMap;
import org.jetbrains.annotations.Nullable;

import java.util.HashMap;
import java.util.Map;

/**
 * Class for converting between package names.
 *
 * @author XyperCode
 * @since 1.0
 */
public class Converters {
    private static final Map<String, String> CONVERTERS = new OrderedHashMap<>();

    private Converters() {

    }

    /**
     * Gets the name of the package name to convert to.
     *
     * @param name the name of the package
     * @return the name of the package to convert to
     */
    public static @Nullable String convert(String name) {
        for (Map.Entry<String, String> entry : CONVERTERS.entrySet()) {
            if (name.startsWith(entry.getKey() + ".")) {
                String value = entry.getValue();
                return value + name.substring(entry.getKey().length());
            }
        }
        return null;
    }

    /**
     * Register a converter for package names.
     *
     * @param from the package name to convert from
     * @param to the package name to convert to
     */
    public static void register(String from, String to) {
        CONVERTERS.put(from, to);
    }

    static {
        register("org.lwjgl.egl", "egl");
        register("org.lwjgl.glfw", "glfw");
        register("org.lwjgl.opencl", "opencl");
        register("org.lwjgl.openal", "openal");
        register("org.lwjgl.opengl", "opengl");
        register("org.lwjgl.nanovg", "nanovg");
        register("org.lwjgl.nuklear", "nuklear");
        register("org.lwjgl.nanovg", "nanovg");
        register("org.lwjgl.stb", "glstb");
        register("org.lwjgl.util", "glutil");
        register("org.lwjgl.vulkan", "vulkan");
        register("org.lwjgl.assimp", "assimp");
        register("org.lwjgl", "gl");

        register("com.google.gson", "gson");
        register("com.google.protobuf", "gprotobuf");
        register("com.google.common.collect", "gcollect");
        register("com.google.common", "gcommon");

        register("space.earlygrey.shapedrawer", "gdx_shapedrawer");

        register("org.slf4j", "slf4py");

        register("com.badlogic.gdx", "libgdx");
        register("com.badlogic.ashley", "libgdx.ashley");

        register("jdk.jshell", "jshell");
        register("jdk.vm", "jvm");
        register("jdk.jfr", "jfr");
        register("jdk.internal", "jdk_internal");
        register("joptsimple", "optionsimple");
        register("libnoiseforjava", "libnoise");
        register("jline", "jline");
        register("javassist", "pyassist");
        register("javazoom", "pyzoom");
        register("net.java.games.input", "pyinput");
        register("net.java.games", "javagames");
        register("net.mgsx.gltf", "gdx_gltf");
        register("net.miginfoccom", "miginfoccom");
        register("net.java.jogl", "jogl");
        register("net.java.jinput", "jinput");
        register("org.apache.groovy", "groovy._impl");
        register("org.apache.logging.slf4j", "log4py.compat.slf4py");
        register("org.apache.logging.log4j", "log4py");
        register("org.bouncycastle", "bouncy");

        register("org.checkerframework", "pychecker");
        register("org.codehaus.groovy", "pygroovy._codehaus");
        register("org.graalvm", "pygraalvm");
        register("org.intellij", "intellij");
        register("org.jetbrains", "jetbrains");
        register("org.json", "pyjson");
        register("org.jspecify", "jspecify");
        register("org.mozilla.classfile", "moz_classfile");
        register("org.mozilla.javascript", "js");
        register("org.objectweb.asm", "jasm");
        register("org.oxbow", "oxbow");
        register("org.reactivestreams", "pyreactive");
        register("org.reflections", "reflections");
        register("org.spongepowered.asm.mixin", "mixin");
        register("org.spongepowered.asm", "sponge_asm");
        register("org.spongepowered", "sponge");
        register("org.tukaani.xz", "pyxz");
        register("org.w3c", "w3c");
        register("org.xml", "pyxml");

        register("org.slf4j", "slf4py");

        register("jna", "jna");

        register("java.applet", "japplet");
        register("java.beans", "jbeans");
        register("java.lang", "jlang");
        register("java.util", "jutil");
        register("java.io", "jio");
        register("java.nio", "jnio");
        register("java.awt", "jawt");
        register("java.net", "jnet");
        register("java.security", "jsec");
        register("java.text", "jtext");
        register("java.time", "jtime");
        register("java.managment", "jman");
        register("java.math", "jmath");
        register("java.sql", "jsql");
        register("javax.xml", "jxml");
        register("javax.imageio", "jximageio");
        register("javax.sound", "jxsound");
        register("javax.crypto", "jxcrypto");
        register("javax.net", "jxnet");

        register("kotlin", "kotlin");
        register("kotlinx", "kotlinx");

        register("org.joml", "joml");

        register("org.apache.commons", "pycommons");
        register("org.apache.logging.log4j", "log4py");

        register("dev.ultreon.libs", "corelibs");
        register("dev.ultreon.data", "ultreon_data");
        register("dev.ultreon.ubo", "ubo");
        register("dev.ultreon.xeox.loader", "xeox");
        register("dev.ultreon.pyquantum", "pyquantum._internal");
        register("dev.ultreon.quantum", "pyquantum");

        register("net.fabricmc.api", "fabric_api");
        register("net.fabricmc.impl", "fabric_impl");
        register("net.fabricmc.loader", "fabric_loader");
        register("net.fabricmc", "fabricmc");

        register("net.minecraft", "minecraft");

        register("com.mojang.datafixers", "mojang.datafixers");
        register("com.mojang.brigadier", "brigadier");
        register("com.mojang.text2speech", "mojang.text2speech");
        register("com.mojang.authlib", "mojang.authlib");
        register("com.mojang.logging", "mojang.logging");

        register("com.ultreon", "ultreon._internal");
        register("dev.ultreon.pyquantum.wrap", "pyquantum.wrap");

        register("scala", "scalapy");

        register("clojure", "clojure");

        register("imgui", "imgui");

        register("groovy", "groovy");
        register("groovyjarjarantlr", "groovy._antlr");
        register("groovyjarjarantlr4", "groovy._antlr4");
        register("groovyjarjarasm", "groovy._asm");
        register("groovyjarjarpicocli", "groovy._picocli");

        register("junit", "junit");

        register("io.javalin", "pylin");

        register("io.github.classgraph", "classgraph");

        register("it.unimi.dsi.fastutil", "fastutil");

        register("com.crashinvaders.jfx", "pyfx");

        register("com.flowpowered.noise", "flownoise");

        register("com.formdev.flatlaf", "flatlaf");

        register("com.jcraft.jorbis", "pyorbis");
        register("com.jcraft.jzlib", "pyzlib");

        register("com.oracle.graal", "graal");
        register("com.oracle.svm", "svm");
        register("com.oracle.truffle", "truffle");

        register("com.raylabz.opensimplex", "opensimplex");

        register("com.studiohartman.jamepad", "jamepad");

        register("com.sun.jna", "native._jna");
        register("sun.jna.platform", "native");
        register("sun.jna", "native._internal");
        register("sun.misc", "jmisc._impl");
        register("sun.nio", "jnio._impl");
        register("sun.security", "jsec._impl");
        register("sun.util", "jutil._impl");
        register("sun.awt", "jawt._impl");
        register("sun.net", "jnet._impl");
        register("sun.text", "jtext._impl");
        register("sun.management", "jman._impl");
        register("sun.math", "jmath._impl");
        register("sun.sql", "jsql._impl");
        register("sun.xml", "jxml._impl");
        register("sun.imageio", "jximageio._impl");
        register("sun.sound", "jxsound._impl");
        register("sun.crypto", "jxcrypto._impl");

        register("com.jme3", "jme3");

        register("io.netty", "netty");

        register("io.github.ultreon.data", "ultreon_data");
        register("io.github.ultreon.ubo", "ubo");
        register("io.github.ultreon.xeox", "xeox");
        register("io.github.ultreon.corelibs", "corelibs");
        register("io.github.ultreon.libs", "libs");
        register("io.github.xypercode.mods", "xyper_mods");
        register("io.github.ultreon.pyquantum", "pyquantum._old");
        register("dev.ultreon.gameprovider", "pyquantum._gameprovider");
        register("de.articdive.jnoise", "pynoise");
        register("de.articdive.marhali", "marhali");

        register("org.owasp.encoder", "pyowasp");
    }
}
