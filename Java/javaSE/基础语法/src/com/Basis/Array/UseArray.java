package com.Basis.Array;

public class UseArray {
    public static void main(String[] args) {
        int[] arrays = {1,2,3,4,5};
        for (int i = 0; i < arrays.length; i++) {
            System.out.print(arrays[i] + "\t");
        }
        System.out.println();
        System.out.println("============");
        for (int array : arrays) {
            System.out.print(array + "\t");
        }
        System.out.println();
        System.out.println("===========");
        int sum = 0;
        for (int array : arrays) {
            sum += array;
        }
        System.out.println(sum);
        System.out.println("===========");
        int max = arrays[0];
        for (int array : arrays) {
            if (max < array)
                max = array;
        }
        System.out.println(max);
    }
}
