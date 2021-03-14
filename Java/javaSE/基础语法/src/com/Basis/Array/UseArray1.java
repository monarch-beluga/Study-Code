package com.Basis.Array;

public class UseArray1 {
    public static void main(String[] args) {
        int[] arrays = {1,2,3,4,5};
        int[] arrays1 = reverseArray(arrays);
        printArray(arrays);
        printArray(arrays1);
    }
    public static void printArray(int[] a){
        for (int i = 0; i < a.length; i++)
            System.out.print(a[i] + "\t");
        System.out.println();
    }
    public static int[] reverseArray(int[] a){
        int[] result = new int[a.length];
        for (int i = 0; i < a.length; i++)
            result[a.length-i-1] = a[i];
        return result;
    }
}
