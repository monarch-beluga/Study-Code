package Com.Monarch.IO.Character;

import java.io.*;

public class FileWrites {
    public static void main(String[] args) throws IOException {
        Writer writer = new FileWriter("E:\\temp\\a.txt");
        writer.write('好');
        writer.write('\n');
        char[] chars = {'好', '好', '学', '习'};
        writer.write(chars);
        writer.write('\n');
        writer.write(chars, 1, 2);
        writer.write('\n');
        writer.write("好好学习");
        System.out.println("end");
        writer.close();
    }
}
