package Com.Monarch.RunnableInterface;

import org.apache.commons.io.FileUtils;

import java.io.File;
import java.io.IOException;
import java.net.URL;

public class TestCreate {
    public static void main(String[] args) {
        MyRunner runner1 = new MyRunner("https://img2020.cnblogs.com/blog/2213660/202012/2213660-20201212111216478-609764954.png", "多线程/image/1.png");
        MyRunner runner2 = new MyRunner("https://img2020.cnblogs.com/blog/2213660/202011/2213660-20201129222930724-678630901.png", "多线程/image/2.png");
        MyRunner runner3 = new MyRunner("https://img2020.cnblogs.com/blog/2213660/202011/2213660-20201129221933721-552034182.png", "多线程/image/3.png");
        new Thread(runner1).start();
        new Thread(runner2).start();
        new Thread(runner3).start();
    }
}

class MyRunner implements Runnable{
    private final String url;
    private final String name;

    MyRunner(String url, String name) {
        this.url = url;
        this.name = name;
    }

    @Override
    public void run() {
        WebDownloader downloader = new WebDownloader();
        downloader.downloader(url, name);
        System.out.println("下载文件名为："+name);
    }
}

class WebDownloader{
    public void downloader(String url, String name){
        try {
            FileUtils.copyURLToFile(new URL(url), new File(name));
        } catch (IOException e) {
            System.out.println("IO异常，downloader方法异常");
        }
    }
}

