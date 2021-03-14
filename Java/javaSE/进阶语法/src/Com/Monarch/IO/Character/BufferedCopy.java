package Com.Monarch.IO.Character;

import java.io.*;

public class BufferedCopy {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader("E:\\temp\\a.txt"));
        BufferedWriter writer = new BufferedWriter(new FileWriter("E:\\temp\\d.txt"));
        int len;
        while ((len = reader.read()) != -1){
            writer.write(len);
        }
        System.out.println("end");
        writer.close();
        reader.close();
    }
}
