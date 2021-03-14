package Com.Monarch.TCP;

import java.io.*;
import java.net.InetAddress;
import java.net.Socket;

public class FileTcpClient {
    public static void main(String[] args) throws Exception {
        Socket socket = new Socket(InetAddress.getByName("127.0.0.1"), 9000);

        OutputStream os = socket.getOutputStream();
        FileInputStream file = new FileInputStream(new File("网络编程/Monarch.jpg"));
        byte[] buffer = new byte[1024];
        int len;
        while ((len = file.read(buffer)) != -1){
            os.write(buffer, 0, len);
        }

        socket.shutdownOutput();

        InputStream is = socket.getInputStream();
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        byte[] bytes = new byte[1024];
        int len1;
        while ((len1 = is.read(bytes)) != -1){
            outputStream.write(bytes, 0, len1);
        }
        System.out.println(outputStream.toString());

        file.close();
        os.close();
        socket.close();
    }
}
