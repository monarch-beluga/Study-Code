package Com.Monarch.Annotation;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

public class customize {
    @MyAnnotation2(name = "白鲸")
    public void test(){

    }

    @MyAnnotation3("白鲸")
    public void test2(){

    }
}

@Target({ElementType.METHOD, ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
@interface MyAnnotation2{
    String name();
    int age() default 0;    // default设置默认值
    int id() default -1;    // 如果默认值为-1，代表不存在

    String[] schools() default {"致远科研", "九江学院"};
}

@Target({ElementType.METHOD, ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
@interface MyAnnotation3{
    String value();     // 如果只有一个参数，默认参数名为value
}