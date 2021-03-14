package Com.Monarch.Swing.List;

import javax.swing.*;
import java.awt.*;
import java.util.Vector;

public class TestJList {
    public static void main(String[] args) {
        new JListFrame("列表框").init();
    }
}
class JListFrame extends JFrame{
    public JListFrame(String title) throws HeadlessException {
        super(title);
    }

    public void init(){
        loadJList();
        loadJList1();
        loadJFrame();
        loadContainer();
    }
    public void loadJFrame(){
        setBounds(200,200,400,400);
        this.setVisible(true);
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
    }
    public void loadContainer(){
        Container container = getContentPane();
        container.setBackground(Color.white);
    }
    public void loadJList(){
        setLayout(null);

        String[] contents = {"1", "2", "3", "4", "5", "6"};
        JList<String> jList = new JList<>(contents);
        jList.setBounds(5,5,290,55);
        jList.setVisibleRowCount(3);
        jList.setLayoutOrientation(JList.VERTICAL_WRAP);
        jList.setFixedCellWidth(145);

        JPanel panel = new JPanel(null);
        panel.setBounds(10,10,300,65);
        panel.add(jList);
        panel.setBackground(Color.lightGray);
        add(panel);
    }
    public void loadJList1(){
        Vector<String> contents = new Vector<>();
        JList<String> jList = new JList<>(contents);
        contents.add("张三");
        contents.add("李四");
        contents.add("王五");
        jList.setBounds(5,5,290,55);

        JPanel panel = new JPanel(null);
        panel.setBounds(10,200,300,65);
        panel.add(jList);
        panel.setBackground(new Color(0x42423D));
        add(panel);
    }
}