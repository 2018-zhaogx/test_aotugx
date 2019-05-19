#！/usr/bin/python
#-*- coding:utf-8 -*-
import requests
import re
# class dianying():
    # def qingqiu(self,asd):
url='https://movie.douban.com/top250?start=25&filter='#.format(25*asd)
head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}
res=requests.get(url,headers=head)
html = res.content.decode('utf-8')
#return html
# def guolv(self,qwe):
patt=re.compile('<img width="100" alt=(.*?)<div class="info">',re.S)
items=patt.findall(html)
print(len(items))
lianjie=[]
for i in items:
    new_p=re.compile('"(.*?)"',re.S)
    item=new_p.findall(i)
    item.remove('')
    lianjie.extend(item)
    for i in range(1,len(lianjie),2):
        qq=requests.get(lianjie[i])
        qq=qq.content
        with open('{}.jpg'.format(lianjie[i-1]),'wb') as ff:
            ff.write(qq)
print(lianjie[0])
print(len(lianjie))














