# ！/usr/bin/python
# -*- coding:utf-8 -*-

# #print('hello word')
# #a=4
# #print(a)
# #d = input('请输入密码:')
# #print(d)
# #print('hello')
# #c=False
# #print(type(c))
# #c='qwertyuiopasdfghjklzxc'
# #print(c[5::])
# #   字符窜的内置函数
# #a='asd123'
# #将字符串小写变大写
# #b=a.upper()
# #print(b)
# #将大写变小写
# #b=a.swapcase()
# #a='qwe123'
# #将字符串中的某个字符更改成其他数据
# #b=a.replace('qwe','110')
# #print(b)
# a = 'qwqeqcqr1123q'
# #b=a.replace('q','0',2)
# #print(b)
# #b=a.endswith('q')
# #print(b)
# #{}大括号填充
# a= '我叫{name},今年{age}岁'
# b='qwe'
# q=20
# c=a.format(name=b,age=q)
# print(c)
# #%填充
# #a='我叫%s,今年%d岁'
# #b=input('请输入名字')
# #c=input('请输入年龄')
# #c=int()
# #d=a %(b,c)
# #print(d)
# a=' qwer '
# print(a)
# b=a.rstrip()
# print(b)
# a= 'qwersdsga gaf '
# #print(len(a))
# print(a[1])
# print(a[::2])
# print(a[:2])
# b=a.count('g')
# print(b)
# a=(1,23,22,32423,45,35,23462,2365,2,236,235,25)
# #b=a.index(35)
# print(len(a))
# # ziuhgia
# # ijoaijgioaaihg
# # uaihgiujssz
# # aiwhgizsl
# # aishfois
# a=[1,2,3,43,532,235,45,65]
# print(a[-2])
# a.append(999)
# print(a)
# a.insert(2,888)
# print(a)
# print(a[])
#a = [20, 5, [23, [21,30],45,55]
# # a.remove(20)
# # print(a)
# # a.pop(0)
# # print(a)
# # a.clear()
# # print(a)
# b=a.copy()
# a.append(100)
# print(b)
# print(a)
#     集合(set)
# a={23,34,45,56,67,353253}
# print(type(a))
# print(a)
# a.add(2222)
# print(a)
# a={'name':[123,234,123],'age':20}
# print(a.values())
# a='123'
# a=tuple(a)
# pr    print(False)int(a)
# print(type(a))
# a =4+3
# print(a)
# a=5
# if a>6:
#     print('你好')
# elif a<6:
# a=input('请输入成绩：')
# a=int(a)
# if a>=60 and a<70:
#     print("及格")
# elif a<60 and a>0:
#     print("不及格")
# elif a>=70  and a<90:
#     print("良好")
# elif a>=90  and a<=100:
#     print("优秀")
# else:
#     print("错误")
# a=input('请输入一个数：')
# a=int(a)
# if a%2==0:
#     if a%3==0:
#         print('hello world')
#    print('hello')
# elif a%2!=0:
#     if a%3==0:
#         print('world')
# elif a%2!=0:
#     if a%3!=0:
#         print(123)
# print(123)
# e=input('请输入一个字符串：')
# if e[0]=='a' or e[0]=='A' and e[-1]=='c':
#     print(110)
# elif e[0]=='a':
#     print(120)
# elif e[-1]=='c':
#     print(130)
# else:
#     print(250)
# if e[0]=='a' or e[0]=='A':
#     if e[-1]=='c':
#         print(110)
# elif e[0]:
#     print(120)
# elif e[-1]=='c':
#     print(130)
# else:
#     print(250)
# a=110123
# b=a.replace(110,111)
# print(b)
# a=0
# for i in range(1,10):
#     if i==7:
#         continue
#     print(i)
# else:
#     print('hello')
#计算1-2+3-4+5...-98+99=?
# a=0
# for i in range(1,100):
#     if i%2==0:
#         a=a-i
#     else:
#         a=a+i
# print(a)
#三次猜数字，0-10的随机产生一数字（10除外）
# import random
# a = random.randrange(1,10)
# print(a)
# for i in range(1,4):
#     b=int(input('>>>:'))
#     if b>a:
#          print('大了,还有%d次机会' %(3-i))
#     elif b<a:
#         print('小了,还有%d次机会' %(3-i))
#     else:
#          print('ok')
#          break
# else:
#     print('废物')
# a=[11,22,66,44,55,44,33,77,88,99]
# b,c=[],[]
# for i in a:
#     if i > 55:
#         b.append(i)
#     else:
#         c.append(i)
# print(b)
# print(c)
# for i in range(1,10):
#     for j in range(1,10):
#         if j<=i:
#             print('{}*{}={}'.format(i,j,j*i),end='\t')
#     print()
# l=[]
# for i in range(2,101):
#     for j in range(2,101):
#         if i%j==0:
#             break
#     if i==j:
#         l.append(i)
# print(sum(l))
#质数之和，因数之和，9*9乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(j,i,j*i),end='\t')
#     print('')
# l=[]
# for i in range(2,101):
#     for j in range(2,i+1):
#         if i%j==0:
#             break
#     if j==i:
#         l.append(i)
# print(sum(l))
# for i in range(1,1001):
#     c=[]
#     for j in range(1,i):
#         if i%j==0:
#             c.append(j)
#             sum(c)
#     if sum(c)==i:
#         print(i)
# c=0
# for i in range(1,6):
#     for j in range(1,i+1):
#         b=i*j
#         c=c+b
# print(c)
# a,b=1,0
# # for i in range(1,6):
# #     a *= i   #a=a*i   1*1 1*2 2*3
# #     b += a
# # print(b)
#shuixianhuashu
# for i in range(100,1000):
#     b=i //100
#     c=i //10 %10
#     b=i%10
#     if b**3+c**3+b**3==i:
#         print(i)



