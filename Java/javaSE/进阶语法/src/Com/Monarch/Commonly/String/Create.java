package Com.Monarch.Commonly.String;

public class Create {
    public static void main(String[] args) {
        String name = "Monarch";
        System.out.println(name);
        String s = new String();
        System.out.println(s);
        byte[] b = {97,98,99};
        String s1 = new String(b);
        System.out.println(s1);
        String s2 = new String(b, 1, 2);
        System.out.println(s2);
        char[] chars = {'a','b','c','d'};
        String s3 = new String(chars);
        System.out.println(s3);
        String s4 = new String(chars, 1, 2);
        System.out.println(s4);
    }
}
