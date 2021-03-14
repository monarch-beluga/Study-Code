package com.Basis.ProcessControl.Cycle;

public class StructureFor1 {
    public static void main(String[] args) {
        int sum1 = 0;
        int sum2 = 0;

        // 计算0-100之间的奇数和偶数的和
        for (int i = 0; i <= 100; i++){
            if (i % 2 == 0)
                sum1 += i;
            else
                sum2 += i;
        }
        System.out.println("偶数之和为："+sum1);
        System.out.println("奇数之和为："+sum2);
        System.out.println("总和为："+(sum1+sum2));
        System.out.println("==================");

        // 输出1-1000之间能被5整除的数，并且每行输出3个
        int n = 0;
        for (int i = 1; i <= 1000; i++){
            if (i % 5 ==0){
                n++;
                System.out.print(i + "\t");
            }
            if (n == 3){
                System.out.print("\n");
                n = 0;
            }
        }
        System.out.print("\n");
        System.out.println("====================");

        // 打印九九乘法口诀表
        for (int i = 1; i < 10; i++) {
            for (int i1 = 1; i1 <= i; i1++) {
                System.out.print(i1 + "*" + i + "=" + (i*i1) + "\t");
            }
            System.out.println();
        }
        System.out.println("====================");


    }
}
