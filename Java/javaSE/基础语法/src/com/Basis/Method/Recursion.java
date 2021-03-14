package com.Basis.Method;

import java.util.Scanner;

public class Recursion {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("输入一个数：");
        int n = scanner.nextInt();
        long s = factorial(n);
        System.out.println("该数的阶乘为："+s);

        scanner.close();
    }
    public static long factorial(int i){
        if (i == 1)
            return 1;
        else
            return i * factorial(i-1);
    }
}
