package Com.Monarch.Game.SweeperGame;

import Com.Monarch.Game.Data;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.Random;

public class SweeperPanel extends JPanel {
    private int[][] inside, surface;
    private JButton[][] buttons;
    private int N;
    private final Random random = new Random();
    private final int size = 16;
    private int bombs, grade = 1;
    private int[][] sst= {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
    private boolean flag = false, isFlag = false;

    public SweeperPanel() {
        init();
        this.setFocusable(true);
        addKeyListener(new SweeperKeyListener());
    }

    public void init(){
        N = (int)Math.pow(grade+2, 2);
        inside = new int[N][N];
        surface = new int[N][N];
        buttons = new JButton[N][N];
        initInside();
        initButton();
        setVisible(true);
        repaint();
    }
    // 初始化数组
    public void initInside(){
        bombs = N * grade;
        int num = 0;
        int x, y;
        int i, j;
        for (i = 0; i < N; i++) {
            for (j = 0; j < N; j++) {
                inside[i][j] = 0;
                surface[i][j] = 0;
            }
        }
        while (num < bombs){
            x = random.nextInt(N);
            y = random.nextInt(N);
            if (inside[x][y] != 9){
                inside[x][y] = 9;
                num++;
                for (int n = 0; n < 8; n++) {
                    i=x+sst[n][0];
                    j=y+sst[n][1];
                    if(i<N&&j<N&&i>=0&&j>=0&&inside[i][j]<9)
                        inside[i][j]++;
                }
            }
        }
    }

    public void initButton(){
        setLayout(null);
        int x = 300 - size * N / 2;
        int y = 300 - size * N / 2;
        int X, Y;
        SweeperMouseAdapter mouseAdapter = new SweeperMouseAdapter();
//        SweeperActionListener actionListener = new SweeperActionListener();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                X = x + j*size;
                Y = y + i*size;
                buttons[i][j] = new JButton();
                buttons[i][j].setBounds(X, Y, size, size);
                buttons[i][j].setIcon(Data.air_1);
                buttons[i][j].addMouseListener(mouseAdapter);
                buttons[i][j].setActionCommand(i + "-" +j);
                add(buttons[i][j]);
            }
        }
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        int x = 300 - size * N / 2;
        int y = 300 - size * N / 2;
        int X, Y;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (surface[i][j] != 0){
                    X = x + j*size;
                    Y = y + i*size;
                    buttons[i][j].setVisible(false);
                    if (surface[i][j] == 1) {
                        Data.air_2.paintIcon(this, g, X, Y);
                        g.setColor(Color.blue);
                        if (inside[i][j] != 0)
                            g.drawString("" + inside[i][j], X + 4, Y + size - 2);
                    }else if (surface[i][j] == 4) {
                        buttons[i][j].setVisible(true);
                        buttons[i][j].setIcon(Data.flag);
                    }else if (surface[i][j] == 3) {
                        Data.explosion.paintIcon(this, g, X, Y);
                    }else if (surface[i][j] == 2)
                        Data.bomb.paintIcon(this, g, X, Y);
                    else
                        Data.bomb_1.paintIcon(this, g, X, Y);
                }else {
                    buttons[i][j].setVisible(true);
                    buttons[i][j].setIcon(Data.air_1);
                }
            }
        }
        if (flag){
            grade++;
            g.setColor(Color.green);
            g.setFont(new Font("楷体", Font.BOLD, 30));
            g.drawString("成功!按下空格继续", 200, 50);
        }
        if (isFlag){
            g.setColor(Color.red);
            g.setFont(new Font("楷体", Font.BOLD, 30));
            g.drawString("失败!按下空格继续", 200, 50);
        }
    }
    class SweeperKeyListener extends KeyAdapter{
    @Override
    public void keyPressed(KeyEvent e) {
        if (e.getKeyCode() == KeyEvent.VK_SPACE && (flag || isFlag)) {
            if (flag)
                flag = false;
            else
                isFlag = false;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    remove(buttons[i][j]);
                }
            }
            init();
        }
    }
}
    class SweeperMouseAdapter extends MouseAdapter {
        @Override
        public void mouseClicked(MouseEvent e) {
            int c = e.getButton();
            JButton button = (JButton) e.getSource();
            Integer X = new Integer(button.getActionCommand().split("-")[0]);
            Integer Y = new Integer(button.getActionCommand().split("-")[1]);
            if (c == MouseEvent.BUTTON1){
                mark(X, Y);
            }else if (c == MouseEvent.BUTTON3){
                if (surface[X][Y] == 4)
                    surface[X][Y] = 0;
                else
                    surface[X][Y] = 4;
            }
            end();
            repaint();
        }
        public void display(int X, int Y){
            int x, y;
            if (inside[X][Y] == 0 && surface[X][Y] == 0) {
                surface[X][Y] = 1;
                for (int i = 0; i < 8; i++) {
                    x = X + sst[i][0];
                    y = Y + sst[i][1];
                    if (x < N && y < N && y >= 0 && x >= 0)
                        display(x, y);
                }
            }else
                surface[X][Y] = 1;
        }
        public void mark(int X, int Y){
            if (inside[X][Y] == 9) {
                for (int i = 0; i < N; i++)
                    for (int j = 0; j < N; j++)
                        if (inside[i][j] == 9)
                            surface[i][j] = 2;
                surface[X][Y] = 3;
                isFlag = true;
            }else
                display(X, Y);
        }
        public void end(){
            int n = 0;
            int n1 = 0;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (surface[i][j] == 0)
                        n++;
                }
            }
            if (n == 0){
                for (int i = 0; i < N; i++) {
                    for (int j = 0; j < N; j++) {
                        if (surface[i][j] == 4)
                            if (inside[i][j] != 9) {
                                surface[i][j] = 5;
                                n1++;
                            }else
                                surface[i][j] = 2;
                    }
                }
                if (n1 == 0)
                    flag = true;
                else
                    isFlag = true;
            }
        }
    }
}


