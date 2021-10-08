package Com.Monarch.Lambda;

public class TestLambda {
    public static void main(String[] args) {
        ILove love = new Love();
        love.love(1);
        love = a -> {
            love1(a);
            love1(a);
        };
        love.love(2);
    }
    static public void love1(int a) {
        System.out.println("I love you——>"+a);
    }
}

interface ILove{
    void love(int a);
}

class Love implements ILove{

    @Override
    public void love(int a) {
        System.out.println("I love you——>"+a);
    }
}