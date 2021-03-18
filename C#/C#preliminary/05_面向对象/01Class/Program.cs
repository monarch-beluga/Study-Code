using System;

namespace _01Class
{
    class Program
    {
        static void Main(string[] args)
        {
            // 创建Person类的对象
            Person zhangSan = new Person();

            // 公有字段赋值
            zhangSan._name = "张三";
            zhangSan._age = 23;
            zhangSan._gender = '男';

            // 方法调用
            zhangSan.Test();
            /*我叫张三，我今年23岁了，我是男生，我可以吃喝拉撒睡~~~.*/
        }
    }
}
