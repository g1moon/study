package domain;

import java.util.List;

//인터페이스 - 메서드만 명시해줌
public interface MenuItemRepository {

    List<MenuItem> findAllByRestaurantId(Long retaurantId);

}
