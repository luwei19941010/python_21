#-*-coding:utf-8-*-
# Author:Lu Wei

import xlrd,xlwt
data = xlrd.open_workbook('2.xlsx')
sheet1 = data.sheet_by_name("Sheet1")
sheet2 = data.sheet_by_name("Sheet2")
workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('1')
# l=sheet1.col_values(0)
# for i in range(len(sheet1.col_values(0))):
#     print(sheet1.col_values(0,i))
# print(sheet1.col_values(0,1,2))

for i in range(len(sheet1.col_values(0))):
    for j in range(len(sheet2.col_values(0))):
        if int(sheet1.cell(i,0).value)==int(sheet2.cell(j,0).value):
            num=str(sheet2.cell(j, 1).value)
            worksheet.write(i,0,num)
workbook.save('1.xls')