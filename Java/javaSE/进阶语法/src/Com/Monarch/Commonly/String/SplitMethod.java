package Com.Monarch.Commonly.String;

public class SplitMethod {
    public static void main(String[] args) {
        String s = "monarch+男+15";
        String[] strs = s.split("\\+");
        for (String str : strs) {
            System.out.println(str);
        }
        System.out.println(s);
    }
}
