package Com.Monarch.Communication;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.SocketException;

public class TalkReceive implements Runnable{
    private final DatagramSocket socket;
    private final String msgFrom;

    public TalkReceive(int formPort, String msgFrom) throws SocketException {
        socket = new DatagramSocket(formPort);
        this.msgFrom = msgFrom;
    }

    @Override
    public void run() {
        while (true) {
            byte[] osBytes = new byte[1024];
            DatagramPacket osPacket = new DatagramPacket(osBytes, 0, osBytes.length);
            try {
                socket.receive(osPacket);
            } catch (IOException e) {
                e.printStackTrace();
            }
            String os = new String(osPacket.getData(), 0, osPacket.getLength());
            System.out.println(msgFrom+":"+os);
            if (os.equals("bye")){
                break;
            }
        }
        socket.close();
        System.exit(0);
    }
}
