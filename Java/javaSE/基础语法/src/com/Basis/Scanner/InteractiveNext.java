package com.Basis.Scanner;

import java.util.Scanner;

public class InteractiveNext {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("使用next方式接收：");

        if (scanner.hasNext()){
            String str = scanner.next();
            System.out.println("输入的内容为："+str);
        }

        scanner.close();
    }
}
