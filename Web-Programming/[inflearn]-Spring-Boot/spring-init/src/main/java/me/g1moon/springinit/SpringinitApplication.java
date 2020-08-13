package me.g1moon.springinit;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.WebApplicationType;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class SpringinitApplication {
    public static void main(String[] args) {
        //1
//        SpringApplication.run(SpringinitApplication.class, args);

        //2
        SpringApplication app = new SpringApplication(SpringinitApplication.class);
        app.setWebApplicationType(WebApplicationType.NONE);
        app.run(args);

    }
}
