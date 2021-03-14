package Com.Monarch.Swing.Button;

import javax.swing.*;
import java.awt.*;
import java.net.URL;

public class ImageButton {
    public static void main(String[] args) {
        new ImageButtonJFrame("图片按钮").init();
    }
}
class ImageButtonJFrame extends JFrame{
    public ImageButtonJFrame(String title){
        super(title);
    }

    public void init(){
        loadButton();
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
    public void loadButton(){
        setLayout(null);
        URL url = ImageButton.class.getResource("bai.jpg");
        Icon imageIcon = new ImageIcon(url);
        JButton button = new JButton();
        button.setIcon(imageIcon);
        button.setToolTipText("这是一个图片按钮");
        button.setBounds(150,120,100,100);
        add(button);
    }
}