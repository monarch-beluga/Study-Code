package Com.Monarch.Create.RunnableInterface;

public class Create implements Runnable{
    @Override
    public void run() {
        for (int i = 0; i < 5; i++) {
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("我在看代码——"+i);
        }
    }
    public static void main(String[] args) throws InterruptedException {
        Create create = new Create();
        Thread thread = new Thread(create);
        thread.start();
        for (int i = 0; i < 5; i++) {
            Thread.sleep(100);
            System.out.println("我在学习多线程——"+i);
        }
    }
}
