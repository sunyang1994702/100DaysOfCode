## Method1
def sayName(func):
    print('I am Python freak')
    return func


def sayHi():
    print('Hello World')

a = sayName(sayHi)
a()


## Method2
def sayName(func):
    def inner():
        print('I am Python freak')
        return func()
    return inner

# Here, adding a decorator @sayName
@sayName
def sayHi():
    print('Hello World')

sayHi()


## Method3 decorator's function with parameter
def sayName(func):
    def inner(name):
        print('I am Python freak')
        return func(name)
    return inner

@sayName
def sayHi(name):
    print('Hi {}'.format(name))

sayHi("Sun")


## Method4 decorator with parameter
## reference: https://zhuanlan.zhihu.com/p/39093542
def multiply(by = None):
	def multiply_real_decorator(function):
		def wrapper(*args,**kwargs):
			return by * function(*args,**kwargs)
		return wrapper
	return multiply_real_decorator

@multiply(by=2)
def adder(a, b, c):
    return (a + b) * c

@multiply(by=3)
def subtractor(a, b):
    return a - b

print(adder(2,3,4))
print(subtractor(2,3))