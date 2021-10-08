package Com.Monarch.UDP;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class TestUdpClient {
    public static void main(String[] args) throws Exception {
        InetAddress localhost = InetAddress.getByName("localhost");
        int port = 9090;
        DatagramSocket socket = new DatagramSocket();
        String msg = "你好啊，服务器！";
        DatagramPacket packet = new DatagramPacket(msg.getBytes(), 0, msg.getBytes().length, localhost, port);
        socket.send(packet);
        socket.close();
    }
}
