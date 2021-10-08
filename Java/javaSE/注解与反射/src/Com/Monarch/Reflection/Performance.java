package Com.Monarch.Reflection;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

public class Performance {

    // 普通方式调用
    static public void test1(){
        User user = new User();

        long startTime = System.currentTimeMillis();

        for (int i = 0; i < 1000000000; i++) {
            user.getName();
        }

        long endTime = System.currentTimeMillis();

        System.out.println("普通方式执行10亿次:"+(endTime-startTime)+"mg");
    }

    // 反射方式调用
    static public void test2() throws ClassNotFoundException, NoSuchMethodException, IllegalAccessException, InstantiationException, InvocationTargetException {
        Class c1 = Class.forName("Com.Monarch.Reflection.User");
        User user = (User)c1.newInstance();
        Method getName = c1.getDeclaredMethod("getName", null);

        long startTime = System.currentTimeMillis();

        for (int i = 0; i < 1000000000; i++) {
            getName.invoke(user, null);
        }

        long endTime = System.currentTimeMillis();

        System.out.println("反射方式执行10亿次:"+(endTime-startTime)+"mg");
    }

    // 反射方式调用 关闭检测
    static public void test3() throws ClassNotFoundException, NoSuchMethodException, IllegalAccessException, InstantiationException, InvocationTargetException {
        Class c1 = Class.forName("Com.Monarch.Reflection.User");
        User user = (User)c1.newInstance();
        Method getName = c1.getDeclaredMethod("getName", null);
        getName.setAccessible(true);

        long startTime = System.currentTimeMillis();    // 获取时间

        for (int i = 0; i < 1000000000; i++) {
            getName.invoke(user, null);
        }

        long endTime = System.currentTimeMillis();

        System.out.println("关闭性能检测执行10亿次:"+(endTime-startTime)+"mg");
    }

    public static void main(String[] args) throws ClassNotFoundException, NoSuchMethodException, InvocationTargetException, InstantiationException, IllegalAccessException {
        test1();
        test2();
        test3();
    }
}
