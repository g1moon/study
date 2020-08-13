package me.g1moon.springbootjdbc;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Component;

import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.Statement;

@Component
//public class H2Runner implements ApplicationRunner
public class MySQLRunner implements ApplicationRunner {

    @Autowired
    DataSource dataSource;

    @Autowired// 더 간결하고 좋은 것 같
    JdbcTemplate jdbcTemplate;

    //spring.h2.console.enable=true를 properties에 명시해준다
    //spring.datasource.hikari.maximum-pool-size=4
    @Override
    public void run(ApplicationArguments args) throws Exception {

        //에플리케이션에 커넥트 객체를 주지 못하면 종료해주고 이러한 설정들
        //몇개를 유지할 것이냐 ~ 이것이 매우 중요 -> 성능에 매우 큰 영향을 끼침
        //시피유 코어가 넘어간 커넥트는 -> 실행이 안됨... 잘 설정해야함
        //spring.datasource.hikari.maximum-pool-size=4
        try(Connection connection = dataSource.getConnection()){
            System.out.println(connection.getClass()); //어떤 dbpc 사용하는지.
            System.out.println(connection.getMetaData().getDriverName());
            System.out.println(connection.getMetaData().getURL());
            System.out.println(connection.getMetaData().getUserName());

            Statement statement = connection.createStatement();
            String sql = "CREATE TABLE USERS(ID INTEGER NOT NULL, name VARCHAR(255), PRIMARY KEY(ID))";
            statement.executeUpdate(sql);

        }
        //jdbc 템플릿을 사용하면 이렇게하면 좀 더 안전하게 간결하게 할 수 있음
        jdbcTemplate.execute("INSERT INTO USERS VALUES(1, 'g1moon')");

    }
}
