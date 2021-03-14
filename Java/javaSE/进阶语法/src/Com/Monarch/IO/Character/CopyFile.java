package Com.Monarch.IO.Character;

import java.io.*;

public class CopyFile {
    public static void main(String[] args) throws IOException {
        Reader reader = new FileReader("E:\\temp\\a.txt");
        Writer writer = new FileWriter("E:\\temp\\b.txt");
        int a;
        while ((a = reader.read()) != -1){
            writer.write(a);
        }
        System.out.println("end");
        writer.close();
        reader.close();
    }
}
