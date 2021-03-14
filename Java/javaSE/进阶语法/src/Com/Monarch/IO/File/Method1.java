package Com.Monarch.IO.File;

import java.io.File;

public class Method1 {
    public static void main(String[] args) {
        File file1 = new File("out\\production");
        System.out.println("file1的绝对路径："+file1.getAbsolutePath());
        System.out.println("file1的相对路径："+file1.getPath());
        System.out.println("====================");
        File file2 = new File("E:\\temp\\a.txt");
        System.out.println("路径为："+file2);
        System.out.println("文件名为："+file2.getName());
        System.out.println("====================");
        File path = new File("E:\\temp\\npp");
        String[] files = path.list();
        for (int i = 0; i < files.length;) {
            System.out.print(files[i] + "\t");
            if (++i % 2 == 0)
                System.out.println();
        }
        System.out.println("====================");
        File[] files1 = path.listFiles();
        for (File file : files1) {
            System.out.println(file);
        }
    }
}
