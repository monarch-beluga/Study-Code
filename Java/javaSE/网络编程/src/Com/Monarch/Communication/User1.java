package Com.Monarch.Communication;

import java.net.SocketException;

public class User1 {
    public static void main(String[] args) throws SocketException {
        new Thread(new TalkSend(8888, "localhost", 9999)).start();
        new Thread(new TalkReceive(7777, "老师")).start();
    }
}
