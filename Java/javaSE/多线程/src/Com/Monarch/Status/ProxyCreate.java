package Com.Monarch.Status;

public class ProxyCreate {
    public static void main(String[] args) {
        PYou you = new PYou();
        WeddingCompany company = new WeddingCompany(you);
        company.HappyMarry();
    }
}

interface Marry{
    void HappyMarry();
}
class PYou implements Marry{
    @Override
    public void HappyMarry() {
        System.out.println("Monarch要结婚了,超开心");
    }
}
class WeddingCompany implements Marry{
    private Marry target;

    public WeddingCompany(Marry target) {
        this.target = target;
    }

    @Override
    public void HappyMarry() {
        after();
        this.target.HappyMarry();
        before();
    }
    private void after(){
        System.out.println("结婚之前,布置现场");
    }
    private void before(){
        System.out.println("结婚之后,收尾款");
    }
}