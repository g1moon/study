package domain;

import org.springframework.stereotype.Component;

import java.util.ArrayList;
import java.util.List;
//구현체
@Component
public class RestaurantRepositoryImpl implements RestaurantRepository {
    //필드로 리스트 만들어주고
    private List<Restaurant> restaurants = new ArrayList<>();

    //생성자로 데이터 넣어주고
    public RestaurantRepositoryImpl() {
        restaurants.add(new Restaurant(1004L, "Bob zip", "Seoul"));
        restaurants.add(new Restaurant(2020L,"Cyber food", "Seoul"));
    }

    //-------인터페이스로 분리(메서드)-----------------------
    @Override
    public List<Restaurant> findAll() {
            return restaurants;
    }

    @Override
    public Restaurant findById(Long id) {
        return restaurants.stream()
                .filter(r -> r.getId().equals(id))
                .findFirst()
                .orElse(null);
    }
    //---------------------------------------------
}
