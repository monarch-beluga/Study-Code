package com.Basis.ProcessControl.Select;

import java.util.Scanner;

public class StructureSelect2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("请输入成绩：");
        int score = scanner.nextInt();

        if (score >= 60){
            System.out.println("及格");
        }else {
            System.out.println("不及格");
        }

        scanner.close();
    }
}
