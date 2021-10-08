package Com.Monarch.Awts.TextField;

import Com.Monarch.Awts.Main.MyFrame;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Create {
    public static void main(String[] args) {
        new MyFramePassword();
        new MyFrameInput();
    }
}
class MyFrameInput extends MyFrame {
    public MyFrameInput() {
        super("输入框");
        MyTextField textField = new MyTextField();
        setLayout(null);
        add(textField);

        MyActionListenerText actionListenerText = new MyActionListenerText();
        textField.addActionListener(actionListenerText);
    }
}
class MyTextField extends TextField{
    public MyTextField() throws HeadlessException {
        setBounds(50,50,300,50);
    }
}
class MyFramePassword extends MyFrame{
    public MyFramePassword() {
        super("密码框");
        MyTextField textField = new MyTextField();
        textField.setEchoChar('*');
        setLayout(null);
        add(textField);

        MyActionListenerText actionListenerText = new MyActionListenerText();
        textField.addActionListener(actionListenerText);
    }
}
class MyActionListenerText implements ActionListener{

    @Override
    public void actionPerformed(ActionEvent e) {
        TextField field = (TextField) e.getSource();
        System.out.println(field.getText());
        field.setText("");
    }
}