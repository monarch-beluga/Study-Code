package com.Basis.ProcessControl.Cycle;

public class StructureFor {
    public static void main(String[] args) {
        int sum = 0;
        int sum1 = 0;
        // while形式
        int a = 1;  // 初始化
        while (a<=100){ // 条件判断
            sum += a;
            a++;    // 迭代
        }
        System.out.println(sum);
        System.out.println("============");

        // for形式
        for(int b=1; b<=100; b++){
            sum1 += b;
        }
        System.out.println(sum1);

    }
}
