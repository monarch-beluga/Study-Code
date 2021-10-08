package com.Basis.base;

public class Base_conversion {
    public static void main(String[] args) {
        // 整数拓展： 进制
        int i = 10;
        int i2 = 010;   // 八进制
        int i3 = 0x10;  // 十六进制
        System.out.println(i);
        System.out.println(i2);
        System.out.println(i3);
        System.out.println("===============");

        // 浮点数扩展
        float f = 0.1f; // 0.1
        double d = 1.0 / 10;  // 0.1
        System.out.println(f == d);   // false
        // 最好不要用浮点数去比较
        float d1 = 221564321f;
        float d2 = d1 + 1;
        System.out.println(d1 == d2);
        System.out.println("===============");

        // 字符拓展
        char c1 = 'a';
        char c2 = '中';
        System.out.println(c1);
        System.out.println((int) c1);    // 强制转换
        System.out.println(c2);
        System.out.println((int) c2);    // 强制转换
        // 所有的字符本质还是数字
        // 编码  Unicode  2字节 0 - 65536   Excel 2 16  = 65536
        char c3 = '\u0061';
        System.out.println(c3);
        // 转义字符
        // \t   制表符
        // \n   换行
        // .....
        System.out.println("Hello\nWorld");
        System.out.println("===============");

        String sa = new String("hello world");
        String sb = new String("hello world");
        System.out.println(sa == sb);
        String sc = "hello world";
        String sd = "hello world";
        System.out.println(sc == sd);
        // 对象   从内存分析

        // 布尔值扩展
        boolean flag = true;
        if (flag == true) {
        } // 新手
        if (flag) {
        } // 老手
        // Less is More!  代码要精简易读
    }
}
