package com.Basis.base.Operator;

public class Priority {
    public static void main(String[] args) {
        int a = 10;
        int b = 20;
        int c = 30;
        System.out.println(a+b*c);
        System.out.println(a+b%c);
        System.out.println(++a+a);
        System.out.println(a+++a);
        System.out.println(a<b-10);
        System.out.println(a<b&&a>b);
        System.out.println((a+b)*c);
    }
}
