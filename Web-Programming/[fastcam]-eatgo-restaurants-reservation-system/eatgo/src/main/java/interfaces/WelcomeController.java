package interfaces;

import domain.Restaurant;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

@RestController
public class WelcomeController {

    @GetMapping("/")
    public String hello() {
        return "hello, world";
    }



}
