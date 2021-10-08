package Com.Monarch.TestURL;

import javax.net.ssl.HttpsURLConnection;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;

public class TestRUL3 {
    public static void main(String[] args) throws IOException {
        URL url = new URL("https://m801.music.126.net/20201217221938/c57b7685c977ee11518b49a492e83b33/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/5286158199/9170/d14e/9c9b/2c71d6ffd1365c412b71db7b27ae3dd7.m4a");

        HttpsURLConnection urlConnection = (HttpsURLConnection) url.openConnection();

        InputStream is = urlConnection.getInputStream();

        FileOutputStream fos = new FileOutputStream("网络编程/像一道光.m4a");

        byte[] buffer = new byte[1024];
        int len;
        while ((len = is.read(buffer)) != -1){
            fos.write(buffer, 0, len);
        }

        fos.close();
        is.close();
        urlConnection.disconnect();
    }
}
