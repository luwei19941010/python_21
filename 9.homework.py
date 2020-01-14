#-*-coding:utf-8-*-
# Author:Lu Wei
#1.列举你了解的面向对象中的特殊成员，并为每个写代码示例。
'''
1.__init__初始化对象
2.__new__生成对象
3.__call__对象加（）
4.__setitem__
5.__getitem__
6.__delitem__
7.__enter__
8.__exit__
9.__dict__
10.__str__打印对象时输出
11.__add__对象相加



#2.看代码写结果
class Foo(object):

    def __init__(self, age):
        self.age = age

    def display(self):
        print(self.age)


data_list = [Foo(8), Foo(9)]
for item in data_list:
    print(item.age, item.display())
#8 8 none 9 9 none


#3.看代码写结果

class Base(object):
    def __init__(self, a1):
        self.a1 = a1


    def f2(self, arg):
        print(self.a1, arg)


class Foo(Base):
    def f2(self, arg):
        print(self.a1,'666')


obj_list = [Base(1), Foo(2), Foo(3)]
for obj in obj_list:
    obj.f2(1)
#1,1
#2,666
#3,666

#4.看代码写结果
class StarkConfig(object):

    def __init__(self,num):
        self.num = num

    def changelist(self,request):
        print(self.num,request)

class RoleConfig(StarkConfig):

    def changelist(self,request):
        print('666')

config_obj_list = [StarkConfig(1),StarkConfig(2),RoleConfig(3)]

for item in config_obj_list:
    print(item.num)
    #1,2,3


#5.看代码写结果

class StarkConfig(object):

    def __init__(self,num):
        self.num = num

    def changelist(self,request):
        print(self.num,request)

class RoleConfig(StarkConfig):
    pass

config_obj_list = [StarkConfig(1),StarkConfig(2),RoleConfig(3)]
for item in config_obj_list:
    item.changelist(168)
#1,168
#2.168
#3.168



#6.看代码写结果
class StarkConfig(object):

    def __init__(self,num):
        self.num = num

    def changelist(self,request):
        print(self.num,request)

class RoleConfig(StarkConfig):

    def changelist(self,request):
        print(666,self.num)

config_obj_list = [StarkConfig(1),StarkConfig(2),RoleConfig(3)]
for item in config_obj_list:
    item.changelist(168)
#1,168
#2,168
#666,3



#7.看代码写结果
class StarkConfig(object):

    def __init__(self,num):
        self.num = num

    def changelist(self,request):
        print(self.num,request)

    def run(self):
        self.changelist(999)

class RoleConfig(StarkConfig):

    def changelist(self,request):
        print(666,self.num)

config_obj_list = [StarkConfig(1),StarkConfig(2),RoleConfig(3)]
config_obj_list[1].run()
config_obj_list[2].run()

#2,999
#666,3



#8.看代码写结果
class StarkConfig(object):

    def __init__(self,num):
        self.num = num

    def changelist(self,request):
        print(self.num,request)

    def run(self):
        self.changelist(999)

class RoleConfig(StarkConfig):

    def changelist(self,request):
        print(666,self.num)


class AdminSite(object):
    def __init__(self):
        self._registry = {}

    def register(self,k,v):
        self._registry[k] = v

site = AdminSite()
print(len(site._registry)) #0
site.register('range',666)
site.register('shilei',438)
print(len(site._registry))#2

site.register('lyd',StarkConfig(19))
site.register('yjl',StarkConfig(20))
site.register('fgz',RoleConfig(33))

print(len(site._registry))#5
print(site._registry)#{'fgz': <__main__.RoleConfig object at 0x0000000000A9D908>, 'range': 666, 'yjl': <__main__.StarkConfig object at 0x0000000000A9D828>, 'lyd': <__main__.StarkConfig object at 0x0000000000A9D8D0>, 'shilei': 438}



#9.
class StarkConfig(object):

    def __init__(self,num):
        self.num = num

    def changelist(self,request):
        print(self.num,request)

    def run(self):
        self.changelist(999)

class RoleConfig(StarkConfig):

    def changelist(self,request):
        print(666,self.num)

class AdminSite(object):
    def __init__(self):
        self._registry = {}

    def register(self,k,v):
        self._registry[k] = v

site = AdminSite()
site.register('lyd',StarkConfig(19))
site.register('yjl',StarkConfig(20))
site.register('fgz',RoleConfig(33))
print(len(site._registry)) # 3

for k,row in site._registry.items():
    row.changelist(5)
    #19,5
    #20,5
    #666,33


#10.
class StarkConfig(object):

    def __init__(self,num):
        self.num = num

    def changelist(self,request):
        print(self.num,request)

    def run(self):
        self.changelist(999)

class RoleConfig(StarkConfig):

    def changelist(self,request):
        print(666,self.num)

class AdminSite(object):
    def __init__(self):
        self._registry = {}

    def register(self,k,v):
        self._registry[k] = v

site = AdminSite()
site.register('lyd',StarkConfig(19))
site.register('yjl',StarkConfig(20))
site.register('fgz',RoleConfig(33))
print(len(site._registry)) # 3

for k,row in site._registry.items():
    row.run()
#19,999
#20,999
#666,33


#11.
class UserInfo(object):
    pass

class Department(object):
    pass

class StarkConfig(object):

    def __init__(self,num):
        self.num = num

    def changelist(self,request):
        print(self.num,request)

    def run(self):
        self.changelist(999)

class RoleConfig(StarkConfig):

    def changelist(self,request):
        print(666,self.num)

class AdminSite(object):
    def __init__(self):
        self._registry = {}

    def register(self,k,v):
        self._registry[k] = v(k)

site = AdminSite()
site.register(UserInfo,StarkConfig)
site.register(Department,StarkConfig)
print(len(site._registry))#2
for k,row in site._registry.items():
    row.run()
#<class '__main__.UserInfo'>,999
#<class '__main__.Department'> 999


#12.
class F3(object):
    def f1(self):
        ret = super().f1()
        print(ret)
        return 123


class F2(object):
    def f1(self):
        print('123')


class F1(F3, F2):
    pass


obj = F1()
obj.f1()
#123
#None


#13.
class Base(object):
    def __init__(self, name):
        self.name = name


class Foo(Base):
    def __init__(self, name):
        super().__init__(name)
        self.name = "于大爷"


obj1 = Foo('alex')
print(obj1.name)#"于大爷"

obj2 = Base('alex')
print(obj2.name)#alex
'''

#14.
class Base(object):
    pass

class Foo(Base):
    pass


obj = Foo()

print(type(obj) == Foo)#T
print(type(obj) == Base)#F
print(isinstance(obj,Foo))#T
print(isinstance(obj,Base))#T




