package interfaces;

import application.RestaurantService;
import domain.*;
import org.junit.jupiter.api.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.boot.test.mock.mockito.SpyBean;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.web.servlet.MockMvc;

import java.util.ArrayList;
import java.util.List;

import static org.hamcrest.Matchers.containsString;

import static org.mockito.BDDMockito.given;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;


@RunWith(SpringRunner.class)//스프링을 이용해 이 테스트
@WebMvcTest(RestaurantController.class)//특정 컨트롤러를 테스트한다
class RestaurantControllerTest {
    //----------------------------------------------------------
    @Autowired
    private MockMvc mvc;
//-----실제로 테스트에서 서비스, 레포들을 투입한 것인데, mock객체로 대신해서 테스트를 할 수 있음 ------------------
    @MockBean
    private RestaurantService restaurantService; //서비스에 레포들이 담겨있음(식당, 메뉴아이템)
//----------------------------------------------------------
    @Test
    public void list() throws Exception {
//        List<Restaurant> restaurants = new ArrayList<>();
//        restaurants.add(new Restaurant(1004L, "Bob zip", "Seoul"));
//        given(restaurantService.getRestaurants()).willReturn(restaurants);//getRest를하면 -> restaurants를 리턴할 것이다

        mvc.perform(get("/restaurants"))
                //Restaurant restaurant = new Restaurant(1004L,"Bob zip", "Seoul");
                .andExpect(status().isOk())
                .andExpect(content().string(containsString("Bob zip")))
                .andExpect(content().string(containsString("Seoul")))
                .andExpect(content().string(
                        containsString("\"name\":\"Bob zip\"")))
                .andExpect(content().string(containsString("Kimchi")))
                .andExpect(content().string(containsString("\"id\":1004")));

    }
//----------------------------------------------------------
    @Test
    public void detail() throws Exception {
        Restaurant restaurant1 = new Restaurant(1004L, "Bob zip", "Seoul");
        restaurant1.addMenuItem(new MenuItem("Kimchi"));

        Restaurant restaurant2 = new Restaurant(2020L, "Cyber food", "Seoul");

        given(restaurantService.getRestaurant(1004L)).willReturn(restaurant1);
        given(restaurantService.getRestaurant(2020L)).willReturn(restaurant2);

        mvc.perform(get("/restaurants/1004"))
                //Restaurant restaurant = new Restaurant(1004L,"Bob zip", "Seoul");
                .andExpect(status().isOk())
                .andExpect(content().string(containsString("\"id\":1004")))
                .andExpect(content().string(containsString("\"name\":\"Bob zip\"")));

        mvc.perform(get("/restaurants/2020"))
                //Restaurant restaurant = new Restaurant(2020L,"Bob zip", "Seoul");
                .andExpect(status().isOk())
                .andExpect(content().string(containsString("\"id\":2020")))
                .andExpect(content().string(containsString("\"name\":\"Cyber food\"")));

    }

}