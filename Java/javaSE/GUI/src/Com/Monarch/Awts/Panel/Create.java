package Com.Monarch.Awts.Panel;

import Com.Monarch.Awts.Frame.MyFrame;

import java.awt.*;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class Create {
    public static void main(String[] args) {
        MyFrame myFrame = new MyFrame(200, 200, 500,500, Color.white);
        Panel panel = new Panel();

        myFrame.setLayout(null);

        panel.setBounds(50, 50,400, 400);
        panel.setBackground(new Color(116, 104, 104));

        myFrame.add(panel);

        // 监听窗口关闭事件
        myFrame.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                // 结束程序
                System.exit(0);
            }
        });
    }
}
