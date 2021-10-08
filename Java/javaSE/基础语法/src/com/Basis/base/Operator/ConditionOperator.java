package com.Basis.base.Operator;

public class ConditionOperator {
    public static void main(String[] args) {
        int score = 80;
        String type = score < 60 ? "不及格":"及格";
        System.out.println(type);
    }
}
