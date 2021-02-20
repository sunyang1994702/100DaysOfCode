
""" Property and staticmethod modifier in Class  """
class Person:
    family_name = "Yang"
    def __init__(self, first_name):
        self.__first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self.__first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self.__first_name = value

    # deleter function
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can not delete this attribute")


    # staticmethod Modifier
    """ Parameters are not mandatory! Usually used inside the calss! """
    @staticmethod 
    def show_class():
        return "My class is Person!"

    def show_info(self):
        print("Nmae: {} {}".format(self.__first_name, self.family_name))
        print(self.show_class())



p = Person('Sun')
print(p.first_name) ## getter
p.first_name = 'Wang' ## setter
print(p.first_name)
#del p.first_name ## deleter

p.show_info() ## show_info
