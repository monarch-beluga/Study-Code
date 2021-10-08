package com.Oop.Polymorphism;

public class Student extends Person{
    public void run(){
        System.out.println("son");
    }
    public void eat(){
        System.out.println("eat");
    }
}

/*
import com.Oop.Polymorphism.Person;
import com.Oop.Polymorphism.Student;
import com.Oop.Polymorphism.Teacher;

public class Application {

    public static void main(String[] args) {
        Student s1 = new Student();
        Person s2 = new Student();
        ((Student)s2).eat();

    }
}

 */