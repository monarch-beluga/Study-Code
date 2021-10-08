package Com.Monarch.Reflection;

import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

public class CreateClass {
    public static void main(String[] args) throws ClassNotFoundException, IllegalAccessException, InstantiationException, NoSuchMethodException, InvocationTargetException, NoSuchFieldException {
        // 获取class对象
        Class c1 = Class.forName("Com.Monarch.Reflection.User");

        // 构造一个对象
        User user = (User)c1.newInstance();     // 本质上是调用无参构造器
        System.out.println(user);           /*User{name='null', id=0, age=0}*/

        // 通过构造器创建对象
        Constructor constructor = c1.getDeclaredConstructor(String.class, int.class, int.class);
        User user2 = (User) constructor.newInstance("白鲸", 666, 19);
        System.out.println(user2);          /*User{name='白鲸', id=666, age=19}*/

        // 通过反射来调用方法
        Method setName = c1.getMethod("setName", String.class);     // 获取方法
        setName.invoke(user, "monarch");            // 激活方法，传递参数
        System.out.println(user.getName());         /*monarch*/

        // 通过反射操作属性
        Field name = c1.getDeclaredField("name");

        name.setAccessible(true);       // 关闭程序安全检查
        name.set(user, "寒江雪");          /*报错，name为private*/
        System.out.println(user.getName());     /*寒江雪*/
    }
}
