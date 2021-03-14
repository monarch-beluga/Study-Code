package Com.Monarch.Game.GreedySnake;

import javax.swing.*;

public class SnakeFrame extends JDialog {
    public void init(){
        loadPanel();
        setFrame();
    }

    public SnakeFrame(String title){
        setTitle(title);
    }

    public void setFrame(){
        setBounds(200,100,1005,820);
        setResizable(false);
        setVisible(true);
    }
    public void loadPanel(){
        add(new SnakePanel());
    }
}
