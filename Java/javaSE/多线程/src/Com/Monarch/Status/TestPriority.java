package Com.Monarch.Status;

public class TestPriority {
    public static void main(String[] args) {
        MyPriority priority = new MyPriority();

        Thread t1 = new Thread(priority);
        Thread t2 = new Thread(priority);
        Thread t3 = new Thread(priority);
        Thread t4 = new Thread(priority);
        Thread t5 = new Thread(priority);
        Thread t6 = new Thread(priority);

        t1.start();
        t2.setPriority(1);
        t2.start();
        t3.setPriority(4);
        t3.start();
        t4.setPriority(Thread.MAX_PRIORITY);
        t4.start();
        t5.setPriority(8);
        t5.start();
        t6.setPriority(6);
        t6.start();
        System.out.println(Thread.currentThread().getName()+"-->"+Thread.currentThread().getPriority());

    }
}

class MyPriority implements Runnable{

    @Override
    public void run() {
        System.out.println(Thread.currentThread().getName()+"-->"+Thread.currentThread().getPriority());
    }
}
