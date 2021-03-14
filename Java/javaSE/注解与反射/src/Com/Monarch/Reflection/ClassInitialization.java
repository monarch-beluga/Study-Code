package Com.Monarch.Reflection;

public class ClassInitialization {
    static {
        System.out.println("Main类被加载");
    }
    public static void main(String[] args) throws ClassNotFoundException {
        // 1. 主动引用
        // Son son = new Son();
        // 2. 反射
        // Class.forName("Com.Monarch.Reflection.Son");

        // 不会产生类的引用的方法
        // 1. 父类的静态域
        // System.out.println(Son.b);
        // 2. 数组
        // Son[] array = new Son[5];
        // 3. 常量
        System.out.println(Son.M);

    }
}

class Father{
    static int b = 2;

    static {
        System.out.println("父类被加载");
    }
}

class Son extends Father{
    static {
        System.out.println("子类被加载");
        m = 300;
    }
    static int m = 100;
    static final int M = 1;
}
