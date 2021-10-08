package Com.Monarch.Commonly.String;

public class ToCharArrayMethod {
    public static void main(String[] args) {
        String s = "白鲸";
        char[] chars = s.toCharArray();
        for (char aChar : chars) {
            System.out.print(aChar + "\t");
        }
        System.out.println();
        System.out.println(s);
    }
}
