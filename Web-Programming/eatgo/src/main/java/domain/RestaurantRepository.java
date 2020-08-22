package domain;

import java.util.List;

//인터페이스로 메서들들 나누고
public interface RestaurantRepository {
    //(리턴타입)  메서
    List<Restaurant> findAll();
    Restaurant findById(Long id);

}
