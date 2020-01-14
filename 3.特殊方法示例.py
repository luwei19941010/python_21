#-*-coding:utf-8-*-
# Author:Lu Wei

'''
1.__new__
2.__call__
3.__setitem__,__getitem__,__delitem__
4.__str__
5.__dict__
6.上下文管理，__enter__,__exit__
7.对象相加
8.__init__
'''
"""
class Foo(object):
    def __call__(self, *args, **kwargs):
        print('执行call方法')

    def __init__(self,x):
        print('初始化对象 ')
        '''
        用于给对象进行复制，初始化方法
        :param x:
        '''
        self.x=x
    def __new__(cls, *args, **kwargs):
        '''
        用于创建空的对象，构造方法
        :param args:
        :param kwargs:
        :return:
        '''
        print('创建对象')
        return object.__new__(cls)
obj=Foo(1)

obj()
Foo(2)()



class Foo1(object):
    def __call__(self, *args, **kwargs):
        print('执行对象加（）')
        pass
obj1=Foo1()
obj1()

Foo1()()

obj2=dict()
obj2['k1']=123

class Foo3(object):
    def __setitem__(self, key, value):
        print('执行setitem,key:%s,value:%s'%(key,value))

    def __getitem__(self, item):
        print('执行getitem,item:%s'%(item))
        return item+'llll'

    def __delitem__(self, key):
        print('执行delitem,item:%s'%(key))
        return key+'keykey'

obj3=Foo3()
obj3['k3']=123
val=obj3['k2']
print(val)
del obj3['k4']



class Foo(object):
    def __str__(self):
        '''
        当打印对象时，会自动调用该方法，将__str__方法返回值就打印在页面上
        :return:
        '''
        return 'asdasd'
obj=Foo()
print(obj,type(obj))


class Foo(object):
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email

obj=Foo('luwei',20,'663969502@qq.com')
print(obj.name)
print(obj.age)
print(obj.email)
val=obj.__dict__#__ dict __去对象中找到所有变量并将其转换为字典
print(val)


class Foo(object):
    def __enter__(self):
        self.open=open('123.txt',mode='a',encoding='utf-8')
        return self.open
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.open.close()

with Foo() as f:
    f.write('asd')
    f.write('asd')
    f.write('asd')




class Foo(object):
    def __add__(self, other):
        print(self,other)
        return 123

obj1=Foo()
obj2=Foo()
val=obj1 + obj2
print(val)
"""

