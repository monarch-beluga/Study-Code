package Com.Monarch.Game;

import javax.swing.*;
import java.net.URL;

public class Data {
    public static URL headURL = Data.class.getResource("statics/Snake/head.jpg");
    public static URL foodURL = Data.class.getResource("statics/Snake/food.png");
    public static URL titleURL = Data.class.getResource("statics/Snake/Title.jpg");
    public static URL bodyURL = Data.class.getResource("statics/Snake/body.jpg");
    public static URL air_1URL = Data.class.getResource("statics/Sweeper/a.png");
    public static URL air_2URL = Data.class.getResource("statics/Sweeper/b.png");
    public static URL bombURL = Data.class.getResource("statics/Sweeper/bomb.png");
    public static URL bomb_1URL = Data.class.getResource("statics/Sweeper/bomb1.png");
    public static URL explosionURL = Data.class.getResource("statics/Sweeper/explosion.png");
    public static URL flagURL = Data.class.getResource("statics/Sweeper/flag1.png");
    public static ImageIcon head = new ImageIcon(headURL);
    public static ImageIcon food = new ImageIcon(foodURL);
    public static ImageIcon body = new ImageIcon(bodyURL);
    public static ImageIcon title = new ImageIcon(titleURL);
    public static ImageIcon air_1 = new ImageIcon(air_1URL);
    public static ImageIcon air_2 = new ImageIcon(air_2URL);
    public static ImageIcon bomb = new ImageIcon(bombURL);
    public static ImageIcon bomb_1 = new ImageIcon(bomb_1URL);
    public static ImageIcon explosion = new ImageIcon(explosionURL);
    public static ImageIcon flag = new ImageIcon(flagURL);
}
