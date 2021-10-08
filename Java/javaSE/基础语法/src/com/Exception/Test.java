package com.Exception;

public class Test {
    public static void main(String[] args) {
        int a = 1;
        int b = 0;

        try {
            System.out.println(a/b);
        }
        catch (Error e){
            System.out.println("Error");
        }
        catch (ArithmeticException e){
            System.out.println("程序出现异常，变量不能为0");
        }
        finally {
            System.out.println("finally");
        }
    }
}
