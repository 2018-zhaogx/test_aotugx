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
        item=''.join(items)
        print(item)
        m = re.compile('<img width="100" alt="(.*?)" src="', re.S)
        d = re.compile('导演: (.*?)&nbsp;&nbsp', re.S)
        yp = re.compile('v:average">(.*?)</span>', re.S)
        pf = re.compile('<span>(.*?)人评价</span>',re.S)
        new_m=m.findall(item)
        new_d=d.findall(item)
        new_yp = yp.findall(item)
        new_pf = pf.findall(item)
        mm.append(new_m)
        dd.append(new_d)
        yyp.append(new_yp)
        ppf.append(new_pf)
        print(mm)
        return list(zip(mm,dd,yyp,ppf))
    def save(self,a):
        try:
            f=xlrd.open_workbook('open.xls')
            sheet1=f.sheets()[0]
            num=sheet1.nrows
            new_f=copy(f)
            sheet=new_f.get_sheet(0)
            cc = list(zip(a, s, d, f))
            for q, w, e, r in a:
                sheet.write(1+num,0,q[0])
                sheet.write(1+num,1,w[0])
                sheet.write(1+num,2,e[0])
                sheet.write(1+num,3,r[0])
                num += 1
            new_f.save('open.xls')
        except:
            f=xlwt.Workbook()
            sheet=f.add_sheet('sheet1')
            sheet.write(0, 0, '电影名')
            sheet.write(0, 1, '导演')
            sheet.write(0, 2, '影评')
            sheet.write(0, 3, '评分')
            for a,s,d,f in:
                sheet.write(i + 1, 0, a[i][0])
                sheet.write(i + 1, 1, s[i][0])
                sheet.write(i + 1, 2, d[i][0])
                sheet.write(i + 1, 3, f[i][0])
            f.save('open.xls')
tt=doubian()
for i in range(1):
    html=tt.qingqiu(i)
    a,s,d,f=tt.guolv(html)
    tt.save(a,s,d,f)