package me.g1moon.springbootsecurity2.account;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import javax.swing.text.html.Option;
import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Collection;
import java.util.Optional;

//이게 빈으로 되어있어야 스프링이 유저를 만들지 않아
@Service //UserDetailsService
public class AccountService implements UserDetailsService {

    @Autowired
    private AccountRepository accountRepository; //interface

    //이름과 패스워드 받고 -> 레포에 저장(세터) -> 세이브
    //그리고 다시 넘겨줘서 만든쪽에서 사용할 수 있게
    public Account createAccount(String username, String password) {
        Account account = new Account();
        account.setUsername(username);
        account.setPassword(password);
        return accountRepository.save(account);
    }

    //우리가 입력한 패스워드와, 패스워드가 맞는지 확인 -> 아주 핵심적인 인터페이스
    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        //타입을 정해주고 -> 메서드만들어주고 -> 인터페이스에서 메서드 써
        //orElseThrow 데이터가 없으면 -> 유저네임 낫파운드던지고
        //있으면 리턴값으로 실제 어카운트가 나온다
        Optional<Account> byUserName = accountRepository.findByUserName(username);
        Account account = byUserName.orElseThrow(() -> new UsernameNotFoundException(username));
        return new User(account.getUsername(), account.getPassword(), authorities());

        //리턴할떄는 UserDetatils는 서비스마다 모두 다르게 정의되어있는 인터페이스
        //유저라는 이름으로 스프링 시큐리티가 제공해주는데
        //세번쨰는 어설리티를 줘얗나ㅡㄴ데 ->
    }
    private Collection<? extends GrantedAuthority> authorities() {
        return Arrays.asList(new SimpleGrantedAuthority("ROLE_USER"));
    }
}
