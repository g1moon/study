package domain;


import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;

public class Restaurant {
    private final String location;
    private final Long id;
    private String name; //레스토랑 객체의 파라미터
    private List<MenuItem> menuitems = new ArrayList<MenuItem>(); //메뉴아이템관리할 리스트


    public Restaurant(Long id, String name, String location) {
        this.name = name; //파라미터 생성자로 잡아주고
        this.location = location;
        this.id = id;
    }

    public Long getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getInformation() {
        return name + " in " + location;
    }

    public String getLocation() {
        return location;
    }

    public List<MenuItem> getMenuitems() {
        return menuitems;
    }

    public void addMenuItem(MenuItem menuItem) {
        menuitems.add(menuItem);
    }

    public void setMenuItems(List<MenuItem> menuItems) {
        for (MenuItem menuItem : menuItems) {
            addMenuItem(menuItem);
        }
    }
}




