package Com.Monarch.Status;

public class TestJoin {
    public static void main(String[] args) throws InterruptedException {
        JoinRunner runner = new JoinRunner();
        Thread thread = new Thread(runner);
        thread.start();

        for (int i = 0; i < 10; i++) {
            if (i > 5)
                thread.join();
            System.out.println("main..."+i);
        }
    }
}
class JoinRunner implements Runnable{

    @Override
    public void run() {
        for (int i = 0; i < 20; i++) {
            System.out.println("VIP...."+i);
        }
    }
}
