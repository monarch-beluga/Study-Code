package Com.Monarch.Awts.Label;

import Com.Monarch.Awts.Main.MyFrame;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Calc {
    public static void main(String[] args) {
        new CalcFrame().loaFrame();
    }
}
class CalcFrame extends MyFrame{
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
        button.addActionListener(new CalcActonListener(this));
        clear.addActionListener(new CalcActonListener(this));
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
}

class CalcActonListener implements ActionListener {
    // 类的组合
    private CalcFrame frame = null;
    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getActionCommand().equals("=")) {
            calculation();
        }else {
            clearText();
        }
    }

    public CalcActonListener(CalcFrame frame) {
        this.frame = frame;
    }
    private void clearText(){
        frame.textField1.setText("");
        frame.textField2.setText("");
        frame.textField3.setText("");
    }
    private void calculation(){
        int n1 = Integer.parseInt(frame.textField1.getText());
        int n2 = Integer.parseInt(frame.textField2.getText());
        frame.textField3.setText("" + (n1 + n2));
    }
}
