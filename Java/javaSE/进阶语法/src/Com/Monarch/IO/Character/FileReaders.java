package Com.Monarch.IO.Character;

import java.io.*;

public class FileReaders {
    public static void main(String[] args) throws IOException {
        File file1 = new File("E:\\temp\\npp");
        File[] files1 = file1.listFiles();
        Reader reader = new FileReader(files1[0]);
        System.out.println(files1[0]);
        int a;
        while ((a = reader.read()) != -1){
            System.out.print((char)a);
        }
        reader.close();
    }
}
