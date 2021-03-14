/*
%[flag][width][.precision]type为printf()函数格式控制符的格式
[]表示此处的内容可省略
*/
#include <stdio.h>
int main()
{
    int n = 234;
    float f = 9.8;
    char c = '@';
    char *str = "http://c.biancheng.net";
    printf("%10d%12f%4c%8s\n", n, f, c, str);
/*  
width表示输出的宽度
当width表示的宽度大于输出结果时，以空格补齐
当输出结果的宽度超过 width 时，width 不再起作用，按照数据本身的宽度来输出
*/
    n = 123456;
    f = 882.923672;
    str = "abcdefghi";
    printf("n: %.9d  %.4d\n", n, n);
    printf("f: %.2lf  %.4lf  %.10lf\n", f, f, f);
    printf("str: %.5s  %.15s\n", str, str);
/*
.precision用于实数型输出时表示输出的精度
当用于整数显示表示输出的最小宽度，当整数宽度不足时使用0在左边补齐
当用于字符串时表示输出的最大宽度，当字符串长度大于precision时会截取字符串
*/
    int m = 192;
    n = -943;
    f = 84.342;
    printf("m=%10d, m=%-10d\n", m, m);  //演示 - 的用法
    printf("m=%+d, n=%+d\n", m, n);  //演示 + 的用法
    printf("m=% d, n=% d\n", m, n);  //演示空格的用法
    printf("f=%.0f, f=%#.0f\n", f, f);  //演示#的用法
/*
flag是标志字符，有四种：-、+、空格、#
-表示左对齐，如果没有就按照默认的对齐方式即右对齐
+用于整数或者小数，表示输出符号（正负号）。如果没有，那么只有负数才会输出符号
空格：用于整数或者小数，输出值为正时冠以空格，为负时冠以负号
#对于八进制（%o）和十六进制（%x / %X）整数，# 表示在输出时添加前缀，对于小数（%f / %e / %g），# 表示强迫输出小数点
*/
    return 0;
}