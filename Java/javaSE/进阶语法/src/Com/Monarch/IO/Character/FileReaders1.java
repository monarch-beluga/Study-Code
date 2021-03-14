package Com.Monarch.IO.Character;

import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;

public class FileReaders1 {
    public static void main(String[] args) throws IOException {
        File file1 = new File("E:\\temp\\npp");
        File[] files1 = file1.listFiles();
        Reader reader = new FileReader(files1[0]);
        char[] chars = new char[5];
        int len;
        while (true){
            len = reader.read(chars);
            if (len < chars.length){
                String s = new String(chars, 0, len);
                System.out.print(s);
                break;
            }
            System.out.print(chars);
        }
        reader.close();
    }
}
