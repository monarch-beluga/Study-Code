package Com.Monarch.IO.Bate;

import java.io.ByteArrayInputStream;
import java.io.IOException;

public class ByteArrayInput {
    public static void main(String[] args) {
        byte[] src = "talk is show me the code".getBytes();
        ByteArrayInputStream is = new ByteArrayInputStream(src);
        try {
            byte[] buffer = new byte[5];
            int len;
            while ((len = is.read(buffer)) != -1){
                String str = new String(buffer, 0, len);
                System.out.print(str);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
