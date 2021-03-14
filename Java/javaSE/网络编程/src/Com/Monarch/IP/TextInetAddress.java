package Com.Monarch.IP;

import java.net.InetAddress;
import java.net.UnknownHostException;

public class TextInetAddress {
    public static void main(String[] args) {
        try {
            InetAddress inetAddress1 = InetAddress.getByName("monarch");
            System.out.println(inetAddress1);
            InetAddress inetAddress2 = InetAddress.getByName("localhost");
            System.out.println(inetAddress2);
            InetAddress inetAddress4 = InetAddress.getLocalHost();
            System.out.println(inetAddress4);

            InetAddress inetAddress3 = InetAddress.getByName("www.baidu.com");
            InetAddress inetAddress5 = InetAddress.getByName("14.215.177.39");
            System.out.println(inetAddress3);
            System.out.println(inetAddress5);

            System.out.println(inetAddress3.getCanonicalHostName());
            System.out.println(inetAddress3.getHostAddress());
            System.out.println(inetAddress3.getHostName());
        } catch (UnknownHostException e) {
            e.printStackTrace();
        }
    }
}
