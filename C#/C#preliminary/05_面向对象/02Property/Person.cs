using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _02Property
{
    class Person
    {
        // 字段
        private string _name;
        public string Name
        {
            get { return _name; }
            set { _name = value; }
        }
        private int _age;
        public int Age
        {
            get { return _age; }
            set
            {
                if (value < 0 || value > 100)
                    value = 0;
                _age = value;
            }
        }
        private char _gender;
        public char Gender
        {
            get
            {
                if (_gender != '男' && _gender != '女')
                    return _gender = '男';
                return _gender;
            }
            set { _gender = value; }
        }

        // 方法
        public void Test()
        {
            Console.WriteLine("我叫{0}，我今年{1}岁了，我是{2}生，我可以吃喝拉撒睡~~~.", this.Name, this.Age, this.Gender);
        }
    }
}
