package me.g1moon.springinit;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.stereotype.Component;

@Component
public class SampleRunner implements ApplicationRunner {
    @Value("${g1moon.name}")
    private String name;

    @Value("${g1moon.age}")
    private int age;

    @Override
    public void run(ApplicationArguments args) throws Exception {
        System.out.println("==================");
        System.out.println(name);
        System.out.println("===================");


    }
}
