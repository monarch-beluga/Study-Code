package Com.Monarch.IO.Bate;

import java.io.*;

public class Buffered1 {
    public static void main(String[] args) throws IOException {
        BufferedInputStream bis = new BufferedInputStream(new FileInputStream("E:\\temp\\a\\1.png") );
        BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream("E:\\temp\\a\\4.png"));
        int len;
        while ((len = bis.read()) != -1) {
            bos.write(len);
        }
        System.out.println("end");
        bis.close();
        bos.close();
    }
}
