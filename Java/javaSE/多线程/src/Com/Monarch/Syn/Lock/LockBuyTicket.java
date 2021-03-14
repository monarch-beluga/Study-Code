package Com.Monarch.Syn.Lock;

import java.util.concurrent.locks.ReentrantLock;

public class LockBuyTicket {
    public static void main(String[] args) {
        BuyTicket station = new BuyTicket();

        new Thread(station, "我").start();
        new Thread(station, "你").start();
        new Thread(station, "黄牛").start();
    }
}

class BuyTicket implements Runnable{
    private int ticketNums = 10;
    private boolean flag = true;

    private final ReentrantLock lock = new ReentrantLock();

    @Override
    public void run() {
        while (flag) {
            try {
                lock.lock();
                try {
                    buy();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }finally {
                lock.unlock();
            }
        }
    }

    private synchronized void buy() throws InterruptedException {
        if (ticketNums <= 0) {
            flag = false;
            return;
        }
        Thread.sleep(100);
        System.out.println(Thread.currentThread().getName()+"拿到"+ticketNums--);
    }
}
