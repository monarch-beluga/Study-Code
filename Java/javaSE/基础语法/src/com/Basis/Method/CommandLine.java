package com.Basis.Method;

public class CommandLine {
    public static void main(String[] args) {
        // length为获取数组元素个数
        for (int i = 0; i < args.length; i++) {
            System.out.println("args["+i+"]:"+args[i]);
        }
    }
}
