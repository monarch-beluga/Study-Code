package Com.Monarch.IO.Bate;

import java.io.ByteArrayOutputStream;
import java.io.IOException;

public class ByteArrayOut {
    public static void main(String[] args) {
        ByteArrayOutputStream os = new ByteArrayOutputStream();
        byte[] dest = null;

        String msg = "show me the code";
        try {
            byte[] datas = msg.getBytes();
            os.write(datas, 0, datas.length);
            os.flush();
            dest = os.toByteArray();
            System.out.println(dest.length + " " + new String(dest, 0, os.size()));
            System.out.println(os.toString());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
