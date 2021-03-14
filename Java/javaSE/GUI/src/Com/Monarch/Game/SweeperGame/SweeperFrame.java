package Com.Monarch.Game.SweeperGame;

import javax.swing.*;

public class SweeperFrame extends JDialog {
    public void init(){
        loadPanel();
        setFrame();
    }

    public SweeperFrame(String title){
        setTitle(title);
    }

    public void setFrame(){
        setBounds(600,200,600,600);
        setResizable(false);
        setVisible(true);
    }
    public void loadPanel(){
        add(new SweeperPanel());
    }
}
