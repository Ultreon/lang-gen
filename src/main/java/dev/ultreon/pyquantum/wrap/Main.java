package dev.ultreon.pyquantum.wrap;

import org.intellij.lang.annotations.Language;

import java.io.IOException;
import java.net.URISyntaxException;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Main {
    Logger logger = Logger.getLogger("StubBuilder");

    private Main() {

    }

    private void init() {
        try {
            writeWrapper("dev.ultreon.quantum.CommonConstants");
            writeWrapper("dev.ultreon.quantum.client.QuantumClient");
            writeWrapper("dev.ultreon.quantum.desktop.DesktopLauncher");
            writeWrapper("dev.ultreon.ubo.DataIo");
            writeWrapper("dev.ultreon.libs.events.v1.Main");
            writeWrapper("dev.ultreon.libs.collections.v0.util.ArrayUtils");
            writeWrapper("dev.ultreon.libs.commons.v0.Logger");
            writeWrapper("dev.ultreon.libs.crash.v0.ApplicationCrash");
            writeWrapper("dev.ultreon.libs.datetime.v0.Date");
            writeWrapper("dev.ultreon.libs.functions.v0.Float2FloatFunction");
            writeWrapper("dev.ultreon.libs.registries.v0.Registry");
            writeWrapper("dev.ultreon.libs.resources.v0.Resource");
            writeWrapper("dev.ultreon.libs.text.v0.LiteralText");
            writeWrapper("dev.ultreon.libs.translations.v0.Translation");
            writeWrapper("dev.ultreon.libs.translations.v1.Translation");
            writeWrapper("com.google.common.collect.ImmutableMap");
            writeWrapper("com.google.gson.JsonObject");
            writeWrapper("org.apache.commons.lang3.StringUtils");
            writeWrapper("org.apache.commons.collections4.CollectionUtils");
            writeWrapper("org.apache.logging.log4j.LogManager");
            writeWrapper("org.slf4j.Logger");
            writeWrapper("org.lwjgl.BufferUtils");
            writeWrapper("org.lwjgl.glfw.GLFW");
            writeWrapper("org.lwjgl.stb.STBImage");
            writeWrapper("org.lwjgl.system.MemoryUtil");
            writeWrapper("com.badlogic.gdx.Gdx");
            writeWrapper("com.badlogic.gdx.ai.GdxAI");
            writeWrapper("com.badlogic.gdx.backends.headless.HeadlessApplication");
            writeWrapper("com.badlogic.gdx.video.VideoDecoder");
            writeWrapper("com.badlogic.gdx.physics.box2d.Box2D");
            writeWrapper("com.badlogic.gdx.controllers.Controllers");
            writeWrapper("com.badlogic.gdx.graphics.g2d.freetype.FreeTypeFontGenerator");
            writeWrapper("com.badlogic.gdx.utils.SharedLibraryLoader");
            writeWrapper("box2dLight.Light");
            writeWrapper("space.earlygrey.shapedrawer.ShapeDrawer");
            writeWrapper("com.badlogic.gdx.tools.texturepacker.TexturePacker");
            writeWrapper("com.badlogic.ashley.core.Engine");
//            writeWrapper("dev.ultreon.gameprovider.quantum.QuantumVxlGameProvider");
//            writeWrapper("net.fabricmc.api.EnvType");
        } catch (Exception e) {
            logger.log(Level.SEVERE, e.getMessage(), e);
            System.exit(1);
        }
    }

    private void writeWrapper(@Language("jvm-class-name") String className) throws ClassNotFoundException, URISyntaxException, IOException {
        Class<?> clazz = Class.forName(className, false, Main.class.getClassLoader());
        URL location = clazz.getProtectionDomain().getCodeSource().getLocation();
        Path path = Path.of(location.toURI());

        if (!Files.exists(path)) {
            logger.info("File not found: " + path);
            throw new RuntimeException("File not found: " + path);
        }

        WrapperBuilder.buildPath(path);
    }

    public static void main(String[] args) {
        Main main = new Main();
        main.init();
    }
}
