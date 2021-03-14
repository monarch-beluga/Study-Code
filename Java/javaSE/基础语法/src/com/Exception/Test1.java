package com.Exception;

public class Test1 {
    public static void main(String[] args) {
        int a = 1;
        int b = 0;
//        new Test1().test(a, b);
        new Test1().test1(a, b);
    }
    public void test(int a, int b){
        if (b == 0){
            throw new ArithmeticException();
        }
    }
    public void test1(int a, int b) throws ArithmeticException{
        if (b == 0){
            throw new ArithmeticException();
        }
    }
}
