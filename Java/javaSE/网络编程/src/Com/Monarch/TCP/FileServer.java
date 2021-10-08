package Com.Monarch.TCP;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class FileServer {
    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = new ServerSocket(9000);
        Socket socket = serverSocket.accept();
        InputStream is = socket.getInputStream();

        FileOutputStream file = new FileOutputStream(new File("网络编程/baijing.jpg"));
        byte[] buffer = new byte[1024];
        int len;
        while ((len = is.read(buffer)) != -1){
            file.write(buffer, 0, len);
        }

        OutputStream os = socket.getOutputStream();
        os.write("我接收完毕了, 你可以断开了".getBytes());

        file.close();
        is.close();
        socket.close();
        serverSocket.close();
    }
}
