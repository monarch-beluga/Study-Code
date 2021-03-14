package com.Basis.Array;

public class BubbleArray {
    public static void main(String[] args) {
        int[] arrays = {2,5,4,6,8,1,5};
        for (int array : arrays)
            System.out.print(array+"\t");
        System.out.println();
        bubble(arrays);
        for (int array : arrays)
            System.out.print(array+"\t");
    }
    public static void bubble(int[] a){
        int temp = 0;
        for (int i = 0; i < a.length-1; i++) {
            for (int j = 0; j < a.length-i-1; j++){
                if (a[j+1] < a[j]){
                    temp = a[j];
                    a[j] = a[j+1];
                    a[j+1] = temp;
                }
            }
        }
    }
}
