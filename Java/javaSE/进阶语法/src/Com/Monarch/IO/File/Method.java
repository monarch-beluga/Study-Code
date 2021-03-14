package Com.Monarch.IO.File;

import java.io.File;
import java.io.IOException;

public class Method {
    public static void main(String[] args) {
        String s = "E:\\temp\\b.txt";
        File file3 = new File(s);
        System.out.println(s+"该文件是否存在："+file3.exists());
        try {
            boolean newFile = file3.createNewFile();
        } catch (IOException e) {
            System.out.println("没有该路径");
        }
        System.out.println(s+"该文件是否存在："+file3.exists());
        System.out.println("==============");
        String s1 = "E:\\temp\\a";
        String s2 = "E:\\temp\\a\\b\\c";
        File file4 = new File(s1);
        File file5 = new File(s2);
        System.out.println(s1+"该路径是否存在："+file4.exists());
        System.out.println(s2+"该路径是否存在："+file5.exists());
        boolean newpath = file4.mkdir();
        newpath = file5.mkdirs();
        System.out.println(s1+"该路径是否存在："+file4.exists());
        System.out.println(s2+"该路径是否存在："+file5.exists());
        System.out.println("==============");
        System.out.println(s1+"是否为文件夹:"+file4.isDirectory());
        System.out.println(s+"是否为文件夹:"+file3.isDirectory());
        System.out.println(s+"是否为文件:"+file3.isFile());
    }
}
