package Com.Monarch.ThreadClass;

public class TestThread1 extends Thread{
    @Override
    public void run() {
        for (int i = 0; i < 5; i++) {
            try {
                sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("我在看代码——"+i);
        }
    }

    public static void main(String[] args) throws InterruptedException {
        TestThread1 thread1 = new TestThread1();

        thread1.start();

        for (int i = 0; i < 5; i++) {
            sleep(100);
            System.out.println("我在学习多线程——"+i);
        }
    }
}
