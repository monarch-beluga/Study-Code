package Com.Monarch.Awts.Paint;

import Com.Monarch.Awts.Main.MyFrame;

import java.awt.*;

public class CreatePaint {
    public static void main(String[] args) {
        new CreateFrame().loadFrame();
    }
}

class CreateFrame extends MyFrame{
    private int num, flag;
    public void loadFrame(){
        setTitle("画笔");
        setBounds(200,200,600,400);
    }
    @Override
    public void paint(Graphics g) {
        g.setColor(Color.blue);
        g.drawOval(num*5,100,100,100);
        g.setColor(Color.red);
        repaint();
        g.fillOval(100,250,100,100);
        g.setColor(Color.green);
        g.fillRect(200,150,200,200);
        if (num*5 == 500)
            flag = 1;
        if (num*5 == 0)
            flag = 0;
        try {
            Thread.sleep(40);
            if (flag == 0)
                num++;
            else
                num--;
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

