package com.Basis.ProcessControl.Select;

import java.util.Scanner;

public class StructureSelect4 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("请输入等级：");
        char grade = scanner.nextLine().charAt(0);

        switch (grade){
            case 'A':
                System.out.println("优秀");
                break;
            case 'B':
                System.out.println("良好");
            case 'C':
                System.out.println("及格");
            case 'D':
                System.out.println("再接再厉");
            case 'E':
                System.out.println("挂科");
            default:
                System.out.println("未知等级");
        }

        scanner.close();

    }
}
