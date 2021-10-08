package Com.Monarch.Awts.Frame;

import java.awt.*;

public class MyFrame extends Frame{
    static int num = 0;
    public MyFrame(int x, int y, int w, int h, Color color){
        super("MyFrame");
        setBounds(x+num*50, y+num*50, w, h);
        setBackground(color);
        setVisible(true);
        setResizable(false);
        num++;
    }
}
