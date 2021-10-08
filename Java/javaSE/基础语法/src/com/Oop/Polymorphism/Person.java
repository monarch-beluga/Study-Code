package com.Oop.Polymorphism;

public class Person {
    public void run(){
        System.out.println("run");
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
        Object s3 = new Student();
        s2.run();
        s1.run();
//        s2.eat();
        s1.eat();
        System.out.println(s3 instanceof Student);
        System.out.println(s3 instanceof Person);
        System.out.println(s3 instanceof Object);
        System.out.println(s3 instanceof Teacher);
        System.out.println(s3 instanceof String);
        System.out.println("===================");
        System.out.println(s2 instanceof Student);
        System.out.println(s2 instanceof Person);
        System.out.println(s2 instanceof Object);
        System.out.println(s2 instanceof Teacher);
//        System.out.println(s2 instanceof String);
        System.out.println(s1 instanceof Student);
        System.out.println(s1 instanceof Person);
        System.out.println(s1 instanceof Object);
//        System.out.println(s1 instanceof Teacher)
//        System.out.println(s1 instanceof String);
    }
}
 */