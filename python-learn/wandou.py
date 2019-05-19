#！/usr/bin/python
#-*- coding:utf-8 -*-
import re
import requests
import xlwt
import xlrd
from xlutils.copy import copy

class doubian(object):
    def qingqiu(self,qwe):
        url='https://movie.douban.com/top250?start={}&filter='.format(25*qwe)
        head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}
        res=requests.get(url,headers=head)
        html=res.content.decode('utf-8')
        return html
    def guolv(self,asd):
        mm,dd,yyp,ppf=[],[],[],[]
        patt=re.compile('<div class="item">(.*?)<p class="quote">',re.S)
        items=patt.findall(asd)
        for i in items:
            m = re.compile('<img width="100" alt="(.*?)" src="', re.S)
            d = re.compile('导演: (.*?)&nbsp;&nbsp', re.S)
            yp = re.compile('v:average">(.*?)</span>', re.S)
            pf = re.compile('<span>(.*?)人评价</span>',re.S)
            new_m=m.findall(i)
            new_d=d.findall(i)
            new_yp = yp.findall(i)
            new_pf = pf.findall(i)
            mm.append(new_m)
            dd.append(new_d)
            yyp.append(new_yp)
            ppf.append(new_pf)
        return mm,dd,yyp,ppf
    def save(self,a,s,d,f):
        try:
            mn=xlrd.open_workbook('open.xls')
            sheet1=mn.sheets()[0]
            num=sheet1.nrows
            new_f=copy(mn)
            sheet=new_f.get_sheet(0)
            for i in range(len(a)):
                sheet.write(i+num,0,a[i][0])
                sheet.write(i+num,1,s[i][0])
                sheet.write(i+num,2,d[i][0])
                sheet.write(i+num,3,f[i][0])
            new_f.save('open.xls')
        except:
            mn=xlwt.Workbook()
            sheet=mn.add_sheet('sheet1')
            sheet.write(0, 0, '电影名')
            sheet.write(0, 1, '导演')
            sheet.write(0, 2, '影评')
            sheet.write(0, 3, '评分')
            for i in range(len(a)):
                sheet.write(i + 1, 0, a[i][0])
                sheet.write(i + 1, 1, s[i][0])
                sheet.write(i + 1, 2, d[i][0])
                sheet.write(i + 1, 3, f[i][0])
            mn.save('open.xls')
tt=doubian()
for i in range(3):
    html=tt.qingqiu(i)
    a,s,d,f=tt.guolv(html)
    tt.save(a,s,d,f)





