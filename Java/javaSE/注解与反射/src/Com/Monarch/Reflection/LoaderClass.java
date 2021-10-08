package Com.Monarch.Reflection;

public class LoaderClass {
    public static void main(String[] args) throws ClassNotFoundException {

        // 获取系统类的加载器
        ClassLoader systemClassLoader = ClassLoader.getSystemClassLoader();
        System.out.println(systemClassLoader);

        // 获取系统类加载器的父类加载器--> 扩展类加载器
        ClassLoader parent = systemClassLoader.getParent();
        System.out.println(parent);

        // 获取扩展类加载器的父类加载器--> 根加载器(C/C++)
        ClassLoader parent1 = parent.getParent();
        System.out.println(parent1);

        // 测试当前类是那个加载器加载的
        ClassLoader classLoader = Class.forName("Com.Monarch.Reflection.LoaderClass").getClassLoader();
        System.out.println(classLoader);

        // 测试 JDK 内置类是谁加载的
        classLoader = Class.forName("java.lang.Object").getClassLoader();
        System.out.println(classLoader);

        // 如何获得系统类加载器可以加载的路径
        System.out.println(System.getProperty("java.class.path"));
        /*
        E:\java\jdk8\jre\lib\charsets.jar;
        E:\java\jdk8\jre\lib\deploy.jar;
        E:\java\jdk8\jre\lib\ext\access-bridge-64.jar;
        E:\java\jdk8\jre\lib\ext\cldrdata.jar;
        E:\java\jdk8\jre\lib\ext\dnsns.jar;
        E:\java\jdk8\jre\lib\ext\jaccess.jar;
        E:\java\jdk8\jre\lib\ext\jfxrt.jar;
        E:\java\jdk8\jre\lib\ext\localedata.jar;
        E:\java\jdk8\jre\lib\ext\nashorn.jar;
        E:\java\jdk8\jre\lib\ext\sunec.jar;
        E:\java\jdk8\jre\lib\ext\sunjce_provider.jar;
        E:\java\jdk8\jre\lib\ext\sunmscapi.jar;
        E:\java\jdk8\jre\lib\ext\sunpkcs11.jar;
        E:\java\jdk8\jre\lib\ext\zipfs.jar;
        E:\java\jdk8\jre\lib\javaws.jar;
        E:\java\jdk8\jre\lib\jce.jar;
        E:\java\jdk8\jre\lib\jfr.jar;
        E:\java\jdk8\jre\lib\jfxswt.jar;
        E:\java\jdk8\jre\lib\jsse.jar;
        E:\java\jdk8\jre\lib\management-agent.jar;
        E:\java\jdk8\jre\lib\plugin.jar;
        E:\java\jdk8\jre\lib\resources.jar;
        E:\java\jdk8\jre\lib\rt.jar;
        E:\study\java\IntelliJ_IDEA\project\javaSE\out\production\注解与反射;
        E:\study\java\IntelliJ_IDEA\lib\idea_rt.jar
         */
    }
}
