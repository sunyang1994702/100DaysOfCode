"""
Class in Python3
----> Some private class method.
"""



class Student:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __getattr__(self, attr):
        if attr == 'age':   
            return 26

    def __call__(self):
        print("Name: {}".format(self.name))

    def __add__(self, other):
        return "{} and {} weight is: {}".format(self.name, other.name, (self.weight + other.weight))

    def __len__(self):
        return 1000


s = Student('Sun', 70)
print(s.name)
print(s.age) ## __getattr__ 
print(s.aaa) ## None
s() ## __call__

s2 = Student("Bob", 80)
print(s + s2) ## __add__ 

print(len(s)) ## __len__