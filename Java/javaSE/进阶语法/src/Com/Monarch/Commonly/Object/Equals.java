package Com.Monarch.Commonly.Object;

public class Equals {
    public static void main(String[] args) {
        Equals equals = new Equals();
        Equals equals1 = equals;
        Equals equals2 = new Equals();
        System.out.println(equals.equals(equals1));
        System.out.println(equals.equals(equals2));
    }
}

/*
public boolean equals(Object obj) {
    return (this == obj);
}
 */