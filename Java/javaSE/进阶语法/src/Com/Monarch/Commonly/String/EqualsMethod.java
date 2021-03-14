package Com.Monarch.Commonly.String;

public class EqualsMethod {
    public static void main(String[] args) {
        String s = "张三";
        String s1 = "张三";
        String s2 = "李四";
        int[] i = {1,2,3};
        System.out.println(s.equals(s1));
        System.out.println(s == s1);
        System.out.println(s.equals(s2));
        System.out.println(s == s2);
    }
}
