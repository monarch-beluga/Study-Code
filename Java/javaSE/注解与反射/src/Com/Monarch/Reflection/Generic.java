package Com.Monarch.Reflection;

import java.lang.reflect.Method;
import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;
import java.util.List;
import java.util.Map;

public class Generic {
    public void test1(Map<String, User> map, List<User> list){
        System.out.println("test1");
    }

    public Map<String, User> test2(){
        System.out.println("test2");
        return null;
    }

    public static void main(String[] args) throws NoSuchMethodException {
        Method method = Generic.class.getMethod("test1", Map.class, List.class);        // 获取方法

        Type[] genericParameterTypes = method.getGenericParameterTypes();               // 获取形参类型
        for (Type genericParameterType : genericParameterTypes) {                       // 遍历输出形参类型
            System.out.println("#" + genericParameterType);
            if (genericParameterType instanceof ParameterizedType){                     // 判断是否为参数化类型ParameterizedType或其子类
                Type[] actualTypeArguments = ((ParameterizedType) genericParameterType).getActualTypeArguments();       // 强制转换为ParameterizedType并获取其实际类型的数组
                for (Type actualTypeArgument : actualTypeArguments) {                   // 遍历输出实际参数类型
                    System.out.println(actualTypeArgument);
                }
            }
        }

        System.out.println("================");
        method = Generic.class.getMethod("test2", null);
        Type genericReturnType = method.getGenericReturnType();             // 获取返回值类型

        if (genericReturnType instanceof ParameterizedType){
            Type[] actualTypeArguments = ((ParameterizedType) genericReturnType).getActualTypeArguments();
            for (Type actualTypeArgument : actualTypeArguments) {
                System.out.println(actualTypeArgument);
            }
        }else{
            System.out.println("#" + genericReturnType);
        }
    }
}
