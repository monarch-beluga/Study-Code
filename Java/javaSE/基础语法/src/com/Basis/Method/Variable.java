package com.Basis.Method;

public class Variable {
    public static void main(String[] args) {
        Max(2,5,6,7,9,4,6);
    }
    public static void Max(int... a){
        if (a.length == 0) {
            System.out.println("无数据比较！请输入数据");
            return;
        }
        int max = a[0];
        for (int i = 1; i < a.length; i++){
            if (max < a[i])
                max = a[i];
        }
        System.out.println("最大的数为："+max);
    }
}
