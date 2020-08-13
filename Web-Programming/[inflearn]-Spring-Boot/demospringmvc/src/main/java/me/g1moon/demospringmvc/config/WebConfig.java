package me.g1moon.demospringmvc.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

//스프링부트가 제공하는 리소스 헨들러 기능을 유지하면서 -> 커스텀한 방법 추가 ------//
//http://localhost:8080/m/helloo.html
@Configuration
public class WebConfig implements WebMvcConfigurer {
    @Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {
        registry.addResourceHandler("/m/**") //m아래 이러한 요청이 오면
                                   //!주의 반드시 m/ 이렇게 끝나야해 //
                .addResourceLocations("classpath:/m/") //여기서 처리를 하겠따 해
                .setCachePeriod(20); //20초 //캐시 컨트롤 직접해줘야

    }
}
//--------------------------------------------------------------------