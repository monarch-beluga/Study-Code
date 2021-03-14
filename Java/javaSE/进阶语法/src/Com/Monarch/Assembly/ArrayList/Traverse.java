package Com.Monarch.Assembly.ArrayList;

import java.util.ArrayList;
import java.util.Iterator;

public class Traverse {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("monarch");
        list.add("15");
        list.add("男");
        list.add("2001");
        for (int i = 0; i < list.size(); i++) {
            System.out.println(list.get(i));
        }
        System.out.println("================");
        for (String s : list) {
            System.out.println(s);
        }
        System.out.println("================");
        Iterator<String> it = list.iterator();
        System.out.println(it.next());
        System.out.println(it.next());
        System.out.println(it.next());
        System.out.println(it.next());
        System.out.println(it.hasNext());
        System.out.println("================");
        while (it.hasNext()){
            System.out.println(it.next());
        }
        System.out.println("================");
        Iterator<String> it1 = list.iterator();
        while (it1.hasNext()){
            System.out.println(it1.next());
        }
    }
}
