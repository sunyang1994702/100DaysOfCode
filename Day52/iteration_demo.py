list1 = [1,2,3,4]
it = iter(list1)
print(it)

print(next(it))
print(next(it))

list2 = [1,2,3,4,5,6,7]
for x in iter(list2):
    print(x)


## Creating a iteration function
class Mynumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

mynumber = Mynumbers()
myiter = iter(mynumber)
print(myiter)

print(next(myiter))
print(next(myiter))
print(next(myiter))