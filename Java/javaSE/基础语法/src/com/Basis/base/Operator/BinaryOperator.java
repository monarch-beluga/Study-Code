package com.Basis.base.Operator;

public class BinaryOperator {
    public static void main(String[] args) {
        // 二元运算符
        // Ctrl + D：复制当前行到下一行

        int a = 10;
        int b = 20;

        System.out.println(a+b);
        System.out.println(a-b);
        System.out.println(a*b);
        System.out.println(a/(double)b);
        System.out.println("==============");

        long i = 123213132123121L;
        int j = 123;
        short k = 10;
        byte l = 8;

        System.out.println(i+j+k+l);    // long
        System.out.println(j+k+l);  // int
        System.out.println(k+l);    // int
        System.out.println("==============");

        int s = 10;
        int s1 = 10;
        int w = 3;
        int w1 = 3;
        System.out.println(s%w);    // 1 求余
        System.out.println(s++);    // 10 先赋值，再自增1
        System.out.println(++s1);   // 11 先自增再赋值
        System.out.println(w--);    // 3 先赋值，再自减1
        System.out.println(--w1);   // 2 先自减再赋值
        System.out.println("==============");
    }
}
