package com.Basis.base;

public class variable_Scope {

    // 实例变量
    String name;
    int age;

    // 类变量  static
    static double salary = 20000.0;

    // main()方法
    public static void main(String[] args) {
        // 局部变量
        int i = 10;
        System.out.println(i);

        // 实例变量的使用
        variable_Scope scope = new variable_Scope();
        System.out.println(scope.age);
        System.out.println(scope.name);

        // 类变量使用
        System.out.println(salary);
    }
    // 其他方法
    public void add(){
//        System.out.println(i);
    }
}
