package Com.Monarch.ThreadClass;

import org.apache.commons.io.FileUtils;

import java.io.File;
import java.io.IOException;
import java.net.URL;

public class TestThread2 extends Thread{
    private final String url;
    private final String name;

    public TestThread2(String url, String name) {
        this.url = url;
        this.name = name;
    }

    @Override
    public void run() {
        WebDownloader downloader = new WebDownloader();
        downloader.downloader(url, name);
        System.out.println("下载文件名为："+name);
    }

    public static void main(String[] args) {
        TestThread2 thread1 = new TestThread2("https://img2020.cnblogs.com/blog/2213660/202012/2213660-20201212111216478-609764954.png", "多线程/image/1.png");
        TestThread2 thread2 = new TestThread2("https://img2020.cnblogs.com/blog/2213660/202011/2213660-20201129222930724-678630901.png", "多线程/image/2.png");
        TestThread2 thread3 = new TestThread2("https://img2020.cnblogs.com/blog/2213660/202011/2213660-20201129221933721-552034182.png", "多线程/image/3.png");
        thread1.start();
        thread2.start();
        thread3.start();
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