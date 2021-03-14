package Com.Monarch.Swing.AddIcon;

import javax.swing.*;
import java.awt.*;
import java.net.URL;

public class ImageIconLabel {
    public static void main(String[] args) {
        new ImageFrame("图片图标").init();
    }
}
class ImageFrame extends JFrame{
    public void init(){
        loadLabel();
        loadJFrame();
        loadContainer();
    }
    public ImageFrame(String title){
        super(title);
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
    public void loadLabel(){
        URL url = ImageIconLabel.class.getResource("Monarch.jpg");
        ImageIcon imageIcon = new ImageIcon(url);
        JLabel label = new JLabel("Monarch",imageIcon,SwingConstants.CENTER);
        add(label);
    }
}