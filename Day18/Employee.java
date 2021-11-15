import java.util.*;

public class Employee{
    // name is a string variable
    public String name;
    // salary is a private variable only used in this class
    private double salary;
    // country is a public variable
    String country = "China";
    // constructer. similiar with the __init__() of Python
    public Employee (String empName){
        this.name = empName;
    }

    public void setSalary(double empSal){
        salary = empSal;
    }  
    // print 
    public void printEmp(){
        System.out.println("Name : " + name );
        System.out.println("Salary : " + salary);
        System.out.println("Country : " + country);
    }

    public static void main(String[] args){
        Employee empOne = new Employee("JAVA");
        empOne.setSalary(1000.0);
        empOne.printEmp();
        Person1 person1 = new Person1("Python");
        person1.setSalary(1200.0);
        person1.reviseCountry("Japan");
        person1.printEmp();
        // it would be error. outside class can not call the private variable (salary) of different class. 
        // person1.salary = 14555.0;
        // country would be ok! it was a public variable
        person1.country = "US";
        person1.printEmp();
    }
}

// sub calss extending Employee. Just to test the private and public variable! 
class Person1 extends Employee{
    public Person1(String empName) {
        super(empName); 
    }

    public void reviseCountry(String country){
        super.country = country;
    }
}
