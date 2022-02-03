## reference: https://zhuanlan.zhihu.com/p/149532177

## *args parameter
def test_args(*args):
    for arg in args:
        print("arg : {}".format(arg))

test_args('yasoob','python','eggs' ,'test')


## **kwargs parameter
def test_kwargs(**kwargs):
    for key, value in kwargs.items():
        print("{} == {}".format(key, value))

test_kwargs(name="yasoob", number=24)


## test:
def demo(a,b,c,d):
    return a + b + c + d

arr = [1,2,3,4]
print(demo(*arr))

def func(*args, **kwargs):
    print('args = {}'.format(args))
    print('kwargs = {}'.format(kwargs))

func(1,2,3,4, A='a', B='b', C='c')