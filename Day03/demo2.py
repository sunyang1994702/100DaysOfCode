"""
Class in Python3
----> Some private class method.
"""

_formats = {
    '-': '{f.name}-{f.age}',
    ':': '{f.name}:{f.age}',
    '=': '{f.name}={f.age}'
}

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def who(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
    
    ## define a private method
    def __show(self):
        print("This is private!")
        
    ## define a public method to call a internal private method
    def show(self):
        print('This is Public!')
        self.__show()

    ## Change the string representation of the instance. re-define __repr__ and __str__.
    def __repr__(self):
        return 'Person__repr({}, {})'.format(self.name, self.age)
    

    def __str__(self):
        return 'Name is : {}'.format(self.name)

    ## customize a format function.
    def __format__(self, code):
        fmt = _formats[code]
        return fmt.format(f=self)


bob = Person("Bob", 25)
bob.who()
bob.__show() ## error
bob.show()
## call __str__ method
print(bob)

print(format(bob, '-'))
print(format(bob, '='))
