#！/usr/bin/python
#-*- coding:utf-8 -*-
import xlrd
class duqu():
    def shuju1(self):
        ff = xlrd.open_workbook(r'c:\Users\www\Desktop\asd2.xlsx')
        sheet=ff.sheets()[0]
        num=sheet.nrows
        li=[]
        for i in range(num):
            li.append(sheet.row_values(i))
        return li


print(duqu().shuju1()[1][0])