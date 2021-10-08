package Com.Monarch.IO.Character;

import java.io.*;

public class BufferedCopy1 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader("E:\\temp\\a.txt"));
        BufferedWriter writer = new BufferedWriter(new FileWriter("E:\\temp\\f.txt"));
        String s = reader.readLine();
        while (true){
            writer.write(s);
            if ((s = reader.readLine()) == null)
                break;
            writer.write('\n');
        }
        System.out.println("end");
        reader.close();
        writer.close();
    }
}
