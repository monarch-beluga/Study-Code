using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _01Class
{
    public class Person
    {
        // 字段
        public string _name;
        public int _age;
        public char _gender;

        // 方法
        public void Test()
        {
            Console.WriteLine("我叫{0}，我今年{1}岁了，我是{2}生，我可以吃喝拉撒睡~~~.", this._name, this._age, this._gender);
        }
    }
}
