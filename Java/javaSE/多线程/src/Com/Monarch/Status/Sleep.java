package Com.Monarch.Status;

public class Sleep {
    public static void main(String[] args) {
        SleepRunner runner = new SleepRunner();
        new Thread(runner,"小明").start();
        new Thread(runner,"老师").start();
        new Thread(runner,"黄牛").start();
    }
}

class SleepRunner implements Runnable{

    private int ticketNums = 10;

    @Override
    public void run() {
        while (ticketNums > 0) {
            try {
                Thread.sleep(10);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println(Thread.currentThread().getName() + "——>拿到了第" + ticketNums-- + "票");
        }
    }
}
