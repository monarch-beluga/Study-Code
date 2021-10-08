package Com.Monarch.Assembly.ArrayList;

import java.util.ArrayList;

public class Method {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("monarch");
        list.add("15");
        list.add("男");
        System.out.println("第零个元素是："+list.get(0));
        System.out.println("第一个元素是："+list.get(1));
        list.add(1, "2001");
        System.out.println("第一个元素是："+list.get(1));
        System.out.println("第二个元素是："+list.get(2));
        System.out.println("第三个元素是："+list.get(3));
        String s = list.set(2,"19");
        System.out.println("修改前的元素是："+s);
        System.out.println("修改后的元素是："+list.get(2));
        System.out.println("删除前的第一个元素是："+list.get(1));
        list.remove(1);
        System.out.println("删除后的第一个元素是："+list.get(1));
        System.out.println("list中的元素个数为："+list.size());
        System.out.println("list中是否存在19："+list.contains("19"));
        System.out.println("list中是否存在2001："+list.contains("2001"));
        list.remove("19");
        System.out.println("list中是否存在19："+list.contains("19"));
    }
}
