package me.g1moon.springbootjpa.account;

import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;


public interface AccountRepository extends JpaRepository<Account, Long> {
    Account findByUsername(String username);

//    Optional<Account> findByUsername(String username);
    //
}
