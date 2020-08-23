package interfaces;

import domain.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringBootConfiguration;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

@RestController
@SpringBootConfiguration
public class RestaurantController {

    @Autowired
    private RestaurantRepositoryImpl restaurantsRepository; //구현체로 받아옴
    @Autowired
    private MenuItemRepository menuItemRepository;


//----------------------------------------------------------
    @GetMapping("/restaurants") //리스트만들고, 객체만들고, 더하고, 리턴
    public List<Restaurant> list() {

        List<Restaurant> restaurants = restaurantsRepository.findAll();
        return restaurants; //리스트를 리턴
    }
//----------------------------------------------------------
    @GetMapping("/restaurants/{id}")
    public Restaurant detail(@PathVariable("id") Long id) {
        
        Restaurant restaurant = restaurantsRepository.findById(id);
        List<MenuItem> menuItems = menuItemRepository.findAllByRestaurantId(id);
        restaurant.setMenuItems(menuItems);

        return restaurant;
    }
//----------------------------------------------------------

}
