package Com.Monarch.Cooperation;

public class TestPC {
    public static void main(String[] args) {
        SynContainer container = new SynContainer();

        new Producer(container).start();
        new Consumer(container).start();
    }
}

class Producer extends Thread{
    private final SynContainer container;

    public Producer(SynContainer container) {
        this.container = container;
    }

    @Override
    public void run() {
        for (int i = 0; i < 100; i++) {
            container.push(new Chicken(i));
            System.out.println("生产了"+i+"只鸡");
        }
    }
}
class Consumer extends Thread{
    private final SynContainer container;

    public Consumer(SynContainer container) {
        this.container = container;
    }

    @Override
    public void run() {
        for (int i = 0; i < 100; i++) {
            System.out.println("消费了"+container.pop().id+"只鸡");
        }
    }
}

class Chicken{
    public final int id;

    public Chicken(int id) {
        this.id = id;
    }
}

class SynContainer{
    private final Chicken[] chickens = new Chicken[10];
    private int count = 0;

    public synchronized void push(Chicken chicken){
        if (count == chickens.length){
            try {
                this.wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        chickens[count] = chicken;
        count++;
        this.notify();
    }

    public synchronized Chicken pop(){
        if (count == 0){
            try {
                this.wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        count--;
        Chicken chicken = chickens[count];
        this.notify();

        return chicken;
    }
}
