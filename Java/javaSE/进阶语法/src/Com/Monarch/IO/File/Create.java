package Com.Monarch.IO.File;

import java.io.File;

public class Create {
    public static void main(String[] args) {
        File file = new File("E:\\temp\\a.txt");
        System.out.println("file："+file);
        System.out.println("==============");
        File file1 = new File("E:\\temp\\", "a.txt");
        System.out.println("file1："+file1);
        System.out.println("==============");
        File path = new File("E:\\temp\\");
        File file2 = new File(path, "a.txt");
        System.out.println("file2："+file2);
        System.out.println("==============");
    }
}
