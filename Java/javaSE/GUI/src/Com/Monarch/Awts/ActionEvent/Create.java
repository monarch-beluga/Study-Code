package Com.Monarch.Awts.ActionEvent;

import Com.Monarch.Awts.Main.MyFrame;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Create {
    public static void main(String[] args) {
        MyFrame frame = new MyFrame();
        Button button = new Button("exit");
        Printf printf = new Printf();
        frame.setLayout(new FlowLayout(FlowLayout.CENTER));
        button.addActionListener(printf);
        frame.add(button);
    }
}

class Printf implements ActionListener{
    @Override
    public void actionPerformed(ActionEvent e) {
        for (int i = 3; i >= 0; i--){
            System.out.println("程序将在："+i+"秒后关闭");
            try {
                Thread.sleep(1000);
            } catch (InterruptedException interruptedException) {
                interruptedException.printStackTrace();
            }
        }
        System.exit(0);
    }
}
