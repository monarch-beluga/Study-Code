package Com.Monarch.Commonly.Package;

public class ValueOfMethod {
    public static void main(String[] args) {
        Integer i3 = Integer.valueOf(10);
        Integer i4 = Integer.valueOf("10");
        Integer i5 = Integer.valueOf("1000", 2);
        Integer i6 = Integer.valueOf("1000", 8);
        System.out.println(i3);
        System.out.println(i4);
        System.out.println(i5);
        System.out.println(i6);
        Integer integer = 10;
        Integer integer1 = 10;
        Integer integer2 = 1300;
        Integer integer3 = 1300;
        System.out.println(integer == integer1);
        System.out.println(integer.toString());
        System.out.println(integer1.toString());
        System.out.println(integer2 == integer3);
    }
}
