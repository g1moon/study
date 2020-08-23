package interfaces;

import domain.MenuItem;
import domain.Restaurant;
import domain.RestaurantRepositoryImpl;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringBootConfiguration;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

@RestController
@SpringBootConfiguration //추가해서 오류 해결 -> 스프링 부트의 설정을 나타내는 어노테이션,
//스프링의 @Configuration을 대체하며 -> 스프링 부트 전용 어노테이션 -> 테스트 어노테이션을
//사용할 때 계속 이 어노테이션을 찾기 떄문에 스프링부트에서는 필수 어노테이션
public class RestaurantController {
    //객체를 직접 만들어주지 않고 아래처럼----------------------------
    //    private RestaurantRepository repository = new RestaurantRepository(); //repository필드를 만들어주면서 -> 식당레포객체를만들
    @Autowired
    private RestaurantRepositoryImpl restaurantsRepository; //구현체로 받아옴
    //---------------------------------------------

    @GetMapping("/restaurants") //리스트만들고, 객체만들고, 더하고, 리턴
    public List<Restaurant> list() {
//        List<Restaurant> restaurants = new ArrayList<>(); //리스트 만들어주고
//
////        restaurants.add(new Restaurant(1004L, "Bob zip", "Seoul"));
////        restaurants.add(new Restaurant(2020L,"Cyber food", "Seoul"));

        List<Restaurant> restaurants = restaurantsRepository.findAll();

        return restaurants; //리스트를 리턴
    }
    //////////////

    ///////////////

    @GetMapping("/restaurants/{id}")
    public Restaurant detail(@PathVariable("id") Long id) {
//        List<Restaurant> restaurants = new ArrayList<>(); //리스트 만들고
//
//        restaurants.add(new Restaurant(1004L, "Bob zip", "Seoul")); //리스트에 더해주고
//        restaurants.add(new Restaurant(2020L, "Cyber food", "Seoul"));

        //-------------1-----------
//        List<Restaurant> restaurants = new ArrayList<>();
//        restaurants = repository.findAll();
        //------------------------
        //1과 같음
//        List<Restaurant> restaurants = repository.findAll();
        //-----------------------
        Restaurant restaurant = restaurantsRepository.findById(id);

        List<MenuItem> menuitems = menuItemRepository.findAllByRestaurantId(id);
        restaurant.setMenuItems(menuitems);

        //----------repository로 넘겨줌---------------
//        Restaurant restaurant = restaurants.stream() //리슽트를 스트림으로 바꿔서
//                .filter(r -> r.getId().equals(id)) //@PathVariable("id")
//                .findFirst() //첫번째 거
////                .get();
//                .orElse(null);
        //------------------------------------------

        return restaurant;

    }


}
