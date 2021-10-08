package com.Basis.Method;

import java.util.Scanner;

public class MaxMethod {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        MaxMethod Max = new MaxMethod();
        System.out.println("输入a:");
        int a = scanner.nextInt();
        System.out.println("输入b:");
        int b = scanner.nextInt();
        int c = Max.compare1(a, b);
        if (c != a+b)
            System.out.println("较大的是："+c);
        System.out.println("================");

        a = scanner.nextInt();
        b = scanner.nextInt();
        compare2(a, b);

        scanner.close();
    }
    public int compare1(int a, int b){
        if (a > b)
            return a;
        else if (a < b)
            return b;
        else {
            System.out.println("两个数相等！");
            return a+b;
        }
    }
    public static void compare2(int a, int b){
        if (a > b)
            System.out.println("较大的数是："+a);
        else if (a < b)
            System.out.println("较大的数是："+b);
        else {
            System.out.println("两个数相等！");
        }
    }
}
