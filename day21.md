 day21

### 今日内容

- 嵌套

- 特殊成员 '__ init __'
- type/isinstance/issubclass/super
- 异常处理

### 内容回归

```
def func():
	pass
```

```
class Foo(object):
	def func(self):
		pass
obj=Foo()
obj.func()
```

1.谈谈你了解的面向对象？ 针对面向对象三个特性开始聊。封装，继承，多态

2.类和对象是什么关系？对象是类的一个实例

```
class Foo(object):
	x=1
	def __ init __(self)
	def func(self):
		pass
obj=Foo()
```

3.self是什么?

```
#self就是一个形式参数,对象调用方法时 python内部将该对象传给这个参数。
class Foo(object)：
	def func(self):
		pass
obj=Foo()
obj.func()
```

4.类成员&对象成员以及他们之间的关系

```
class Foo(object):
	x=1
	def __ init __(self)
	def func(self):
		pass
obj=Foo()
```

对象能访问类变量，但不能修改类变量

5.类和对象 都可以当做变量或嵌套到其他类型中。

```
class Foo(object):
	def run(self):
		pass
v=[Foo,Foo]
v=[Foo(),Foo()]
obj=Foo()
v=[obj.run,obj.run,]
```



### 内容详细

#### 1.嵌套

- 函数：参数可以任意类型
- 字典：

#### 2.特殊成员

​	为了能够快速的实现执行某些方法而生

```
1.__new__
2.__call__
3.__setitem__,__getitem__,__delitem__
4.__str__
5.__dict__
6.上下文管理，__enter__,__exit__
7.对象相加
8.__init__
```

##### 2.1 __ init __(self)

```
#用于初始化对象，给对象进行赋值，初始化方法
class Foo(object):

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
```

##### 2.2 __ new __(self)

```
#用于创建空的对象，构造方法
class Foo(object):

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
```

##### 2.3 __ cal __

```
#对象加()执行类中call方法。
class Foo(object):
    def __call__(self, *args, **kwargs):
        print('执行call方法')

obj=Foo(1)
obj()

Foo()()
```

##### 2.4 __ getitem __ , __ setitem __ , __ delitem __

```
#字典其实也是类。obj2是通过dict实例化出来的对象。对象加[]执行类中相关的方法
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
obj3['k3']=123            #内部会自动调用__setitem__方法
val=obj3['k2']            #内部会自动调用__getitem__方法
print(val)
del obj3['k4']            #内部会自动调用__delitem__方法
```

##### 2.5 __ str __

```
class Foo(object):
    def __str__(self):
        '''
        当打印对象时，会自动调用该方法，将__str__方法返回值就打印在页面上
        :return:
        '''
        return 'asdasd'
obj=Foo()
print(obj,type(obj))
#asdasd <class '__main__.Foo'>
```

##### 2.6 __ dict __

```
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
```

##### 2.7 上下文管理【面试】

```
#__enter__,__exit__#先执行enter 在执行自己的代码 最后执行exit
class Foo(object):
    def __enter__(self):
        self.open=open('123.txt',mode='a',encoding='utf-8')
        return self.open   #enter方法返回什么
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.open.close()

with Foo() as f:#f是什么 是由__ENTER__方法返回值所决定
    f.write('asd')
    f.write('asd')
    f.write('asd')
```

##### 2.8 对象相加__ add __

```
class Foo(object):
    def __add__(self, other):
        print(self,other)
        return 123

obj1=Foo()
obj2=Foo()
val=obj1 + obj2
#由obj1触发add方法，add 方法中self为obj1，other为obj2
```



#### 3.内置函数补充

##### 3.1 type

##### 3.2 issubclass

```
#issubclass(a,b) 判断a是否为b的子类（派生类）

class Base(object):
    pass

class Foo(Base):
    pass

class Foo1(Foo):
    pass

class Bar(object):
    pass
print(issubclass(Bar,Base))
print(issubclass(Foo1,Base))
```

##### 3.3 isinstance

```
#isinstance(a,b) 判断a是否为b的实例，或者是否为b的基类的实例。
class Foo(object):
    pass

class Bar(object):
    pass

obj=Bar()
print(isinstance(obj,Bar))
print(isinstance(obj,Foo))
```

3.4 super

```
#根据self对象所属类的继承关系，按顺序挨个找func方法找到‘’第一个‘’就不在继续找（如果还想继续找则继续写super（）.func（）##
# v1=super().func()
class Base(object):
    def func(self):
        print('base.func')
        return 123

class Foo(Base):
    def func(self):
        v1=super().func()
        print(v1)
        print('Foo.func')

obj=Foo()
obj.func()
```

```
#根据self对象所属类的继承关系，按顺序挨个找func方法找到‘’第一个‘’就不在继续找（如果还想继续找则继续写super（）.func（）##

class Base(object):
    def func(self):
        print('base.func')
        super().func()
        return 123

class Foo(object):
    def func(self):
        print('Foo.func')

class Bar(Base,Foo):
    def func(self):
        super().func()
        #print(v1)

obj=Bar()
obj.func()
```



#### 4.异常处理

##### 4.1 try异常处理

```
try:
    v=[]
    v[111]						#IndexError
except ValueError as e:
    print('ValueError')
except IndexError as e:
    print('IndexError') 
except Exception as e:
    print(e) 					#e是Exception类的对象，中有一个错误信息，打印的是对象
finally:
    print('无论对错最后都执行')
```



```
特殊情况 try 在函数内部，函数体内部有return时仅结束函数体内部代码 try代码继续执行
一、
def func():
    try:
        v=[]
        v[111] #IndexError
        return 123
    except ValueError as e:
        print('ValueError')
    except IndexError as e:
        print('IndexError')
    except Exception as e:
        print('eorr')
    finally:
        print('无论对错最后都执行')
print(func())
'''
IndexError
无论对错最后都执行
None
'''

二、
def func():
    try:
        v=[]
        return 123
        v[111] #IndexError

    except ValueError as e:
        print('ValueError')
    except IndexError as e:
        print('IndexError')
    except Exception as e:
        print('eorr')
    finally:
        print('无论对错最后都执行')
print(func())

'''
无论对错最后都执行
123
'''

```

##### 4.2主动触发异常

```
try:
    vla=int(10)
    raise Exception('asdsadasd')#主动抛出错误
except Exception as e:
    print(e)
```



```
def func():
    result=True
    try:
        with open('123.txt',mode='r',encoding='utf-8') as f:
            data=f.read()
        if 'luwei' not in data:
            raise Exception('123')
    except Exception as e:
        print(e)
        result=False
    return result
print(func())
```



4.3自定义异常处理

```
class MYerror(Exception):#继承Exception类
    pass

try:
    raise MYerror('123123')#主动触发自定义报错
except MYerror as e:
    print(e)
```

```
class MYerror(Exception):
    def __init__(self,message):
        super().__init__()
        self.message=message

try:
    raise MYerror('123123')
except MYerror as e:
    print(e.message)
```

