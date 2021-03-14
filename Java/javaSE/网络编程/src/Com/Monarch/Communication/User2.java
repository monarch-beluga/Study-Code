package Com.Monarch.Communication;

import java.net.SocketException;

public class User2{
    public static void main(String[] args) throws SocketException {
        new Thread(new TalkSend(5555, "localhost", 7777)).start();
        new Thread(new TalkReceive(9999, "学生")).start();
    }
}
