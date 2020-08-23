package application;

import domain.Restaurant;
import domain.RestaurantRepository;
import domain.RestaurantRepositoryImpl;

import org.junit.Before;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.transaction.BeforeTransaction;


//import static org.hamcrest.Matchers.is;
//import static org.junit.Assert.assertThat;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.core.Is.is;
import static org.junit.jupiter.api.Assertions.*;


class RestaurantServiceTest {

    private RestaurantService restaurantService;
    RestaurantRepository restaurantRepository;


    @BeforeEach //모든 테스트가 실행되기 전에 실행  셋업실행하고 테스트1, 셋업실행하고 테스트2
    public void setUp() {
        restaurantRepository = new RestaurantRepositoryImpl();
        restaurantService = new RestaurantService(restaurantRepository);
    }


    @Test //실패하는지 왜 모르겠 -> 
    public void getRestaurant() {
        Restaurant restaurant = restaurantService.getRestaurant(1004L);
        assertThat(restaurant.getId(), is(1004L));

    }

}