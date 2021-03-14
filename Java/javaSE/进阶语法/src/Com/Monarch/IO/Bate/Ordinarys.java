package Com.Monarch.IO.Bate;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class Ordinarys {
    public static void main(String[] args) throws IOException {
        FileInputStream fis = new FileInputStream("E:\\temp\\a\\1.png");
        FileOutputStream fos = new FileOutputStream("E:\\temp\\a\\3.png");
        byte[] b = new byte[2048];
        int len;
        while ((len = fis.read(b)) != -1){
            fos.write(b, 0, len);
        }
        System.out.println("end");
        fis.close();
        fos.close();
    }
}
