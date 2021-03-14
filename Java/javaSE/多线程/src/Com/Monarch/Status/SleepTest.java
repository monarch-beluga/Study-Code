package Com.Monarch.Status;

import java.text.SimpleDateFormat;
import java.util.Date;

public class SleepTest {
    public static void main(String[] args) throws InterruptedException {
        Date startTime = new Date(System.currentTimeMillis());
        while (true){
            System.out.println(new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(startTime));
            Thread.sleep(1000);
            startTime = new Date(System.currentTimeMillis());
        }
    }
    public void tenDown() throws InterruptedException {
        int num = 10;
        for (int i = num; i > 0; i--) {
            Thread.sleep(1000);
            System.out.println(i);
        }
    }
}
