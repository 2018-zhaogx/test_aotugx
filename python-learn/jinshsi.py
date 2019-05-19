# import day13
# cc=day13.Xiaoai()
# cc.发短信()
# from day13 import Xiaoai
# cc=Xiaoai()
# cc.发短信()


# class zhishu():
#     def __init__(self,a=1000):
#         self.a=a
#     def zhihe(self):
#         cc=0
#         for i in range(2,self.a):
#             for j in range(2,i):
#                 b=i%j
#                 if b==0:
#                     break
#             else:
#                 cc += i
#         print(cc)
# zhishu().zhihe()
# k=[]
# import xlrd
# f = xlrd.open_workbook('a.xls')
# sheet = f.sheet_by_name('ttl')
# h=sheet.nrows
# lie=sheet.ncols
# for i in range(h):
#     for j in range(lie):
#         b = sheet.cell(i, j).value
#         k.append(b)
#         he=len(k)
# b=0
# with open('awenjian.txt','w',encoding='utf-8') as ff:
#     for ii in range(h):
#         for jj in range(lie):#0 1 2 3   0
#             ff.write('{} '.format(k[b]))#0 1 2 3
#             b += 1
#             if jj==lie-1:
#                 ff.write('\n')
# import xlrd
# f=xlrd.open_workbook('asd.xls')
# sheet=f.sheets()[0]
# num= sheet.nrows
# with open('b.txt','w',encoding='utf-8') as ff:
#     for i in range(num):
#         i =sheet.row_values(i)
#         for j,k in enumerate(i):
#             if j==len(i)-1:
#                 ff.write(k)
#             else:
#                 ff.write(k+' ')
#         ff.write('\n')
# a=[1,2,3,4]
# for i in a:
#     for j in a:
#         for k in a:
#             if i!=j and i!=k and j!=k:
#                 print('{}'.format(i*100+j*10+k))
# def aa(*args):
#     for i in args:
#         a=i+10
#         print(a)
# aa(22,11,2,3)
# def asd():
#     for i in range(1,101):
#         print(i)
#     return i
# print(asd())




#     将文件中的内容导入excel表格中：
# with open('C:\\Users\\www\\Desktop\\asd.txt','r',encoding='utf-8') as f:
#     a=f.read()
# b=a.split('\n')
# print(b)
# import xlwt
# ff=xlwt.Workbook()
# sheet=ff.add_sheet('ttl')
# for i in range(len(b)):
#     k=b[i].split(',')
#     for j in range(len(k)):
#         sheet.write(i,j,'{}'.format(k[j]))
# ff.save('ff.xls')




#将excel表格中的数据导入到txt文件中
# import xlrd
# ff=xlrd.open_workbook('c:\\Users\\www\\Desktop\\A.xls')
# sheet=ff.sheet_by_name('Sheet1')
# hang=sheet.nrows
# with open('ff.txt','w',encoding='utf-8') as f:
#     for i in range(hang):
#         d=sheet.row_values(i)
#         for k,l in enumerate(d):
#             f.write('{} '.format(l))
#             if k==len(d)-1:
#                 f.write('{}'.format('\n'))
#

# for i in range(1,1000):
#     c=0
#     for j in range(1,i):
#         if i%j==0:
#             c+= j
#     if c==i:
#         print(i)
# a=[1,2,3,'a',7]
# b=a.pop(0)
# a.append(b)
# print(a)
# a=[23,22,1,34,31]
# a.sort()
# print(a)

#买鸡
# for i in range(1,100):
#     for j in range(1,100):
#         for k in range(1,100):
#             if 2*i+1*j+0.5*k==100 and i+j+k==100:
#                 print(i,j,k)

# a=[str(x) for x in range(10)] +[chr(x) for x in range(97,103)]
# #a=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
# b=int(input('>>>'))
# f=''
# while True:
#     c=b%16
#     b=b//16
#     f=f+a[c]
#     if b==0:
#         break
# f=f[::-1]
# print('0x{}'.format(f))
# c=set()
# a=[1,2,3,4,5]
# b=6
# for i in a:
#     for j in a:
#         if i!=j:
#             v=i+j
#             if v==b:
#                 c.add(i)
#                 c.add(j)
# print(c)
#
# c=[]
# a=input('输入成绩，用空格隔开>>>')
# for kk in a:
#     if kk=='-':
#         print('成绩错误')
#         break
# else:
#     a=a.split(' ')
#     for i in a:
#         v=int(i)
#         c.append(v)
#     chengji=sum(c)//len(c)
#     for j in range(len(c)):
#          if chengji>c[j]:
#              print(c[j])

# a=[12,3,57,4]
# c=int(input('数字>>>'))
# a.append(c)
# a.sort()
# print#
def jiujiu():
    for i in range(1,10):  #2
        for j in range(1,i+1):#1 2
            print('{}*{}={}'.format(i,j,i*j),end='\t')
        print()

