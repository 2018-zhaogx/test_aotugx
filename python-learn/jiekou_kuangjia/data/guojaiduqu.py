#！/usr/bin/python
#-*- coding:utf-8 -*-
import xlrd
class duqu():
    def duq(self):
        f=xlrd.open_workbook(r'c:\Users\www\Desktop\国家路径.xlsx')
        sheet=f.sheets()[0]
        num=sheet.nrows
        liebiao=[]
        for i in range(1,num):
            liebiao.append(sheet.row_values(i))
        return liebiao
if __name__=='__main__':
    pass
