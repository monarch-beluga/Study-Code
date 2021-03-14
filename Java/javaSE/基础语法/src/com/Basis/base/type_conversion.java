package com.Basis.base;

public class type_conversion {
    public static void main(String[] args) {
        int i = 128;
        byte b = (byte)i;   // 内存溢出
        double c = i;

        // 强制转换     （类型）变量名     高到低
        // 自动转换     低到高

        System.out.println(i);  // 128
        System.out.println(b);  // -128
        System.out.println(c);  // 128.0

        System.out.println("============");
        // 精度问题
        System.out.println((int)23.7);  // 23
        System.out.println((int)-45.89f);   // -45

        System.out.println("============");
        char ch = 'a';
        int cd = ch+1;
        System.out.println(cd);     // 98
        System.out.println((char)cd);   // b

        System.out.println("============");
        int money = 10_0000_0000;
        int years = 20;
        int total = money * years;  // -1474836480
        long total1 = money * years;    // -1474836480
        long total2 = money * (long)years;  // 20000000000
        System.out.println(total);
        System.out.println(total1);
        System.out.println(total2);
    }
}
