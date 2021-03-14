package Com.Monarch.Communication;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetSocketAddress;
import java.net.SocketException;
import java.util.Scanner;

public class TalkSend implements Runnable{
    private final Scanner reader = new Scanner(System.in);
    private final DatagramSocket socket;
    private final String toIP;
    private final int toPort;

    public TalkSend(int fromPort, String toIP, int toPort) throws SocketException {
        this.toIP = toIP;
        this.toPort = toPort;

        socket = new DatagramSocket(fromPort);
    }

    @Override
    public void run() {
        while (true) {
            String is = reader.nextLine();
            byte[] isBytes = is.getBytes();
            DatagramPacket isPacket = new DatagramPacket(isBytes, 0, isBytes.length, new InetSocketAddress(toIP, toPort));
            try {
                socket.send(isPacket);
            } catch (IOException e) {
                e.printStackTrace();
            }
            if (is.equals("bye")){
                reader.close();
                break;
            }
        }
        socket.close();

        System.exit(0);
    }
}
