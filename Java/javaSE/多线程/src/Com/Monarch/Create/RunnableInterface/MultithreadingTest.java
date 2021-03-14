package Com.Monarch.Create.RunnableInterface;

public class MultithreadingTest {
    public static void main(String[] args) {
        Runner runner = new Runner();
        new Thread(runner,"小明").start();
        new Thread(runner,"老师").start();
        new Thread(runner,"黄牛").start();
    }
}
class Runner implements Runnable{
    private int ticketNums = 6;

    @Override
    public void run() {
        while (ticketNums > 0) {
            System.out.println(Thread.currentThread().getName() + "——>拿到了第" + ticketNums-- + "票");
        }
    }
}