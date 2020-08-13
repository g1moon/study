package me.g1moon.demospringhateoas;

import org.springframework.hateoas.EntityModel;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import static org.springframework.hateoas.server.mvc.WebMvcLinkBuilder.linkTo;
import static org.springframework.hateoas.server.mvc.WebMvcLinkBuilder.methodOn;

@RestController
public class SampleController {

    @GetMapping("/hello")
    public Hello hello() {
        Hello hello = new Hello();
        hello.setPrefix("Hey,");
        hello.setName("g1moon");
        return hello;

        //여기까지하면 에러가 날거야 -> 왜냐하면 링크정보가 없기때문ㅇ
        //링크 정보를 추가하는 방법
        //Hello라는 리소스를 만들고 -> (우리가 제공하는 리소스 + 링크정보)
        EntityModel<Hello> helloResource = new EntityModel<>(hello);
        helloResource.add(linkTo(methodOn(SampleController.class).hello()).withSelfRel());

        return helloResource;
    }


}
