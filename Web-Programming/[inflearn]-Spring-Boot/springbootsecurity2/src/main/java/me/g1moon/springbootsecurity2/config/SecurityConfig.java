package me.g1moon.springbootsecurity2.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfiguration;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

@Configuration //WebSecurityConfigurerAdapter순간부터 -> autoconfig 중지
public class SecurityConfig extends WebSecurityConfigurerAdapter {

    @Override //Http 가져와서
    protected void configure(HttpSecurity http) throws Exception {
        //루트랑 헬로우는 모두 가능하고
        //나머지는 인증이 필요하고 ~
        //폼 로그인을 사용하고 , 베이직인증도 허용하겠다
        http.authorizeRequests()
                .antMatchers("/", "/hello").permitAll()
                .anyRequest().authenticated()
                .and()
            .formLogin()
                .and()
            .httpBasic();
    }
}
