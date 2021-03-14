package Com.Monarch.Commonly.StringBuilder;

public class Method {
    public static void main(String[] args) {
        StringBuilder stringBuilder = new StringBuilder();
        StringBuilder stringBuilder1 = new StringBuilder();
        stringBuilder.append("monarch,");
        stringBuilder.append(15);
        stringBuilder.append(",男");
        System.out.println(stringBuilder);
        stringBuilder.reverse();
        System.out.println(stringBuilder);
        String s = stringBuilder.toString();
        System.out.println(s);
        System.out.println("=================");
        stringBuilder1.append(21).append(12).append(32);
        System.out.println(stringBuilder1);
    }
}
