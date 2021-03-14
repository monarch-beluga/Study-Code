package Com.Monarch.Reflection;

import java.lang.annotation.*;
import java.lang.reflect.Field;

public class AnnotationReflection {
    public static void main(String[] args) throws ClassNotFoundException, NoSuchFieldException {
        Class c1 = Class.forName("Com.Monarch.Reflection.Student2");

        // 通过反射获得注解
        Annotation[] annotations = c1.getAnnotations();     // 获得注解
        for (Annotation annotation : annotations) {
            System.out.println(annotation);
            /*@Com.Monarch.Reflection.TableMonarch(value=db_student)*/
        }

        // 获得注解的value的值
        TableMonarch tableMonarch = (TableMonarch) c1.getAnnotation(TableMonarch.class);
        String value = tableMonarch.value();
        System.out.println(value);  /*db_student*/

        // 获取指定类的注解
        Field f = c1.getDeclaredField("name");
        FieldMonarch annotation = f.getAnnotation(FieldMonarch.class);
        System.out.println(annotation.columnName());    /*db_name*/
        System.out.println(annotation.type());          /*varchar*/
        System.out.println(annotation.length());        /*3*/

    }
}

@TableMonarch("db_student")
class Student2{

    @FieldMonarch(columnName = "db_id", type = "int", length = 10)
    private int id;
    @FieldMonarch(columnName = "db_age", type = "int", length = 10)
    private int age;
    @FieldMonarch(columnName = "db_name", type = "varchar", length = 3)
    private String name;

    public Student2() {
    }

    public Student2(int id, int age, String name) {
        this.id = id;
        this.age = age;
        this.name = name;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}

// 类名的注解
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@interface TableMonarch{
    String value();
}

// 属性的注解
@Target(ElementType.FIELD)
@Retention(RetentionPolicy.RUNTIME)
@interface FieldMonarch{
    String columnName();
    String type();
    int length();
}