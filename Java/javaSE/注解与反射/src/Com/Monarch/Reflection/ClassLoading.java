package Com.Monarch.Reflection;

public class ClassLoading {
    public static void main(String[] args) {
        A a = new A();
        System.out.println(A.m);


        /*
        1. 加载到内存，会产生一个类对应Class对象
        2. 链接，链接结束后 m = 0
        3. 初始化
            <clinit>(){
                        System.out.println("A类静态代码块初始化");
                        m = 300;
                        m = 100;
            }
         4. 最终 m = 100
         */
    }
}

class A{
    static {
        System.out.println("A类静态代码块初始化");
        m = 300;
    }

    static int m = 100;

    public A(){
        System.out.println("A类的无参构造初始化");
    }
}


