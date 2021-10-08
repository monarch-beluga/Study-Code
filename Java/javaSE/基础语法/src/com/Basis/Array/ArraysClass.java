package com.Basis.Array;

import java.util.Arrays;

public class ArraysClass {
    public static void main(String[] args) {
        int[] a = {1,2,3,4,9090,31323,564,54,45,65};
        System.out.println(a);
        System.out.println(Arrays.toString(a));
        Arrays.sort(a);
        System.out.println(Arrays.toString(a));
        Arrays.fill(a, 2, 4, 0);
        System.out.println(Arrays.toString(a));
        Arrays.fill(a,  0);
        System.out.println(Arrays.toString(a));
    }
}
