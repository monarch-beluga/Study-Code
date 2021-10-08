package Com.Monarch.Swing.JFrame;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;


public class PopupCreate {
    public static void main(String[] args) {
        new MainFrame().init();
    }
}
class MainFrame extends JFrame{
    public void init(){
        loadJFrame();
        loadJButton();
        loadContainer();
    }
    public void loadJFrame(){
        setBounds(200,200,700,500);
        setLayout(null);
        setVisible(true);
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
    }
    public void loadContainer(){
        Container container = getContentPane();
        container.setBackground(Color.white);
    }
    public void loadJButton(){
        JButton button = new JButton("点击弹出一个对话框");
        button.setFont(new Font("楷体",Font.PLAIN,15));
        button.setBounds(50,50,200,20);
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                new PopupJFrame();
            }
        });
        add(button);
    }
}
class PopupJFrame extends JDialog{
    public PopupJFrame() {
        loadFrame();
        loadJLabel();
        loadContainer();
    }
    public void loadContainer(){
        Container container = getContentPane();
        container.setBackground(Color.green);
    }
    public void loadFrame(){
        this.setVisible(true);
        this.setBounds(300,300,300,300);
    }
    public void loadJLabel(){
        JLabel label = new JLabel("这是一个弹窗");
        label.setFont(new Font("楷体",Font.PLAIN,15));
        label.setHorizontalAlignment(SwingConstants.CENTER);
        add(label);
    }
}

