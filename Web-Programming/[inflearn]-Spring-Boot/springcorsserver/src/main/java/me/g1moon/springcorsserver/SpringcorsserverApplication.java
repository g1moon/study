package me.g1moon.springcorsserver;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class SpringcorsserverApplication {

    //이 방법은 메서드 하나, 클래스 하나만 적용 가능한데
    //WebConfig(WebMvcConfiguration을 implement)해서 하면 -> 한번에 처리 가능
    @CrossOrigin(origins = "http://localhost:18080") //cross origin 추가
    @GetMapping("/hello")
    public String hello() {
        return "hello";
    }


    public static void main(String[] args) {
        SpringApplication.run(SpringcorsserverApplication.class, args);
    }

}
