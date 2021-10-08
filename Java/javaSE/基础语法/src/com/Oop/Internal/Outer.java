package com.Oop.Internal;

public class Outer {
    private int id = 1020221;
    public void out(){
        System.out.println("外部类的方法");
    }
    public class Inner{
        public void in(){
            System.out.println("内部类的方法");
        }
        public void getID(){
            System.out.println(id);
        }
    }
}
