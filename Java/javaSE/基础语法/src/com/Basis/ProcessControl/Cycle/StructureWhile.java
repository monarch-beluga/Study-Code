package com.Basis.ProcessControl.Cycle;

public class StructureWhile {
    public static void main(String[] args) {

        int i = 0;
        int sum = 0;

        while (i<100){
            i++;
            sum += i;
        }

        System.out.println(sum);
    }
}
