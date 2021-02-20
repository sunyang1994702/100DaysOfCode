""" Class method modifier in class """

## classmethod -- 1
import time

class Date:
    
    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Alternate constructor 
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)



a = Date(2012, 12, 21) # Primary
print("Year: {}, month: {}".format(a.year, a.month))
b = Date.today()
print("Year: {}, month: {}".format(b.year, b.month))




## classmethod -- 2
class Person:
    family_name = "Kevin"
    def __init__(self, name):
        self.name = name

    @classmethod
    def reset_name(cls, n):
        return cls(n)
        
    def show_name(self):
        print("Name: {} {}".format(self.family_name, self.name))


person1 = Person("Yang")
person1.show_name()
person2 = Person.reset_name("Nan")
person2.show_name()
