package me.g1moon.springbootjpa.account;

import org.springframework.data.jpa.repository.JpaRepository;


public interface AccountRepository extends JpaRepository<Account, Long> {
    Account findByUsername(String username);
    //
}
