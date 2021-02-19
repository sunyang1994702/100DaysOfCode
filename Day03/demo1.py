"""
Class in Python3
"""

class Person:
    name = ''
    ## private attribute. can not be directly accessed outside the class
    __weight = 0
    def __init__(self, name, age, w):
        self.name = name
        self.age = age
        self.__weight = w
    
    def describe(self):
        print("{} is {} years old! The weight is {}".format(self.name, self.age, self.__weight))


p = Person('Sun Yang', 26, 70)
p.describe()
print(p.name)
p.name = 'Kobe'
print(p.name)
p.__weight ## error!!

"""
Class inherit 
"""
class Student(Person):
    def __init__(self, name, age, w, number):
        super().__init__(name, age, w)
        self.student_number = number
    
    def describe(self):
        print("Student number: {}".format(self.student_number))


bob = Student('Bob', 25, 60, '123456')
bob.describe()
print(bob._Person__weight) ## It seems like the subclass can access the private attribute of parent class outside class
bob._Person__weight = 90
print(bob._Person__weight)

