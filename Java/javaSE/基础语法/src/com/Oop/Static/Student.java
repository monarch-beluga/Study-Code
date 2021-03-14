package com.Oop.Static;

public class Student {
    private static int age = 13;
    private double score = 99.5;

    public static void run(){
        System.out.println("run");
    }
    public void go(){
        System.out.println("go");
    }

    public static void main(String[] args) {
        Student s1 = new Student();
        System.out.println(Student.age);
        System.out.println(s1.age);
//        System.out.println(Student.score);
        System.out.println(s1.score);
        Student.run();
        s1.run();
//        Student.go();
        s1.go();
    }
}
