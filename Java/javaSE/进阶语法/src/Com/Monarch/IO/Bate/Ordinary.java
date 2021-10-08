package Com.Monarch.IO.Bate;

import java.io.*;

public class Ordinary {
    public static void main(String[] args) throws IOException {
        InputStream fis = new FileInputStream("E:\\temp\\a\\1.png");
        OutputStream fos = new FileOutputStream("E:\\temp\\a\\2.png");
        int len;
        while ((len = fis.read()) != -1){
            fos.write(len);
        }
        System.out.println("end");
        fis.close();
        fos.close();

    }
}
