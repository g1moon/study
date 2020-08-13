package me.g1moon.demospringmvc.user;


import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.http.MediaType;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.ResultMatcher;

//static method -> get, content, status
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.is;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@RunWith(SpringRunner.class)
@WebMvcTest(UserController.class)
public class UserControllerTest {

    @Autowired
    MockMvc mockMvc;

    @Test
    public void hello() throws Exception {
        mockMvc.perform(get("/hello"))
                .andExpect(status().isOk())
                .andExpect(content().string("hello"));
    }

    @Test
    public void createUser_JOSN() throws Exception {
        //이러한 요청을 보내면 아래와 같아야함
        String userJson = "{\"username\" : \"g1moon\", \"password\":\"123\"}";
        mockMvc.perform(post("/users/create")
                .contentType(MediaType.APPLICATION_JSON)
                //이 헤더에따라 응답이 달라질 수 있(클라이언트가 어떠한 뷰를 원하는가 알기 가장좋은 헤더)
                //근데 accept헤더를 못 쓰는 경우도 있어서 -> "/path?format =pdf" 이런식으로
                .accept(MediaType.APPLICATION_JSON)
                .content(userJson))//여기까지가 요총
            .andExpect(status().isOk())
            .andExpect((ResultMatcher) jsonPath("$.username", //resultMatcher로 모두
                    is(equalTo("g1moon"))))
            .andExpect((ResultMatcher) jsonPath("$.password",
                    is(equalTo("123"))));
    }

    @Test
    public void createUser_XML() throws Exception {
        String userJson = "{\"username\" : \"g1moon\", \"password\":\"123\"}";
        mockMvc.perform(post("/users/create")
                .contentType(MediaType.APPLICATION_JSON_VALUE)
                .accept(MediaType.APPLICATION_XML)
                .content(userJson)) //여기까지가 요청
                .andExpect(status().isOk())
                .andExpect(xpath("/User/username")
                        .string("g1moon"))
                .andExpect(xpath("/User/password")
                        .string("123"));

    }

}
