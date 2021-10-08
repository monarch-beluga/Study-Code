using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _03Static
{
    class Person
    {
        // 静态成员
        private static string _name;
        public static string Name
        {
            get { return _name; }
            set { _name = value; }
        }
        // 实例成员
        private char _gender;
        public char Gender
        {
            get { return _gender; }
            set { _gender = value; }
        }
        // 实例方法
        public void Test1()
        {
            Console.WriteLine("我是非静态方法");
        }
        // 静态方法
        public static void Test2()
        {
            Console.WriteLine("我是静态方法");
        }
    }
}
