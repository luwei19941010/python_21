#-*-coding:utf-8-*-
# Author:Lu Wei
"""
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

"""
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