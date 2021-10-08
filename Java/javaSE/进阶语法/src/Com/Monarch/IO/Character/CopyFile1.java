package Com.Monarch.IO.Character;

import java.io.*;

public class CopyFile1 {
    public static void main(String[] args) throws IOException {
        Reader reader = new FileReader("E:\\temp\\a.txt");
        Writer writer = new FileWriter("E:\\temp\\c.txt");
        char[] chars = new char[1024];
        int len;
        while ((len = reader.read(chars)) != -1){
            writer.write(chars, 0, len);
        }
        System.out.println("end");
        writer.close();
        reader.close();
    }
}