# def zhishu():
#     a=0
#     for i in range(2,101):
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             a += i
#     return a

# def jiechengzhihe(a):
#     c=0
#     b=1
#     for i in range(1,a):
#         b *= i
#         c += b
#     return c
# v=jiechengzhihe(6)
# print(v)
#三角形判断
# def sanjiaoxing():
#     a=input('输入三个数,空格分开>>>')
#     k=[]
#     a=a.split(' ')
#     for i in a:
#         i=int(i)
#         k.append(i)
#     k.sort()
#     print(k)
#     if k[0]+k[1]>k[-1]:
#         if k[0]**2+k[1]**2>k[-1]**2:
#             print('锐角')
#         if k[0]**2+k[1]**2==k[-1]**2:
#             print('直角')
#         if k[0]**2+k[1]**2<k[-1]**2:
#             print('钝角')
#     else:
#         print('错误')

# with open('asdfg.txt','w',encoding='utf-8') as f:
#     for i in range(1,10):
#         for  j in range(1,i+1):
#             f.write('{}*{}={}\t'.format(i,j,i*j))
#         f.write('\n')
# a=input('输入一串数字，空格分开>>>')
# a=a.split(' ')
# aa=set()
# for i in a:
#     aa.add(int(i))
# b=list(aa)
# b.sort()
# print(b)
# def huiwne():
#     a=input('请输入字符串>>>')
#     for i in range(len(a)//2):
#         if a[i]!=a[-1-i]:
#             print('不是')
#             break
#     else:
#         print('是回文')
#选择法
# a=input('输入一串数字，空格隔开>>>')
# a=a.split(' ')
# b=[]
# for k in a:
#    b.append(int(k))
# for i in range(len(b)):
#     for j in range(i+1,len(b)):
#         if b[i]>b[j]:
#             b[i],b[j]=b[j],b[i]
# print(b)
#冒泡法
#a=input('输入一串数字，空格隔开>>>')
# # a=a.split(' ')
# # for i in range(len(a)):
# #     for j in range(len(a)-1):
# #         if int(a[j])>int(a[j+1]):
# #             a[j],a[j+1]=a[j+1],a[j]
# # print(a)






#正则表达式  (re：正则)
# import re
# a='qwQe123qfwQeqst\nyfdqewqf123'
# #complie  编译，将[0-9]*编译成正则语言
# p= re.compile('[0-9]{2,4}')
# #findall 从某个地方查找所有符合正则的字符串（两种用法）
#      # findall如果有两个参数;()中第一个是正则条件，第二个是要查找的范围
# c=re.findall(p,a)
# print(c)
#      #findall如果有一个参数，参数是查找范围：格式c=p.findall(a)
# c=p.findall(a)
# print(c)
#注 ：如果只匹配指定的内容给你的正则条件加上()如下题
#只匹配两个f之间的内容
# p=re.compile('f(.*)f')
# #贪婪模式：尽可能匹配更多的内容
# p=re.compile('q(.*)q')#(结果不精细）
# #非贪婪模式：尽可能匹配少的内容
# p=re.compile('q(.*?)q')
# #########注：.(点)匹配不到换行符  给.(点)加权限:  re.S  如下例
# p=re.compile('q(.*?)q',re.S)
#re.I 给条件加功能，让正则条件不区分大小写(注：每个条件中只能加一个功能)
# p=re.compile('q(.*?)q',re.I)
# print(p)

import re
import requests

class Tupian(object):
    def 发送请求(self,page):
        #下面是网址
        url='https://www.qiushibaike.com/imgrank/page/{}/'.format(page)
        #换请求者名称
        head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}
        #发送请求
        res=requests.get(url,headers=head)
        #以utf-8格式接受源代码
        html=res.content.decode('utf-8')
        return html
    def 过滤(self,abc):
        lianjie=[]
        #正则条件
        patt=re.compile(r'<div class="thumb">(.*?)</a>',re.S)

        items=patt.findall(abc)
        for i in items:
            new_a=re.compile(r'<img src="(.*?)"')
            aaa=new_a.findall(i)
            lianjie.extend(aaa)
        return lianjie
    def save(self,shu):
        cc=[]
#图片是一个连接，请求图片的链接，将相应的保存
        for a,i in enumerate(shu):
            res=requests.get('https:'+i)
            #接受相应的结果只能用content
            qq=res.content
            print(qq)
            # try:
            #     with open('{}.jpg'.format(bb),'ab') as f:
            #         f.write(qq)
            #         bb=bb+1
            # except:
            with open ('{}.jpg'.format(a),'wb') as f:
                f.write(qq)

tu=Tupian()
ab=tu.发送请求(1)
sh=tu.过滤(ab)
tu.save(sh)
# tu=Tupian()
# for i in range(1,3):
#     ab=tu.发送请求(i)
#     sh=tu.过滤(ab)
#     tu.save(sh)























