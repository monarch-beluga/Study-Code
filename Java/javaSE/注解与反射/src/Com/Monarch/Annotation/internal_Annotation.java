package Com.Monarch.Annotation;

import java.util.ArrayList;

public class internal_Annotation {

    //@Override     重写的注解
    @Override
    public String toString(){
        return super.toString();
    }

    //@Deprecated   不支持该方法使用
    @Deprecated
    public static void test(){
        System.out.println("Deprecated");
    }

    //@SuppressWarnings     消除系统的警告
    @SuppressWarnings("all")
    public void test02(){
        ArrayList list = new ArrayList();
    }

    public static void main(String[] args) {
        test();

    }
}
