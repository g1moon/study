package me.g1moon.springcorsserver;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfig implements WebMvcConfigurer {

    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**")
//        registry.addMapping("/hello");
                .allowedOrigins("http://localhost:18080");
        //현재 여기 포트는 8080인데 18080에서 접근을 가능하게 하겠다.
        //hello만 18080에서 접근 가능하게 하겠다.
        // 18080에 index.html에 제이쿼리 이용해서 ->
        //8080/hello에서 응답 받아오면 -> hello출력
        //  --->아니면 fail출력하게 작업했음.
    }
}
