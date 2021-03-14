package com.Basis.Array;

public class StatementArray {
    public static void main(String[] args) {
        int[] nums;
        int nums1[];
        int sum = 0;
        nums = new int[10];
        nums1 = new int[20];
        for (int i = 0; i < nums.length; i++) {
            nums[i] = i + 1;
        }
        System.out.println("第5个元素为"+nums[4]);
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
        }
        System.out.println(nums);
        System.out.println(sum);
    }
}
