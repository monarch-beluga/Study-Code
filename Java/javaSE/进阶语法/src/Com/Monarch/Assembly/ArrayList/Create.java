package Com.Monarch.Assembly.ArrayList;

import java.util.ArrayList;

public class Create {
    public static void main(String[] args) {
        ArrayList list = new ArrayList();
        list.add("monarch");
        list.add(10);
        list.add(12.8);

        ArrayList<String> list1 = new ArrayList<>();
        list1.add("monarch");
//        list1.add(10);
        list1.add("10");
    }
}
