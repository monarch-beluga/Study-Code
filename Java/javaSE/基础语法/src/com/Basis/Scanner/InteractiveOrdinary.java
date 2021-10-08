package com.Basis.Scanner;

import java.util.Scanner;

public class InteractiveOrdinary {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("请输入数据：");
        String str = scanner.nextLine();
        System.out.println("输入的内容为："+str);
        System.out.println("================");

        int i = 0;
        System.out.println("请输入整数数据：");
        if (scanner.hasNextInt()){
            i = scanner.nextInt();
            System.out.println("整数数据："+i);
        }
        else{
            System.out.println("输入的不是整数数据");
        }
        System.out.println("================");

        float f = 0.0f;
        System.out.println("请输入小数：");
        if (scanner.hasNextFloat()){
            f = scanner.nextFloat();
            System.out.println("小数数据："+f);
        }
        else{
            System.out.println("输入的不是小数数据");
        }
        System.out.println("================");

        scanner.close();
    }
}
