#！/usr/bin/python
#-*- coding:utf-8 -*-
import requests
import re
ff=[]
foo=[]
for p in range(1,3):
    oo={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'

    }
    a='https://www.qiushibaike.com/text/page/{}/'.format(p)
    b=requests.get(a,headers=oo)  #headers=oo应对开发的>>反爬技术
    c=b.content.decode('utf-8')#  网页编码方式查看：网页的源代码中找meta的行尾显示编码方式
    d=re.compile('<div class="content">(.*?)</span>',re.S)
    dd=re.compile('<h2>(.*?)</h2>',re.S)
    fo=dd.findall(c)
    f=d.findall(c)
    for j in fo:
        j=str(j)
        j=j.replace('\n','')
        j=j.strip()
        foo.append(j)
    for i in f:
        i=i.replace('<span>','')
        i=i.strip()
        i=i.replace('<br/>','')
        ff.append(i)
print(len(ff))
print(foo)
import xlwt
ee=xlwt.Workbook()
sheet=ee.add_sheet('sheet1')
for i in range(len(ff)):
    sheet.write(i,0,foo[i])
    sheet.write(i,1,ff[i])
ee.save('you.xls')