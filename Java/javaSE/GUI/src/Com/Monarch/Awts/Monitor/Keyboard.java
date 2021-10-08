package Com.Monarch.Awts.Monitor;

import Com.Monarch.Awts.Main.MyFrame;

import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class Keyboard {
    public static void main(String[] args) {
        new KeyboardFrame().loadFrame();
    }
}

class KeyboardFrame extends MyFrame {
    public void loadFrame(){

        this.addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                if (e.getKeyChar() == 'w' || e.getKeyCode() == KeyEvent.VK_UP){
                    System.out.println("你按下了上键");
                }
            }
        });
    }
}
