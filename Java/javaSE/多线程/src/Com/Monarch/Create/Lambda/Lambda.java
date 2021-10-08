package Com.Monarch.Create.Lambda;

public class Lambda {
    public static void main(String[] args) {
        ILike like = new Like();
        like.lambda();

        like = new Like2();
        like.lambda();

        // 局部内部类
        class Like3 implements ILike{

            @Override
            public void lambda() {
                System.out.println("I like lambda3");
            }
        }
        like = new Like3();
        like.lambda();

        // 匿名内部类
        like = new ILike() {
            @Override
            public void lambda() {
                System.out.println("I like lambda4");
            }
        };
        like.lambda();

        // Lambda表达式
        like = () -> {
            System.out.println("I like lambda5");
        };
        like.lambda();
    }
    // 静态内部类
    static class Like2 implements ILike{

        @Override
        public void lambda() {
            System.out.println("I like lambda2");
        }
    }
}

interface ILike{
    void lambda();
}
// 实现类
class Like implements ILike{

    @Override
    public void lambda() {
        System.out.println("I like lambda1");
    }
}