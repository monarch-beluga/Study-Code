package Com.Monarch.TCP;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class TextTcpServer {
    public static void main(String[] args){
        ServerSocket socketSocket = null;
        Socket socket = null;
        InputStream is = null;
        ByteArrayOutputStream boas = null;
        try {
            socketSocket = new ServerSocket(9999);
            socket = socketSocket.accept();
            is = socket.getInputStream();

            /*
                byte[] buffer = new byte[1024];
                int len;
                while ((len = is.read(buffer)) != 1){
                    String msg = new String(buffer, 0, len);
                    System.out.println(msg);
                }
             */
            boas = new ByteArrayOutputStream();
            byte[] buffer = new byte[1024];
            int len;
            while ((len = is.read(buffer)) != -1){
                boas.write(buffer, 0, len);
            }
            System.out.println(boas.toString());

        } catch (IOException e) {
            e.printStackTrace();
        }finally {
            if (boas != null) {
                try {
                    boas.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if (is != null) {
                try {
                    is.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if (socket != null) {
                try {
                    socket.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if (socket != null) {
                try {
                    socket.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
