package com.Basis.Method;

public class AddMethod {
    public static void main(String[] args) {
        int sum = add(1,2);
        double sum1 = add(1.0, 2.0);
        System.out.println(sum);
        System.out.println(sum1);
    }
    public static int add(int a, int b){
        return a+b;
    }
    public static double add(double a, double b){
        return a+b;
    }
}
