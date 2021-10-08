package Com.Monarch.Awts.Layouts;

import Com.Monarch.Awts.Main.MyFrame;

import java.awt.*;

public class Exercise1 {
    public static void main(String[] args) {
        MyFrame frame = new MyFrame(200, 200, 600, 400, Color.white);

        Button[] buttons = new Button[10];
        String s;
        for (int i = 0; i < buttons.length; i++) {
            s = "button" + (i+1);
            Button button = new Button(s);
            buttons[i] = button;
        }
        frame.setLayout(null);
        Panel panel = new Panel(new GridLayout(2,0));
        Panel panel1 = new Panel(new GridLayout(2,0));
        Panel panel2 = new Panel(new GridLayout(2,0));
        Panel panel3 = new Panel(new GridLayout(2,0));
        Panel panel4 = new Panel(new GridLayout(2,0));
        panel.setBounds(0,30,100, 370);
        panel1.setBounds(500,30,100, 370);
        panel2.setBounds(100,30,400, 370);
        frame.add(panel);
        frame.add(panel1);
        frame.add(panel2);
        panel.add(buttons[0]);
        panel.add(buttons[1]);
        panel1.add(buttons[2]);
        panel1.add(buttons[3]);
        panel2.add(panel3);
        panel2.add(panel4);
        panel3.add(buttons[4]);
        panel3.add(buttons[5]);
        for (int i = 6; i < 10; i++) {
            panel4.add(buttons[i]);
        }
    }
}
