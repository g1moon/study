package me.g1moon.springinit;

import org.springframework.boot.ApplicationArguments;
import org.springframework.stereotype.Component;

//리스너가 아니라 그냥 아규먼트 찍어내는 컴포넌트
//@Component
public class SampleListenr{

    public SampleListenr(ApplicationArguments arguments) {
        System.out.println("foo:" + arguments.containsOption("foo"));
        System.out.println("bar:" + arguments.containsOption("bar"));
        //foo  : false
        //bar : true
        //->
    }
}
