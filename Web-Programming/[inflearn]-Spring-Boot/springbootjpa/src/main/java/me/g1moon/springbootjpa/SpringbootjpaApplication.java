package me.g1moon.springbootjpa;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

//1. 데이터베이스가 없음 - h2를 테스트로 스콮줬음
// -> 그래서 postgresql 의존성 추가 
@SpringBootApplication
public class SpringbootjpaApplication {

    public static void main(String[] args) {
        SpringApplication.run(SpringbootjpaApplication.class, args);
    }

}
