package Com.Monarch.Awts.Layouts;

import Com.Monarch.Awts.Main.MyFrame;

import java.awt.*;

public class Form {
    public static void main(String[] args) {
        MyFrame frame = new MyFrame(200,200,500,500, Color.white);

        // 组件->按钮
        Button btn1 = new Button("btn1");
        Button btn2 = new Button("btn2");
        Button btn3 = new Button("btn3");
        Button btn4 = new Button("btn4");
        Button btn5 = new Button("btn5");
        Button btn6 = new Button("btn6");

        frame.setLayout(new GridLayout(2, 3));

        frame.add(btn1);
        frame.add(btn2);
        frame.add(btn3);
        frame.add(btn4);
        frame.add(btn5);
        frame.add(btn6);

        // frame.pack();
    }
}
