package me.g1moon.springinit;

import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.stereotype.Component;

@Component
//@Order(1) #숫자 낮은게 먼저 쓰인다 -> 1이 가장 먼저 쓰임
public class SampleListenerRunner implements ApplicationRunner {
    @Override
    public void run(ApplicationArguments args) throws Exception {
        System.out.println("foo: " + args.containsOption("foo"));
        System.out.println("bar: " + args.containsOption("bar"));
        //foo: false
        //bar: true 항상 jvm옵션은 받지 못하고 ->

    }
}
