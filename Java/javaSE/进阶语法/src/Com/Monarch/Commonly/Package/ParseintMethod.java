package Com.Monarch.Commonly.Package;

public class ParseintMethod {
    public static void main(String[] args) {
        int i = Integer.parseInt("10000");
        int i1 = Integer.parseInt("10000", 2);
        int i2 = Integer.parseInt("10000", 8);
        System.out.println(i);
        System.out.println(i1);
        System.out.println(i2);
    }
}
