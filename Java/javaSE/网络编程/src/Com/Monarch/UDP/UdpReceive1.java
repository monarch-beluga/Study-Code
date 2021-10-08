package Com.Monarch.UDP;

import java.net.DatagramPacket;
import java.net.DatagramSocket;

public class UdpReceive1 {
    public static void main(String[] args) throws Exception{
        DatagramSocket socket = new DatagramSocket(6666);

        while (true) {
            byte[] osBytes = new byte[1024];
            DatagramPacket osPacket = new DatagramPacket(osBytes, 0, osBytes.length);
            socket.receive(osPacket);
            String os = new String(osPacket.getData(), 0, osPacket.getLength());
            System.out.println(os);
            if (os.equals("bye"))
                break;
        }
        socket.close();
    }
}
