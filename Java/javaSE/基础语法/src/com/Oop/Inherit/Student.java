package com.Oop.Inherit;

public class Student extends Person{
    private String name = "baijing";
    public Student(){
        System.out.println("Student无参执行了");
    }

    public void test(String name){
        System.out.println(name);
        System.out.println(this.name);
        System.out.println(super.name);
    }
    public void print(){
        System.out.println("Student");
    }
    public void test1(){
        print();
        this.print();
        super.print();
    }
}

/*
import com.Oop.Inherit.Student;

public class Application {
    public static void main(String[] args) {
        Student student = new Student();
        student.test("白鲸");
        student.test1();
    }
}
 */