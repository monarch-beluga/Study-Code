package Com.Monarch.Awts.Layouts;

import Com.Monarch.Awts.Main.MyFrame;

import java.awt.*;

public class Streaming {
    public static void main(String[] args) {
        MyFrame frame = new MyFrame(200,200,500,500, Color.white);

        // 组件->按钮
        Button button1 = new Button("button1");
        Button button2 = new Button("button2");
        Button button3 = new Button("button3");

//        frame.setLayout(new FlowLayout());
        frame.setLayout(new FlowLayout(FlowLayout.CENTER));

        frame.add(button1);
        frame.add(button2);
        frame.add(button3);
    }
}
