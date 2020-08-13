package me.g1moon.demospringmvc.user;

import org.springframework.web.bind.annotation.*;

@RestController
public class UserController {

    @GetMapping("/hello")
    public String hello() {
        return "hello";
    }

    //HttpMessageConverter
    //HTTP 요청 본문을 객체로 변경하거나, 객체를 http 응답 본문으로 변경할떄 사용
    //컨텐츠 타입이 제이슨이고, 본문도 제이슨이면 -> 제이슨으로 유저 타입의 객체를
    //객체자체로 내보낼 수 없음(http니까) -> 스트링만 리턴하면, 정수만 리턴하면 -> 스트링 컨버터
    //
//    @PostMapping("/user")
//    public @ResponseBody
//    User create(@RequestBody User user) {
//        return null;
//    }

    //User객체를 요청하면 ->
    @PostMapping("/users/create")
    public User create(@RequestBody User user){
        return user;
    }




}
