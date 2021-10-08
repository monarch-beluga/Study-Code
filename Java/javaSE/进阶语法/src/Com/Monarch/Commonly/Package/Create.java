package Com.Monarch.Commonly.Package;

public class Create {
    public static void main(String[] args) {
        Integer i = 10;
        Integer i1 = new Integer(10);
        Integer i2 = new Integer("10");
        Integer i3 = Integer.valueOf(10);
        Integer i4 = Integer.valueOf("10");
        Integer i5 = Integer.valueOf("1000", 2);
        Integer i6 = Integer.valueOf("1000", 8);
        System.out.println(i);
        System.out.println(i1);
        System.out.println(i2);
        System.out.println(i3);
        System.out.println(i4);
        System.out.println(i5);
        System.out.println(i6);
    }
}
