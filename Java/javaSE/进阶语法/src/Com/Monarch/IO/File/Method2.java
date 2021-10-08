package Com.Monarch.IO.File;

import java.io.File;

public class Method2 {
    public static void main(String[] args) {
        File file1 = new File("E:\\temp\\npp");
        File[] files1 = file1.listFiles();
        for (File file : files1) {
            System.out.println(file.getName()+"文件的大小为："+file.length()+"字节");
        }
        File file2 = new File("E:\\temp\\a.txt");
        System.out.println(file2+"是否存在："+file2.exists());
        System.out.println("是否删除了文件："+file2.delete());
        System.out.println(file2+"是否存在："+file2.exists());
    }
}