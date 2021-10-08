package Com.Monarch.Swing.Button;

import javax.swing.*;
import java.awt.*;

public class SingleChoice {
    public static void main(String[] args) {
        new SingleFrame("单选按钮").init();
    }
}
class SingleFrame extends JFrame{
    public void init(){
        loadJRadioButton();
        loadJFrame();
        loadContainer();
    }
    public SingleFrame(String title){
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
    public void loadJRadioButton(){
        setLayout(new FlowLayout(FlowLayout.CENTER, 150, 50));
        ButtonGroup group = new ButtonGroup();
        JRadioButton[] radioButtons = new JRadioButton[3];
        for (int i=0; i < radioButtons.length; i++){
            radioButtons[i] = new JRadioButton("JRadioButton" + (i+1));
            group.add(radioButtons[i]);
            add(radioButtons[i]);
        }
    }
}
