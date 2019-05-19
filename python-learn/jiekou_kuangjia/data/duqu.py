#！/usr/bin/python
#-*- coding:utf-8 -*-
import xlrd
class Shuju():

    def Wenjian(self):
        f = xlrd.open_workbook(r'c:\Users\www\Desktop\工作簿0.xlsx')
        sheet = f.sheets()[0]
        num = sheet.nrows
        wenjian = []
        for i in range(num):
            if i != 0:
                wenjian.append(sheet.row_values(i))
        return wenjian


