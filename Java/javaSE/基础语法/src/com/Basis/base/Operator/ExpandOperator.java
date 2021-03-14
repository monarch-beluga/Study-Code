package com.Basis.base.Operator;

public class ExpandOperator {
    public static void main(String[] args) {
        int a = 10;
        int b = 20;
        a+=b;
        System.out.println(a);
        a-=b;
        System.out.println(a);
        a*=b;
        System.out.println(a);
        a/=b;
        System.out.println(a);

        System.out.println("===========");
        // 字符串连接符  +
        System.out.println(a+b);
        System.out.println(""+a+b);
        System.out.println(a+b+"");
    }
}
