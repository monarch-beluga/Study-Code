package com.Basis.Method;

import java.util.Scanner;

public class Exercise {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double a = 0;
        String ch;
        double b = 0;
        int c = 1;
        while (true){
            System.out.println("输入1开始，0结束");
            c = scanner.nextInt();
            if (c == 0)
                break;
            a = scanner.nextDouble();
            ch = scanner.next();
            b = scanner.nextDouble();
            calculator(a, ch, b);
        }
    }
    public static void calculator(double a, String ch, double b){
        switch (ch){
            case "+":
                System.out.println(a+b);break;
            case "-":
                System.out.println(a-b);break;
            case "*":
                System.out.println(a*b);break;
            case "/":
                System.out.println(a/b);break;
        }
    }
}
