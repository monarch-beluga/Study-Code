using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using System.Threading;

namespace _05ReadFile
{
    class Program
    {
        static void Main(string[] args)
        {

            Program t = new Program();
            t.test();
            
        }
        public void test()
        {
            for (int i = 0; i < 5; i++)
            {
                Thread thread1 = new Thread(new ParameterizedThreadStart(Func1));
                thread1.Start(i);
            }
        }
        private void Func1(object o)
        {
            
            Console.WriteLine(o);
            Thread.Sleep(5000);
        }
    }
}
