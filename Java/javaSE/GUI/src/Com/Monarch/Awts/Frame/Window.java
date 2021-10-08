package Com.Monarch.Awts.Frame;

import java.awt.*;

public class Window {
    static int num = 0;
    public static void main(String[] args) {
        Window window = new Window();
        for (int i = 0; i < 3; i++) {
            window.newframe();
        }
    }
    public void newframe(){
        Frame frame = new Frame("我的第一个java图形界面窗口");
//        frame.setTitle("我的java图形界面");
        frame.setVisible(true);
        frame.setSize(400,400);
        frame.setBackground(new Color(245, 241, 241));
        frame.setLocation(200+num*50,200+num*50);
        frame.setResizable(false);
        num++;
    }
}