#
# a,b,c=int(input('>>>'))
#
#
# if a**2+b**2>c**2 or :
#     print('锐角三角形')
# elif a**2+b**2<c**2:
#     print('钝角三角形')
# else:
#     print('直角三角形')
#a=30
#for i in range(1,31):
#    if i> 20:
#        print('hello')
#        i -= 1
# b=100
# c=0
# while b>0:
#     c=c+b
#     b=b-1
# print(c)
# print('>>请输入数据<<')
# a=str(input('空格隔开:'))
# l=[]
# ll=a.split(' ')
# i=0
# while i <= len(ll)+1:
#     l.append(int(ll.pop()))
#     i+= 1
# print('平均数：',sum(l)/len(l))
# b=sum(l)/len(l)
# for v in l:
#     if b > v:
#         print('小于平均数的有：',l)
# while True:
#     c=[]
#     a=input('输入数据，空格隔开:')
#     if ' ' in a:
#         b=a.split(' ')
#         for i in b:
#             c.append(int(i))
#         d = sum(c)/len(c)
#         print('平均数:{}' .format(d))
#         for j in c:
#             if d>j:
#                 print('低于平均分：{}' .format(j))
#     else:
#         break
 #       print(b)
# a=0
# for i in range(2,100):
#     for j in range(2,i):#i=4  j=2,3
#         if i%j==0:
#             break
#     else:
#          a=a+i
# print(a)
# a=int(input('请输入一个数：'))
# b=0
# for i in range(2,a):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         b += i
# print(b)
# a=int(input('任意数：'))
# b=0
# c=1
# for i in range(1,a):
#     c *= i
#     b += c
# print(b)
# a=input('请输入开头')
# b=input('请输入开头')
# if i in a:
# a.swapcase(a)
#判断字符串是否回文
# a= input('请输入一串字符串>>>')
# b=len(a)
# for i in range(b//2):
#     if a[i] != a[-i-1]:
#         print('不是回文')
#         break
# else:
#     print('是回文')
#         print(j)
# a='1234'
# a=a[::-1]
# b=0
# for i in range(len(a)):
#     for j in range(10):
# a=[i+2 for i in range(10) if i >6 and i<9]
# print(a)
# a=['{}*{}={}'.format(i,j,i*j) for i in range(1,10) for j in range(1,i+1)]
# print(a)
# a=lambda x=10,y=12:x+y
# a()
# def a(x=10,y=20):
#     return x+y
# print(a())
# a=lambda x,y:x+y
# b=lambda x,y:x-y
# c=lambda x,y:x/y
# d=lambda x,y:x*y
# print(a(40,20))
# print(b(40,20))
# print(c(40,20))
# print(d(40,20))
# f=open('C:\\Users\\www\\Desktop\\a.txt','r',encoding='utf-8')
# print(f.read())
# jj=open('cc.txt','w',encoding='utf-8')
# for i in range(1,31):
#     jj.write('{}\n'.format(i))
# jj.close()
# jj=open('cc.txt','w',encoding='utf-8')
# for i in range(1,10):
#     for j in range(1,i+1):
#         jj.write('{}*{}={}\t'.format(i,j,i*j))
#     jj.write('\n')
# jj.close()
#读(r)  读取文件中的内容
#read():读取文件中的所有的内容，以字符串格式显示(一个字符串）
# readlines()：读取文件中的所有内容，以列表格式显示(一个列表)
#  readline()：读取文件中的内容，每次只读取一行（可以多次读取，只能往下读取
# jj=open('cc.txt','r',encoding='utf-8')
# print(jj.readline())
# print(jj.readline())
#w+，r+,a+
#wd  rd ad 以二进制的方式
# a=input('字符串>>')
# for i in range(len(a)//2):
#     if a[i]!=a[-i-1]:
#         print('不是回文')
#         break
# else:
#     print('回文')
#将字符串改为数字不用int
# a='123456'
# b=0
# a=a[::-1]
# for i in range(len(a)):
#     for j in range(10):
#         if str(j)==a[i]:
#             b=b+j**i
# print(b)
# j=open(r'‪C:\Users\www\Desktop\QQ图片20190223163339.jpg','rb')
# print(j.read())
#打印列表中第二大和最大
# a=[9,8,5,9,8,5]
# import copy
# b=set(copy.deepcopy(a))
# c=list(b)
# for i in range(len(c)):
#     for j in range(i+1,len(c)):
#         if c[i]>c[j]:
#             c[i],c[j]=c[j],c[i]
# for d in range(len(a)):
#     if a[d]==c[-1]:
#         print('最大数',a[d])
#         continue
#     elif a[d]==c[-2]:
#       print('第二大数',a[d])
#with语句：叫做上下问管理器
# 作用：来主动释放占用的资源
#with语句两个机制：enter(进入)    exit(退出)
#格式：with 操作的对象  as  变量名
# if __name__=='__main__':
#     with open('cc.txt','w',encoding='utf-8') as f:
#         f.write('123')
#         f.write('qweav')
#         f.close()
#     with open(r'E:\QQ文件夹\W36W{D@~P7@L1LI6W9G4JU7 (1).jpg','rb') as ff:
#         print(ff.read())
#import 语句：
#意为导入语句：将其他python文件中的代码导入到本文件执行
#格式：  import 文件名：   导入文件的所有代码（注：文件名不要加后缀名）
def qqqq(a):
    b=0
    for i in range(1,a+1):
       b += i
    return b,123,423
