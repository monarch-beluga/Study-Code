package Com.Monarch.UDP;

import java.net.DatagramPacket;
import java.net.DatagramSocket;

public class TestUdpServer {
    public static void main(String[] args) throws Exception{
        DatagramSocket socket = new DatagramSocket(9090);
        byte[] buffer = new byte[1024];
        DatagramPacket packet = new DatagramPacket(buffer, 0, buffer.length);
        socket.receive(packet);
        System.out.println(packet.getAddress().getHostName());
        System.out.println(new String(packet.getData(), 0, packet.getLength()));
        socket.close();
    }
}
