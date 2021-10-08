package Com.Monarch.Syn;

public class DeadLock {
    public static void main(String[] args) {
        Makeup g1 = new Makeup(0, "灰姑娘");
        Makeup g2 = new Makeup(1, "白雪公主");

        g1.start();
        g2.start();
    }
}

class Lipstick{

}
class Mirror{

}
class Makeup extends Thread{
    private static final Lipstick lipstick = new Lipstick();
    private static final Mirror mirror = new Mirror();
    int choice;
    String gir1Name;

    public Makeup(int choice, String gir1Name) {
        this.choice = choice;
        this.gir1Name = gir1Name;
    }

    @Override
    public void run() {
        try {
            makeup();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    private void makeup() throws InterruptedException {
        if (choice == 0){
            synchronized (lipstick){
                System.out.println(this.gir1Name+"获得口红的锁");
                sleep(1000);
            }
            synchronized (mirror){
                System.out.println(this.gir1Name+"获得镜子的锁");
            }
        }else {
            synchronized (mirror){
                System.out.println(this.gir1Name+"获得镜子的锁");
                sleep(2000);
            }
            synchronized (lipstick) {
                System.out.println(this.gir1Name + "获得口红的锁");
            }
        }
    }
}
