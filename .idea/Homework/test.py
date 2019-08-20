'''
def dis(*val):     #def定义函数，#*默认是list，**是kv对
    for i in val:
        print(i)

dis(1,2,3,4,5)
'''

'''
sum=lambda i,j:i+j         #lambda表达式，ij输入，：后输出

print(sum(1,2))
'''

'''
total=0
def sum(i,j):
    global total
    total=i+j
    print(total)
sum(1,2)
print(total)
'''
'''
def fun():
    i=3
    def xxx():
        return i
    return xxx()
print(fun())        #应该是闭包
'''

'''
def some(**args):
    print(args)

mydict={"a":1,"b":2}
some(**mydict)
'''

'''
import random

def product():
    print("开始生产")
    data=random.randint(0,9)
    print("生产者生产了"+str(data))
    yield data
    print("xxxx")
p=product()
c=next(p)
print(c)
c=p.send("111")
print(c)
'''
'''
def xxx():
    yield 99
    yield 100

x=xxx()
c=x.send(None)
print(c)

c=next(x)
print(c)
'''
#if __name__=="__main__":
 #   print("xxx")


'''
class xxx:
    pass

#print(xxx.__dict__)

x=xxx()
xxx.a=lambda self,x,y:x+y

print(x.a(1,2))
'''
'''
if __name__=="__main__":
    p1=Person(10,"aaa")
    p1.X=100
    p1.xxx();
    print(p1.Person__id)
    print(p1.X,Person.X)

    p1.adwda+"adasdwd"

    print(Person.__dict__)
    print(p1.__dict__)
'''

'''
class Score:

    def __init__(self,zh_Score,math_Score):
        self.zh_Score=zh_Score
        self.math_Score=math_Score

    def __add__(self, other):
        return Score(self.zh_Score+other.zh_Score,self.math_Score+other.math_Score)

    def __sub__(self, other):
        return Score(self.zh_Score - other.zh_Score, self.math_Score - other.math_Score)

    def __mul__(self, other):
        return Score(self.zh_Score * other.zh_Score, self.math_Score * other.math_Score)

    def __truediv__(self, other):
        return Score(self.zh_Score / other.zh_Score, self.math_Score / other.math_Score)

    def __floordiv__(self, other):
        return Score(self.zh_Score // other.zh_Score, self.math_Score // other.math_Score)

    def __str__(self):
        return "Totle zh_Score is :"+str(self.zh_Score)+" and math_Score is: "+str(self.math_Score)

if __name__ == "__main__":
    s1=Score(100,99)
    s2=Score(98,100)
    s3=s1 + s2
    print(s3)
'''

#oop test extendstest python执行流程demo
'''
class MyException(Exception):
     def __init__(self,message):
         Exception.__init__(self)
         self.message=message


a=int(input("please input a num:"))
if a<10:
     try:
         raise MyException("my excepition is raised ")
     except MyException as e:
         print (e.message)
'''


from contextlib import contextmanager
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()

class Some:
    def __init__(self,name):
        self.name=name
    def close(self):
        print(self.name+" close")

with closing(Some("some")) as res:
    print(res.name)
    
    


f =open('/home/liugaojian/Desktop/python.txt')
str=f.read()
print(f)

