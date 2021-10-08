package Com.Monarch.Swing.JFrame;

import javax.swing.*;
import java.awt.*;

public class Create {

    public static void main(String[] args) {
        new CreateJFrame().init();
    }
}
class CreateJFrame extends JFrame{
    Container container;
    public void init(){
        loadJFrame();
        loadLabel();
        loadContainer();
    }
    public void loadJFrame(){
        setBounds(200,200,400,400);
        setVisible(true);
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
    }
    public void loadLabel(){
        JLabel label = new JLabel("你好，世界");
        label.setFont(new Font("楷体",Font.BOLD,15));
        label.setForeground(Color.CYAN);
        label.setHorizontalAlignment(SwingConstants.CENTER);
        add(label);
    }
    public void loadContainer(){
        container = getContentPane();
        container.setBackground(Color.blue);
    }
}
