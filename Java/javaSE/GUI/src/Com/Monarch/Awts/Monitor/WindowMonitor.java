package Com.Monarch.Awts.Monitor;

import Com.Monarch.Awts.Main.MyFrame;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class WindowMonitor {
    public static void main(String[] args) {
        new MyWindowFrame("window").loadFrame();
    }
}
class MyWindowFrame extends MyFrame{
    private Button button1, button2;
    MyWindowFrame frame2;
    String name;
    public MyWindowFrame(String s) {
        super(s);
        name = s;
    }
    public void loadFrame(){
        frame2 = new MyWindowFrame(name+"副窗口");
        this.loadButton();
        this.addButton();
        setVisible(true);
        windowClose(this);
    }
    public void loadButton(){
        button1 = new Button("Open secondary window");
        button2 = new Button("Close secondary window");
        WindowAction windowAction = new WindowAction();
        button1.addActionListener(windowAction);
        button2.addActionListener(windowAction);
        button1.setActionCommand("start");
        button2.setActionCommand("stop");
    }
    public void addButton(){
        setLayout(new FlowLayout(FlowLayout.CENTER));
        add(button1);
        add(button2);
    }
    @Override
    public void windowClose() {
        this.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                dispose();
            }

            @Override
            public void windowActivated(WindowEvent e) {
                System.out.println("窗口被激活");
            }
        });
    }
    class WindowAction implements ActionListener{

        @Override
        public void actionPerformed(ActionEvent e) {
            frame2.setVisible(e.getActionCommand().equals("start"));
        }
    }
}