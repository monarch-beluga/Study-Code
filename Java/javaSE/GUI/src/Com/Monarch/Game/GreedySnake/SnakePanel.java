package Com.Monarch.Game.GreedySnake;

import Com.Monarch.Game.Data;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.Random;

public class SnakePanel extends JPanel{
    private final char w = 'U';
    private final char a = 'L';
    private final char s = 'D';
    private final char d = 'R';
    private char fx;
    private int length, score;
    private final int[] snakeX = new int[1000];
    private final int[] snakeY = new int[1000];
    private final int rows = 40;
    private final int cols = 25;
    private final int size = 24;
    private boolean isStart = false;
    private boolean isFail = false;
    private boolean isVictory = false;
    private final Timer timer = new Timer(200, new SnakeActionListener());
    private int foodX, foodY;
    private final Random random = new Random();


    public SnakePanel() {
        init();
        this.setFocusable(true);
        this.addKeyListener(new SnakeKeyListener());
    }

    private void init(){
        length = 3;
        score = 0;
        timer.setDelay(200);
        fx = d;
        for (int i = 0; i < length; i++){
            snakeX[i] = 6-i;
            snakeY[i] = 2;
        }
        foodX = random.nextInt(rows);
        foodY = random.nextInt(cols);
        timer.start();
    }

    @Override
    public void paintComponent(Graphics g) {
        super.paintComponents(g);
        setBackground(Color.white);
        Data.title.paintIcon(this,g,20,10);
        g.setColor(Color.darkGray);
        g.fillRect(20, 180, 960,600);

        for (int i = 1; i < length; i++) {
            Data.body.paintIcon(this, g, 20 + snakeX[i] * size, 180 + snakeY[i] * size);
        }
        Data.food.paintIcon(this, g, 20 + size * foodX, 180 + size * foodY);
        Data.head.paintIcon(this, g, 20 + snakeX[0] * size, 180 + snakeY[0] * size);
        g.setColor(Color.white);
        g.setFont(new Font("华文楷体", Font.BOLD, 25));
        g.drawString("长度:"+length,780,70);
        g.drawString("积分:"+score*10,780,110);

        if (!isStart) {
            g.setColor(Color.white);
            g.setFont(new Font("华文楷体", Font.BOLD, 50));
            g.drawString("按下空格开始游戏!", 300, 400);
        }
        if (isFail){
            g.setColor(Color.red);
            g.setFont(new Font("华文楷体", Font.BOLD, 50));
            g.drawString("失败!按下空格重新开始游戏!", 200, 400);
        }
        if (isVictory){
            g.setColor(Color.green);
            g.setFont(new Font("华文楷体", Font.BOLD, 50));
            g.drawString("恭喜通关!按下空格重新开始游戏!", 150, 400);
        }
    }

    class SnakeKeyListener implements KeyListener{
        private int keyCode;
        private char keyChar;
        public void fxChange(){
            if ((fx != s) && ((keyCode == KeyEvent.VK_UP) || (keyChar == 'w')))
                fx = w;
            else if ((fx != w) && (keyCode == KeyEvent.VK_DOWN) || (keyChar == 's'))
                fx = s;
            else if ((fx != d) && (keyCode == KeyEvent.VK_LEFT) || (keyChar == 'a'))
                fx = a;
            else if ((fx != a) && (keyCode == KeyEvent.VK_RIGHT) || (keyChar == 'd'))
                fx = d;
        }
        @Override
        public void keyPressed(KeyEvent e) {
            keyCode = e.getKeyCode();
            keyChar = e.getKeyChar();
            if (keyCode == KeyEvent.VK_SPACE){
                if (isFail){
                    isFail = false;
                    init();
                }else if (isVictory){
                    isVictory = false;
                    init();
                }else
                    isStart = !isStart;
                repaint();
            }
            fxChange();
        }

        @Override
        public void keyReleased(KeyEvent e) {

        }
        @Override
        public void keyTyped(KeyEvent e) {

        }
    }

    class SnakeActionListener implements ActionListener{
        public void fxChange(){
            if (fx == w){
                snakeY[0]--;
                if (snakeY[0] < 0)
                    snakeY[0] = cols-1;
            }else if (fx == a){
                snakeX[0]--;
                if (snakeX[0] < 0)
                    snakeX[0] = rows-1;
            }else if (fx == s){
                snakeY[0]++;
                if (snakeY[0] == cols)
                    snakeY[0] = 0;
            }else if (fx == d){
                snakeX[0]++;
                if (snakeX[0] == rows)
                    snakeX[0] = 0;
            }
        }
        public void foodJudge(){
            if (snakeX[0] == foodX && snakeY[0] == foodY){
                length++;
                foodX = random.nextInt(rows);
                foodY = random.nextInt(cols);
                score++;
                if (score < 160)
                    timer.setDelay(200-score);
            }
        }
        public void failureJudge(){
            for (int i = 1; i < length; i++)
                if (snakeX[0] == snakeX[i] && snakeY[0] == snakeY[i]) {
                    isFail = true;
                    return;
                }
        }
        public void winOrLose(){
            if (length == 1000){
                isVictory = true;
            }
        }
        @Override
        public void actionPerformed(ActionEvent e) {
            if (isStart && !isFail && !isVictory){
                foodJudge();
                for (int i = length-1; i > 0; i--){
                    snakeX[i] = snakeX[i-1];
                    snakeY[i] = snakeY[i-1];
                }
                fxChange();
                failureJudge();
                winOrLose();
                repaint();
            }
            timer.start();
        }
    }
}
