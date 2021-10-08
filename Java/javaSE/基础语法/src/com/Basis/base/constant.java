package com.Basis.base;

public class constant {
    // 修饰符无先后顺序
    static final double PI = 3.14;
    final static double Pi = 3.14;
    public static void main(String[] args) {
        final int c = 100;
        // c = 101;
        System.out.println(PI);
        System.out.println(Pi);
        System.out.println(c);
    }
}
