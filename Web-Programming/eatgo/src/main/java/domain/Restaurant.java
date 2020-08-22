package domain;

public class Restaurant {
    private final String location;
    private final Long id;
    private String name; //레스토랑 객체의 파라미터



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
}




