#-*-coding:utf-8-*-
# Author:Lu Wei

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