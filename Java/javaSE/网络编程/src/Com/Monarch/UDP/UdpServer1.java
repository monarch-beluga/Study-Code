package Com.Monarch.UDP;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetSocketAddress;
import java.util.Scanner;

public class UdpServer1 {
    public static void main(String[] args) throws Exception{
        DatagramSocket socket = new DatagramSocket(8888);
        Scanner reader = new Scanner(System.in);

        while (true) {
            String is = reader.nextLine();
            byte[] isBytes = is.getBytes();
            DatagramPacket isPacket = new DatagramPacket(isBytes, 0, isBytes.length, new InetSocketAddress("localhost", 6666));
            socket.send(isPacket);
            if (is.equals("bye"))
                break;
        }
        reader.close();
        socket.close();
    }
}
