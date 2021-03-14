package Com.Monarch.Create.RunnableInterface;

public class Race {
    public static void main(String[] args) {
        RaceRunner runner = new RaceRunner();
        new Thread(runner, "乌龟").start();
        new Thread(runner, "兔子").start();

    }
}

class RaceRunner implements Runnable{
    private String winner;

    @Override
    public void run() {
        for (int i = 0; i <= 100;) {
            System.out.println(Thread.currentThread().getName()+"——>跑了"+i+"步");
            if (Thread.currentThread().getName().equals("乌龟"))
                i++;
            else{
                i += 5;
                if (i > 80) {
                    try {
                        Thread.sleep(100);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
            if (gameOver(i))
                break;
        }
    }
    private boolean gameOver (int steps){
        if (winner != null)
            return true;
        if (steps >= 100){
            winner = Thread.currentThread().getName();
            System.out.println("winner is "+winner);
            return true;
        }
        return false;
    }
}
