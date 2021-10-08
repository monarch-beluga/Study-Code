package com.Basis.ProcessControl;

public class Break {
    public static void main(String[] args) {
        int i = 0;
        while (i < 100){
            System.out.print(i + "\t");
            if (i == 20){
                break;
            }
            i++;
        }
    }
}
