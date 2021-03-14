package com.Basis.ProcessControl.Select;

import java.util.Scanner;

public class StructureSelect {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("请输入内容：");
        String s = scanner.nextLine();

        // equals判断字符串是否相等
        if (s.equals("hello")){
            System.out.println(s);
        }

        System.out.println("End");

        scanner.close();
    }
}
