package Com.Monarch.Status;

public class Stop {
    public static void main(String[] args) {
        StopRunner runner = new StopRunner();
        new Thread(runner).start();
        for (int i = 0; i < 1000; i++) {
            System.out.println("main....."+i);
            if (i == 900){
                runner.stop();
                System.out.println("线程该停止了");
            }
        }

    }
}

class StopRunner implements Runnable{
    private boolean flag = true;

    @Override
    public void run() {
        int i = 0;
        while (flag)
            System.out.println("run......Thread"+i++);
    }
    public void stop(){
        this.flag = false;
    }
}
