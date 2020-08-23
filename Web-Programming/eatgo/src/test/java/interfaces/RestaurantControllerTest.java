package interfaces;

import domain.RestaurantRepository;
import domain.RestaurantRepositoryImpl;
import org.junit.jupiter.api.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.SpyBean;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.web.servlet.MockMvc;

import static org.hamcrest.Matchers.containsString;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;


@RunWith(SpringRunner.class)//스프링을 이용해 이 테스트
@WebMvcTest(RestaurantController.class)//특정 컨트롤러를 테스트한다
class RestaurantControllerTest {

    @Autowired
    private MockMvc mvc;

    @SpyBean(RestaurantRepositoryImpl.class) //컨트롤러에 원하는 객체를 주입해줄 수 있음 //어떤 구현으로 사용할지 넣어줘얗마
    private RestaurantRepository abc; //걍 아무이름으로 줘도 돌아감

    @Test
    public void list() throws Exception {
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

    @Test
    public void detail() throws Exception {
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