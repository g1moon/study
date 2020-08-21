package interfaces;

import domain.Restaurant;
import org.springframework.boot.SpringBootConfiguration;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

@RestController
@SpringBootConfiguration //추가해서 오류 해결 -> 스프링 부트의 설정을 나타내는 어노테이션,
//스프링의 @Configuration을 대체하며 -> 스프링 부트 전용 어노테이션 -> 테스트 어노테이션을
//사용할 때 계속 이 어노테이션을 찾기 떄문에 스프링부트에서는 필수 어노테이션
public class RestaurantController {

    @GetMapping("/restaurants") //리스트만들고, 객체만들고, 더하고, 리턴
    public List<Restaurant> list() {
        List<Restaurant> restaurants = new ArrayList<>();

        Restaurant restaurant = new Restaurant(1004L,"Bob zip", "Seoul");

        restaurants.add(restaurant);
        return restaurants;

    }
}
