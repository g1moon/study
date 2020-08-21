package me.g1moon.springbootsecurity2;


import me.g1moon.springbootsecurity2.account.Account;
import me.g1moon.springbootsecurity2.account.AccountService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.stereotype.Component;

@Component
public class AccountRunner  implements ApplicationRunner {

    @Autowired
    AccountService accountService;

    @Override
    public void run(ApplicationArguments args) throws Exception {
        Account g1moon = accountService.createAccount("g1moon", "1234");
        System.out.println(g1moon.getUsername() + " pw: " +g1moon.getPassword());
    }
}
