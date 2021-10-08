package Com.Monarch.Annotation;

import java.lang.annotation.*;

@MyAnnotation
public class Meta_annotation {
    @MyAnnotation
    public void test(){

    }
}

// 定义注解作用的地方
@Target(value = {ElementType.METHOD, ElementType.TYPE})

// 表示注解在什么的方还有效，SOURCES表示源码，CLASS表示class文件，RUNTIME表示运行时有效
// 作用范围(SOURCE < CLASS < RUNTIME)
@Retention(value = RetentionPolicy.RUNTIME)

// 表示是否将我们的注解生成在JAVAdoc中
@Documented

// 子类可以继承父类中的注解
@Inherited
@interface MyAnnotation{

}

