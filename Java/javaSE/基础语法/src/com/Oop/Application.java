package com.Oop;

import com.Oop.Internal.Outer;

public class Application {

    public static void main(String[] args) {
        Outer outer = new Outer();
        Outer.Inner inner = outer.new Inner();
        inner.getID();
    }
}
