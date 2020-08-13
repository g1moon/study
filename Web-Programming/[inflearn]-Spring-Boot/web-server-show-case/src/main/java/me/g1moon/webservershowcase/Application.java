package me.g1moon.webservershowcase;

import org.apache.catalina.connector.Connector;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.web.embedded.tomcat.TomcatServletWebServerFactory;
import org.springframework.boot.web.servlet.server.ServletWebServerFactory;
import org.springframework.context.annotation.Bean;
import org.springframework.web.bind.annotation.GetMapping;

@SpringBootApplication
public class Application {

    @GetMapping("/hello")
    public String hello() {
        return "hello spring";
    }

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);

    }



}
