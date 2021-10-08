package Com.Monarch.Game;

import Com.Monarch.Game.GreedySnake.SnakeFrame;
import Com.Monarch.Game.SweeperGame.SweeperFrame;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class appFrame extends JFrame {
    AppActionListener actionListener = new AppActionListener();
    public void init(){
        setJButton();
        setFrame();
    }

    public appFrame(String title) throws HeadlessException {
        super(title);
    }

    public void setFrame(){
        setBounds(200,100,400,400);
        setVisible(true);
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
    }
    public void loadJButton(String s){
        JButton button = new JButton(s);
        button.setFont(new Font("楷体", Font.BOLD, 20));
        button.addActionListener(actionListener);
        add(button);
    }
    public void setJButton(){
        setLayout(new FlowLayout(FlowLayout.CENTER, 200, 50));
        loadJButton("贪吃蛇");
        loadJButton("扫雷");
    }
    static class AppActionListener implements ActionListener{
        @Override
        public void actionPerformed(ActionEvent e) {
            if (e.getActionCommand().equals("贪吃蛇")){
                new SnakeFrame("贪吃蛇小游戏").init();
            }else if (e.getActionCommand().equals("扫雷")){
                new SweeperFrame("扫雷小游戏").init();
            }
        }
    }
}
