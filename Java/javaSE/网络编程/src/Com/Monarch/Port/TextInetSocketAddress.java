package Com.Monarch.Port;

import java.net.InetSocketAddress;

public class TextInetSocketAddress {
    public static void main(String[] args) {
        InetSocketAddress socketAddress1 = new InetSocketAddress("127.0.0.1", 8080);
        InetSocketAddress socketAddress2 = new InetSocketAddress("localhost", 8080);
        System.out.println(socketAddress1);
        System.out.println(socketAddress2);

        System.out.println(socketAddress1.getAddress());
        System.out.println(socketAddress1.getHostName());
        System.out.println(socketAddress1.getPort());
    }
}
