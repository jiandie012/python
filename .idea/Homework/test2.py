'''
m=int(input("请输入最大值"))
count=1
sum=0
while count<=m:
    sum=sum+count
    count+=1
print("1到",m,"之和为",sum)
'''

'''
import inspect,os
def xxx():
    pass

class aaa():
    pass

print(inspect.ismodule(xxx))
print(inspect.isclass(aaa))

print(inspect.getdoc(xxx))
print(inspect.getsourcefile(xxx))  # 文件路径
print(inspect.getsourcelines(xxx))
'''


'''
def decorate(func):
    def wrapper():           #装饰器就是用函数装饰函数，，decorate就是装饰器，只能是类或者方法
        print("定义一个装饰器")
        func()
    return wrapper
def text1():
    print("text1")

decorate(text1)()
'''
'''
def decorate(func):
    def wrapper():
        print("定义一个装饰器")
        func()
    return wrapper
@decorate             #@xxx其实就是 xxx(),并且把紧随的内容当做参数传入。。。。传入函数，返回带参数的函数
def text1():
    print("text1")

text1()
'''
'''
def decorate(name):
    def wrapper(func):
        def sub_wrapper():
            print("定义一个带参数的装饰器",name) #传入函数，返回带参数的函数的函数
            func()
        return sub_wrapper
    return wrapper

@decorate(name="python")   
def text1():
    print("text1")

text1()
'''
'''
class DDD():
    @staticmethod
    def decorate(func):
        def wrapper():
            func()
        return wrapper


@DDD.decorate
def test11():
    print("oooo")

test11()

'''
'''
class Testcall:
    def __init__(self):
        print("init")
    def __call__(self, *args, **kwargs):
        print("call")

testcall=Testcall()

testcall() #call其实就是运算符-> '()'

'''
'''
class desc1:
    def __init__(self,func):       #类装饰器
        print("￥￥￥￥￥")
        self.func=func
    def __call__(self, *args, **kwargs):
        print("～～～～")
        res=self.func(args[0])
        return res

@desc1
def some(arg):
    return arg+1

r=some(1)
print(r)
'''
class C():
    a = 'abc'

    def __setattr__(self, key, value):
        print('__setattr__() is called',key,value)

    def __getattribute__(self, *args, **kwargs):
        print("__getattribute__() is called")
        return object.__getattribute__(self, *args, **kwargs)

    def __getattr__(self, name):
        print("__getattr__() is called ",name)
        return name + " from getattr"

    def __get__(self, instance, owner):
        print("__get__() is called", instance, owner)
        return self

    def __set__(self, instance, value):
        print("__set__() is called",instance,value)

    def __del__(self):
        print("__del__() is called")

    def __delattr__(self, item):
        print("__delattr__() is called ", item)




class C2(object):
    d = C()


c = C()
c2 = C2()

print("-----1----")
c.a="aaa"
print("----2-----")
print(c.a)
print("----3-----")
print(c.zzzzzzzz)
print("+++++++++")
c2.d="xxx"
c2.d
print(c2.d.a)
