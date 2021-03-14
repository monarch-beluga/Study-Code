package Com.Monarch.Swing.Button;

import javax.swing.*;
import java.awt.*;

public class Check {
    public static void main(String[] args) {
        new CheckFrame("多选按钮").init();
    }
}
class CheckFrame extends SingleFrame {
    public CheckFrame(String title) {
        super(title);
    }
    public void loadJCheckBox(){
        setLayout(new FlowLayout(FlowLayout.CENTER, 150, 50));
        JCheckBox checkBox1 = new JCheckBox("JCheckBox1");
        JCheckBox checkBox2 = new JCheckBox("JCheckBox2");
        JCheckBox checkBox3 = new JCheckBox("JCheckBox3");
        JCheckBox checkBox4 = new JCheckBox("JCheckBox4");
        add(checkBox1);
        add(checkBox2);
        add(checkBox3);
        add(checkBox4);
    }

    @Override
    public void init() {
        loadJCheckBox();
        loadJFrame();
        loadJFrame();
    }
}
