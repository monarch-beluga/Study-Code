package Com.Monarch.Swing.Panel;

import javax.swing.*;
import java.awt.*;

public class ScrollPanel {
    public static void main(String[] args) {
        new ScrollFrame("文本域").init();
    }
}

class ScrollFrame extends JFrame{
    private JTextArea textArea;
    public ScrollFrame(String title) throws HeadlessException {
        super(title);
    }

    public void init(){
        loadJFrame();
        loadTextArea();
        loadScrollPanel();
        loadContainer();
        setVisible(true);
    }
    public void loadJFrame(){
        setBounds(200,200,400,400);
        setLayout(new FlowLayout(FlowLayout.CENTER, 50,100));
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
    }
    public void loadContainer(){
        Container container = getContentPane();
        container.setBackground(Color.blue);
    }
    public void loadScrollPanel(){
        JScrollPane scrollPane = new JScrollPane(textArea);
        add(scrollPane);
    }
    public void loadTextArea(){
        textArea = new JTextArea(5,30);
        textArea.setText("欢迎学习java!");
        textArea.setFont(new Font("楷体",Font.PLAIN,15));
    }
}
