package Com.Monarch.Game.GreedySnake;

import javax.swing.*;

public class SnakeFrame extends JFrame {
    public static void main(String[] args){
        new SnakeFrame("贪吃蛇小游戏").init();
    }
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
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
    }
    public void loadPanel(){
        add(new SnakePanel());
    }
}
