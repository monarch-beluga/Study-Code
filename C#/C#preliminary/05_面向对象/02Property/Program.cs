using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _02Property
{
    class Program
    {
        static void Main(string[] args)
        {
            Person zhangSan = new Person();
            // zhangSan._name = "张三";
            zhangSan.Name = "李四";
            zhangSan.Age = -23;
            zhangSan.Gender = '春';

            zhangSan.Test();
            /*我叫张三，我今年0岁了，我是男生，我可以吃喝拉撒睡~~~.*/
        }
    }
}