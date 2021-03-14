package Com.Monarch.Swing.AddIcon;

import javax.swing.*;
import java.awt.*;

public class IconLabels {
    public static void main(String[] args) {
        new IconFrame("绘制图标").init();
    }
}
class IconFrame extends JFrame{
    public void init(){
        loadLabel();
        loadJFrame();
        loadContainer();
    }

    public IconFrame(String title){
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
        IconLabel iconLabel = new IconLabel(20,20);
        JLabel label = new JLabel("IconLabel",iconLabel,SwingConstants.CENTER);
        add(label);
    }
}
class IconLabel implements Icon{
    private final int width, height;

    public IconLabel(int width, int height){
        this.width = width;
        this.height = height;
    }

    @Override
    public void paintIcon(Component c, Graphics g, int x, int y) {
        int w = width/2;
        int h = width/2;
        g.setColor(Color.red);
        g.fillOval(x,y,width,height);
        g.setColor(Color.white);
        g.fillRect(x+w/2,y+w/2,w,h);
    }

    @Override
    public int getIconWidth() {
        return this.width;
    }

    @Override
    public int getIconHeight() {
        return this.height;
    }
}
