package Com.Monarch.Commonly.String;

public class GetBytesMethod {
    public static void main(String[] args) {
        String s = "abcd";
        byte[] bytes = s.getBytes();
        for (byte aByte : bytes) {
            System.out.print(aByte + "\t");
        }
        System.out.println();
        System.out.println(s);
    }
}
