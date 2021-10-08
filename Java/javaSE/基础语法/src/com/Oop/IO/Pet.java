package com.Oop.IO;

public class Pet {
    public String name;
    public int age;

    public Pet(String name, int age) {
        this.name = name;
        this.age = age;
    }
    public void shout(){
        System.out.println(this.name+"叫了一声");
    }
}
/*
public static void main(String[] args) {
    Pet dog = new Pet("旺财",3);
    Pet cat = new Pet("旺财",3);
    dog.shout();
    System.out.println(dog.name);
    System.out.println(dog.age);
}
 */