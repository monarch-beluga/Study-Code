package com.Basis.ProcessControl;

public class Exercise {
    public static void main(String[] args) {
        // 打印三角形    5行
        int n = 5;
        char c = '*';
        for (int i = 1; i <= n; i++){
            for (int j = n; j > i; j--)
                System.out.print(" ");
            for (int j = 0; j < 2*i-1; j++)
                System.out.print(c);
            System.out.println();
        }
        System.out.println("========================");

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n+i; j++){
                if (j < n-i-1)
                    System.out.print(" ");
                else
                    System.out.print(c);
            }
            System.out.println();
        }

    }
}
