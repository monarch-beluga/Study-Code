using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _03Static
{
    static class Student
    {
        // 静态成员
        private static string _name;
        public static string Name
        {
            get { return _name; }
            set { _name = value; }
        }
        public static void Test()
        {
            Console.WriteLine("我是静态方法");
        }
    }
}