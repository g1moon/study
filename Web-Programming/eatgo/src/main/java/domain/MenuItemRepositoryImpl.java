package domain;

import org.springframework.stereotype.Component;

import java.util.ArrayList;
import java.util.List;

@Component //구현체 : 컴포넌트 달아주고, 임플리먼트해주고, 오버라이드
public class MenuItemRepositoryImpl implements MenuItemRepository {
    private List<MenuItem> menuItems = new ArrayList<>();

    public MenuItemRepositoryImpl() {
        menuItems.add(new MenuItem("Kimchi"));
    }

    @Override
    public List<MenuItem> findAllByRestaurantId(Long retaurantId) {
        return menuItems;
    }
}
