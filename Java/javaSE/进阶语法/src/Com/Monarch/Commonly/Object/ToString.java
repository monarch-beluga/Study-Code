package Com.Monarch.Commonly.Object;

public class ToString {
    public static void main(String[] args) {
        Object o = new Object();
        System.out.println(o.toString());

    }
}

/*
public String toString() {
    return getClass().getName() + "@" + Integer.toHexString(hashCode());
}
 */
