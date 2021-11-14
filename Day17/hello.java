import java.util.*;
/**
 * hello
 */

public class hello{

    public static void main(String []args) {

        Programming program = new Programming("Python");

        System.out.println("Hello World!" + " Time:" + new java.util.Date());
        System.out.println("I am going to learn " + program.name);
        Person person1 = new Person("Sunyang", 27);
        person1.sayHallo();
     } 
    
}

class Programming{
    String name;
    public Programming(String name){
        this.name = name;
    }
}


