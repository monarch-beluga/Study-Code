package com.Basis.ProcessControl.Select;

import java.util.Scanner;

public class StructureSelect5 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("请输入名称:");
        String name = scanner.nextLine();

        switch (name){
            case "Monarch":
                System.out.println("Monarch");
                break;
            case "Beluga":
                System.out.println("Beluga");
                break;
            default:
                System.out.println("未知名称");
        }

        scanner.close();

    }
}
