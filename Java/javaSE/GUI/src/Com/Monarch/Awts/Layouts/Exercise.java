package Com.Monarch.Awts.Layouts;

import Com.Monarch.Awts.Main.MyFrame;

import java.awt.*;

public class Exercise {
    public static void main(String[] args) {
        MyFrame frame = new MyFrame(200, 200, 400, 400, Color.white);

        Button[] buttons = new Button[10];
        String s;
        for (int i = 0; i < buttons.length; i++) {
            s = "button" + (i+1);
            Button button = new Button(s);
            buttons[i] = button;
        }
        Panel panel = new Panel(new BorderLayout());
        Panel panel1 = new Panel(new BorderLayout());
        frame.setLayout(new GridLayout(2,1));
        Panel panel2 = new Panel(new GridLayout(2,1));
        Panel panel3 = new Panel(new GridLayout(2,2));
        panel.add(buttons[0], BorderLayout.EAST);
        panel.add(panel2, BorderLayout.CENTER);
        panel.add(buttons[1], BorderLayout.WEST);
        panel1.add(buttons[2], BorderLayout.EAST);
        panel1.add(panel3, BorderLayout.CENTER);
        panel1.add(buttons[3], BorderLayout.WEST);
        frame.add(panel);
        frame.add(panel1);
        for (int i = 4; i < 10; i++) {
            if (i < 6)
                panel2.add(buttons[i]);
            else
                panel3.add(buttons[i]);
        }
    }
}