# d,f,g=qqqq(100)
# print(d,f,g)
#from 文件名  import 函数名  ：只导入文件中的某个函数
# if __name__ =='__main__':    判断执行的文件是否是本文件
#在python中，类似导入day1.py,day2.py这些文件，都叫————模块
#python自带的模块  os，re
#第三方模块


#下载方式：
#1、pip下载   在cmd中输入pip install 模块名
#pymysql
#pip 不是内部或者外部命令：pip程序不在环境变量中
#                      将pip路径手动加入环境变量
#pip是python自带的一个下载模块的组件
#通过pycharm安装
import paramiko





# with open('asd.py','r',encoding='utf-8') as f:
#     b=f.read()
#     c=f.read().count('\n')
#     print(c)
# f = open('qwe','r',encoding= 'utf-8')
# a = f.readlines()
# for i in range(a.count('\n') ):
#     a.remove('\n')
# for j in a:
#     if j.startswith('#'):
#         a.remove(j)
# print(len(a))
# f.close()
# a,b=0,1
# for i in range(1,6):
#     b *= i
#     a+=b
# print(a)
# with open('asd.py','r',encoding='utf-8') as f:
#     b=f.readlines()
#     c=len(b)
#     for i in b:
#         if i.startswith('#') or i =='\n':
#             c -= 1
#     print(c)
# a=[1221342,123,34353,9564,999,999]
# b=a.copy()
# b=list(set(b))
# b.sort()
# for i in b:
#     if i==b[-1] or i==b[-2]:
#         print(i)
#冒泡法
# a=input('输入数字，一空格分开')
# b=a.split(' ')
# c=len(a)
# for i in range(c):
#     for j in range(i+1,c+1):
#         if i>j:
# def jinzhi12(ooo):
# ooo =input('输入一个十进制数')
# aa=[A,B,C,D,E,F]
# ee=[0,1,2,3,4,5,6,7,8,9]
# bbb=int(a)
# ccc=bbb//15
# ddd=bbb%15
# if ddd>9:
#     dd=ddd-9-1
# elif ddd<=9:
#     dd=ddd
# if 9<ccc<16:
#     cc=ccc-9-1
# elif ccc<10:
#     cc=ccc
# elif ccc>15:
#     cc=111
# m=[]
# a=int(input('>>>'))
# b=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
# while True:
#     if a<16:
#         m.append(b[a])
#         break
#     elif a>=16:
#         c=a%16
#         d=a//16
# #        a=c
#         m.append(b[d])
# m.sort(m)
# print(m)
# a=[10,20,90]
# for i in a:
#     if i <0:
#         print('报错请重新输入',i)
#
#     b=sum(a)/len(a)
#     print('平均成绩：',b)
#     break
#     elif i < b:
#         print('低于平均成绩：',i)
#         break
# a=[90,10,20]
# print(sum(a))
#十进制转十六进制
#a=[str(x) for x in range(10)] +[chr(x) for x in range(97,103)]
# a=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
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
#结束
#数字去重排序
c=set()
a=input('输入一串数，空格为分隔符>>')
b=a.split(' ')
for i in b:
    c.add(i)
c=list(c)
c.sort()
print(c)
#结束
x=''
a = input('>>>输入任意四个数,空格分开')
b=a.split(' ')
for i in b:
    b.remove(i)
    for j in b:
        b.remove(j)
        for z in b:
            x=i+j+z
            print(x)
