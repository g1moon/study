package me.g1moon.springbootsecurity2.account;

import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

//account repository에서 데이터를 관리
public interface AccountRepository  extends JpaRepository<Account, Long> {

    Optional<Account> findByUserName(String username);

}
