package me.g1moon.demo;

import org.springframework.stereotype.Controller;

import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class SampleController {

    //리턴하는건 뷰의 이름 , 모델데이터를 받을 모델파라미터 설정
    //뷰는 리턴값으로 담고, 모델은 맵이라생각하고
    @GetMapping("/hello")
    public String hello(Model model) {
        model.addAttribute("name", "g1moon"); //key, value
        return "hello"; //뷰 이름 -> 즉 resource/templates/hello.html

    }

}
