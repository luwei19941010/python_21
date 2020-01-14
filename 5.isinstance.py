#-*-coding:utf-8-*-
# Author:Lu Wei

class Foo(object):
    pass

class Bar(object):
    pass

obj=Bar()
print(isinstance(obj,Bar))
print(isinstance(obj,Foo))