package Com.Monarch.Awts.Main;

import java.awt.*;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class MyFrame extends Frame {
    static int num = 0;

    public MyFrame(){
        super("MyFrame");
        setBounds(200+num*50, 200+num*50, 400, 400);
        setBackground(Color.white);
        setVisible(true);
        windowClose();
        num++;
    }
    public MyFrame(String s){
        super(s);
        setBounds(200+num*50, 200+num*50, 400, 400);
        setBackground(Color.white);
        setVisible(true);
        windowClose();
        num++;
    }

    public MyFrame(int x, int y, int w, int h, Color color){
        super("MyFrame");
        setBounds(x+num*50, y+num*50, w, h);
        setBackground(color);
        setVisible(true);
        windowClose();
        num++;
    }
    public void windowClose(){
        this.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                System.exit(0);
            }
        });
    }
    public void windowClose(Frame frame){
        frame.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                System.exit(0);
            }
        });
    }
}
