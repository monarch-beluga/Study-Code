package com.Basis.ProcessControl;

public class LableGoto {
    public static void main(String[] args) {
        // 普通循环
        int count = 0;
        for (int i = 101; i < 150; i++) {
            for (int j = 2; j <= i/2; j++){
                if (i % j == 0){
                    count = 1;
                    break;
                }
            }
            if (count == 0)
                System.out.print(i+"\t");
            count = 0;
        }
        System.out.println();
        System.out.println("===============");

        // goto类的标签循环，outer:.... continue outer;
        outer: for (int i = 101; i < 150; i++) {
            for (int j = 2; j <= i/2; j++){
                if (i % j == 0){
                    continue outer;
                }
            }
            System.out.print(i+"\t");
        }
    }
}
