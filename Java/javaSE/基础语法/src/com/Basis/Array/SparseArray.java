package com.Basis.Array;

public class SparseArray {
    public static void main(String[] args) {
        int[][] arrays1 = new int[11][11];
        arrays1[1][2] = 1;
        arrays1[2][3] = 2;
        System.out.println("输出原始数组：");
        for (int[] ints : arrays1) {
            for (int anInt : ints) {
                System.out.print(anInt + "\t");
            }
            System.out.println();
        }

        int sum = 0;
        for (int i = 0; i < arrays1.length; i++) {
            for (int j = 0; j < arrays1[0].length; j++) {
                if (arrays1[i][j] != 0)
                    sum++;
            }
        }
        System.out.println("有效值的个数："+sum);

        int[][] arrays2 = new int[sum+1][3];
        arrays2[0][0] = arrays1.length;
        arrays2[0][1] = arrays1[0].length;
        arrays2[0][2] = sum;

        int count = 0;
        for (int i = 0; i < arrays1.length; i++) {
            for (int j = 0; j < arrays1[i].length; j++) {
                if (arrays1[i][j] != 0){
                    count++;
                    arrays2[count][0] = i;
                    arrays2[count][1] = j;
                    arrays2[count][2] = arrays1[i][j];
                }
            }
            if (count == sum)
                break;
        }
        System.out.println("稀疏数组：");
        for (int[] ints : arrays2) {
            for (int anInt : ints) {
                System.out.print(anInt+"\t");
            }
            System.out.println();
        }
        System.out.println("还原");
        int[][] arrays3 = new int[arrays2[0][0]][arrays2[0][1]];
        for (int i = 1; i < arrays2.length; i++) {
            arrays3[arrays2[i][0]][arrays2[i][1]] = arrays2[i][2];
        }
        System.out.println("还原的数组：");
        for (int[] ints : arrays3) {
            for (int anInt : ints) {
                System.out.print(anInt + "\t");
            }
            System.out.println();
        }
    }
}
