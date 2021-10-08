package Com.Monarch.Awts.Layouts;

import Com.Monarch.Awts.Main.MyFrame;

import java.awt.*;

public class Surround {
    public static void main(String[] args) {
        MyFrame frame = new MyFrame(200,200,500,500, Color.white);

        // 组件->按钮
        Button east = new Button("East");
        Button west = new Button("West");
        Button south = new Button("South");
        Button north = new Button("North");
        Button center = new Button("Center");

        frame.setLayout(new BorderLayout());
        frame.add(east, BorderLayout.EAST);
        frame.add(west, BorderLayout.WEST);
        frame.add(south, BorderLayout.SOUTH);
        frame.add(north, BorderLayout.NORTH);
        frame.add(center, BorderLayout.CENTER);
    }
}
