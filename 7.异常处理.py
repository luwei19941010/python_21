#-*-coding:utf-8-*-
# Author:Lu Wei


# def func():
#     try:
#         v=[]
#
#         v[111] #IndexError
#         return 123
#     except ValueError as e:
#         print('ValueError')
#     except IndexError as e:
#         print(e,type(e))
#     except Exception as e:
#         print('eorr')
#     finally:
#         print('无论对错最后都执行')
# print(func())

# try:
#     vla=int(10)
#     raise Exception('asdsadasd')
# except Exception as e:
#     print(e)

# def func():
#     result=True
#     try:
#         with open('123.txt',mode='r',encoding='utf-8') as f:
#             data=f.read()
#         if 'luwei' not in data:
#             raise Exception('123')
#     except Exception as e:
#         print(e)
#         result=False
#     return result
# print(func())

# class MYerror(Exception):
#     pass
#
# try:
#     raise MYerror('123123')
# except MYerror as e:
#     print(e)


class MYerror(Exception):
    def __init__(self,message):
        super().__init__()
        self.message=message

try:
    raise MYerror('123123')
except MYerror as e:
    print(e.__dict__)
    print(e.message,type(e))