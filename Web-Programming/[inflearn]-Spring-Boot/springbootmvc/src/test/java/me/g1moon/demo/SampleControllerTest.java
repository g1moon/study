package me.g1moon.demo;

import com.gargoylesoftware.htmlunit.WebClient;
import com.gargoylesoftware.htmlunit.html.HtmlHeading1;
import com.gargoylesoftware.htmlunit.html.HtmlPage;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.web.servlet.MockMvc;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.internal.bytebuddy.matcher.ElementMatchers.is;
import static org.assertj.core.internal.bytebuddy.matcher.ElementMatchers.nameContains;
import static org.hamcrest.Matchers.containsString;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultHandlers.print;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;


@RunWith(SpringRunner.class)
@WebMvcTest(SampleController.class)
public class SampleControllerTest  {

    @Autowired
    MockMvc mockMvc;
    //WebClient을 이용한 테스트 (html의 겨롸를 맞춰보는데보다 효과적---------
//    @Autowired
//    WebClient webClinet;
//
//    @Test
//    public void hello() {
//        HtmlPage page = webClinet.getPage("/hello"); //get
//        HtmlHeading1 h1 = page.getFirstByXPath("//h1"); //첫번쨰 헤더따서
//        assertThat(h1.getTextContent()).isEqualToIgnoringCase("g1moon"); //g1moon인
//    }
    //------------------------------------ -----------
    @Test
    public void hello() throws Exception {
        //요청 "/"
        //응답
        // -모델 name: keesun
        // -뷰 이름 : hello
        //mockmvc로 겟요청하면 -> 스테이터스가 오케이가 나와야하고 ->
        //view의네임이 헬로우(result matcher) ,
        //model에 name이라는 값을 줄거고 -> 그게 기문으로 잘 나오는지..

        mockMvc.perform(get("/hello"))
                .andExpect(status().isOk())
                .andDo(print()) //jsp는 이러한게 힘들어..
                .andExpect(view().name("hello"))
                .andExpect(content().string(containsString("g1moon")));
//                .andExpect(model().attribute("name", is("g1moon")));

    }
}
