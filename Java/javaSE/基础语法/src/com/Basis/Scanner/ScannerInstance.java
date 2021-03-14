package com.Basis.Scanner;

import java.util.Scanner;

public class ScannerInstance {
    public static void main(String[] args) {
        // 可以输入多个数字，并求出总和与平均数
        // 每输入一个数字用回车确认，通过输入非数字来结束输入并输出执行结果
        Scanner scanner = new Scanner(System.in);

        double sum = 0;
        int m = 0;

        // 通过循环来实现持续和结束输出
        // 用scanner.hasNextDouble()来判断是否有数值的输入
        System.out.println("请输入数值：");
        while (scanner.hasNextDouble()){
            double x = scanner.nextDouble();
            m++;
            sum += x;
            System.out.println("你输入了第"+m+"个数据，然后当前结果sum="+sum+",平均数为："+sum/m);
        }

        System.out.println(m + "个数的和为：" + sum);
        System.out.println(m + "个数的平均数是：" + sum/m);

        scanner.close();
    }
}
