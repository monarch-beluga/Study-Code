using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using System.Threading;
using System.Text.RegularExpressions;

namespace _05ReadFile
{
    class Program
    {
        static void Main(string[] args)
        {

            string[] array = { "123", "-12.5", "-154", "kjf", "卡卡给" };
            for (int i = 0; i < array.Length; i++)
            {
                Console.WriteLine(IsNumber(array[i]));
                Console.WriteLine(IsFloat(array[i]));
            }
                
            
        }

        public static bool IsNumber(String strNumber)
        {
            Regex objNotNumberPattern = new Regex("[^0-9.-]");
            Regex objTwoDotPattern = new Regex("[0-9]*[.][0-9]*[.][0-9]*");
            Regex objTwoMinusPattern = new Regex("[0-9]*[-][0-9]*[-][0-9]*");
            String strValidRealPattern = "^([-]|[.]|[-.]|[0-9])[0-9]*[.]*[0-9]+$";
            String strValidIntegerPattern = "^([-]|[0-9])[0-9]*$";
            Regex objNumberPattern = new Regex("(" + strValidRealPattern + ")|(" + strValidIntegerPattern + ")");

            return !objNotNumberPattern.IsMatch(strNumber) &&
                !objTwoDotPattern.IsMatch(strNumber) &&
                !objTwoMinusPattern.IsMatch(strNumber) &&
                objNumberPattern.IsMatch(strNumber);
        }

        public static bool IsFloat(String strNumber)
        {
            Regex reg = new Regex(@"^[0-9-]+\.\d+$");
            return reg.IsMatch(strNumber);
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
