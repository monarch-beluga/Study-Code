package Com.Monarch.Pool;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class CreatePool {
    public static void main(String[] args) {
        ExecutorService service = Executors.newFixedThreadPool(10);

        for (int i = 0; i < 100; i++) {
            service.execute(new MyThread());
        }

        service.shutdown();
    }
}

class MyThread implements Runnable{

    @Override
    public void run() {
        System.out.println(Thread.currentThread().getName());
    }
}
