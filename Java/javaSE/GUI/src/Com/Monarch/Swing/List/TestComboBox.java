package Com.Monarch.Swing.List;

import javax.swing.*;
import java.awt.*;

public class TestComboBox {
    public static void main(String[] args) {
        new ComboBoxFrame("下拉框").init();
    }
}
class ComboBoxFrame extends JFrame {
    public ComboBoxFrame(String title){
        super(title);
    }

    public void init(){
        loadJComboBox();
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
    public void loadJComboBox(){
        setLayout(null);
        JPanel panel = new JPanel();
        JComboBox<String> status = new JComboBox<>();
        status.setBackground(new Color(239, 239, 124));
        status.addItem(null);
        status.addItem("正在热映");
        status.addItem("已下架");
        status.addItem("即将上映");
        panel.add(status,BorderLayout.CENTER);
        panel.setBounds(150,150,80,30);
        panel.setBackground(new Color(239, 239, 124));
        add(panel);
    }
}