package Com.Monarch.Awts.ActionEvent;

import Com.Monarch.Awts.Main.MyFrame;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Create1 {
    public static void main(String[] args) {
        MyFrame frame = new MyFrame("开始-停止");
        Button button1 = new Button("start");
        Button button2 = new Button("stop");

        button2.setActionCommand("button2-stop");

        StartStop startStop = new StartStop();
        button1.addActionListener(startStop);
        button2.addActionListener(startStop);

        frame.setLayout(new FlowLayout());
        frame.add(button1);
        frame.add(button2);
    }
}
class StartStop implements ActionListener {

    @Override
    public void actionPerformed(ActionEvent e) {
        System.out.println("按钮被点击了："+e.getActionCommand());
    }
}