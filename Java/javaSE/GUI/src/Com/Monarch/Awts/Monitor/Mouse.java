package Com.Monarch.Awts.Monitor;

import Com.Monarch.Awts.Main.MyFrame;

import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.ArrayList;

public class Mouse {
    public static void main(String[] args) {
        new MyMouseMonitor("鼠标监听");
    }
}

class MyMouseMonitor extends MyFrame{
    ArrayList<Point> points;
    public MyMouseMonitor(String s) {
        super(s);
        points = new ArrayList<Point>();

        this.addMouseListener(new MyMouse());
    }
    @Override
    public void paint(Graphics g) {
        for (Point point : points) {
            g.fillOval(point.x, point.y, 5, 5);
        }
    }
    private class MyMouse extends MouseAdapter{

        @Override
        public void mousePressed(MouseEvent e) {
            points.add(new Point(e.getX(), e.getY()));
            repaint();
        }
    }
}
