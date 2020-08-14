package me.g1moon.springbootjpa.account;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.test.context.junit4.SpringRunner;
//import org.springframework.test.context.junit4.SpringRunner;

import javax.sql.DataSource;

import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.SQLException;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.*;
//@SpringBootTest //이렇게 만들면 -> 이테스트는 -> 통합테스트 -> 에플리케이션 모든 빈이 다등록됨
////@SpringBootApplication 찾아서 -> 그래서 아래 di 메서드는 -> postgresql사용하게된다
////그런데 이러한 방법은 권장하지 않음 -> 인메모리 데이터베이스를 사용하는 것이 빠름
////테스트에서 디비설정 바꾸면 -> 진짜 디비설정이 바뀜...
@RunWith(SpringRunner.class)
@DataJpaTest //레포랑 관련된 테스트만 -> 슬라이싱 테스팅
public class AccountRepositoryTest {


    @Autowired
    DataSource dataSource;

    @Autowired
    JdbcTemplate jdbcTemplate;

    @Autowired
    AccountRepository accountRepository;

    @Test
    public void di() throws SQLException {
        Account account = new Account();
        account.setUsername("g1moon");
        account.setPassword("1234");

//        Account newAccount = accountRepository.save(account);
        accountRepository.save(account);
//        assertThat(newAccount).isNotNull(); //junit정리해주고
//
//        Account existingAcoount = accountRepository.findByUsername(newAccount.getUsername());
//        assertThat(existingAcoount).isNotNull();
//
////        Account nonExsistingAcoount = accountRepository.findByUsername(newAccount.getUsername());
////        assertThat(nonExsistingAcoount).isNull();
//
//        //옵셔널로 감싸서 -> isNotEmpty() , isEmpty로 할수도있음
    }

}


