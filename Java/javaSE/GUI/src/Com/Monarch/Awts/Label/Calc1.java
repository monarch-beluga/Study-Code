package Com.Monarch.Awts.Label;

import Com.Monarch.Awts.Main.MyFrame;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Calc1 {
    public static void main(String[] args) {
        new CalcFrame1().loaFrame();
    }
}
class CalcFrame1 extends MyFrame{
    public TextField textField1, textField2, textField3;
    private Label label;
    private Button button, clear;

    public void loaFrame() {
        this.setTitle("简易计算器");
        this.loaText();
        this.loaButton();
        this.loaLabel();
        this.addAction();
        this.layoutText();
    }

    public void loaText(){
        textField1 = new TextField(10);
        textField2 = new TextField(10);
        textField3 = new TextField(20);
    }

    public void loaLabel(){
        label = new Label("+");
    }

    public void loaButton(){
        button = new Button("=");
        clear = new Button("clear");
    }

    public void addAction(){
        button.addActionListener(new CalcActonListener());
        clear.addActionListener(new CalcActonListener());
    }

    public void layoutText(){
        setLayout(new FlowLayout());
        add(textField1);
        add(label);
        add(textField2);
        add(button);
        add(textField3);
        add(clear);
        pack();
    }
    public void clearText(){
        textField1.setText("");
        textField2.setText("");
        textField3.setText("");
    }
    public void calculation(){
        int n1 = Integer.parseInt(textField1.getText());
        int n2 = Integer.parseInt(textField2.getText());
        textField3.setText("" + (n1 + n2));
    }
    private class CalcActonListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            if (e.getActionCommand().equals("=")) {
                calculation();
            } else {
                clearText();
            }
        }
    }
}
