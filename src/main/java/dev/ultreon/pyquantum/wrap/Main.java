package dev.ultreon.pyquantum.wrap;

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
            writeWrapper();
        } catch (Exception e) {
            logger.log(Level.SEVERE, e.getMessage(), e);
            System.exit(1);
        }
    }

    private void writeWrapper() throws ClassNotFoundException, URISyntaxException, IOException {
        Wrapper.buildPath();
    }

    public static void main(String[] args) {
        Main main = new Main();
        main.init();
    }
}
