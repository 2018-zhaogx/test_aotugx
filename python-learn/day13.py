#！/usr/bin/python
#-*- coding:utf-8 -*-
#因数之和
# for i in range(1,1000):
#     b=0
#     for j in range(1,i):
#         if i%j==0:
#             b += j
#     if b==i:
#         print(i)

# for i in range(1,10):
#     for j in range(1,10):
#         for b in range(1,10):
#             if i**3+j**3+b**3
# a=input('>>')
# b= a.split(',')
# for i in range(1,len(b)):
#     for j in range(0,len(b)-i):#  注-i是为了提高运算速度
#         if int(b[j]) > int(b[j+1]):
#             b[j],b[j+1]=b[j+1],b[j]
#     print(b)
# a=input("以逗号分开>>>")
# b=a.split(",")
# c=[]
# for i in b:
#     c.append(int(b))
#     c.sort()
# def 函数名():
#     a=input('>>')
#     b= a.split(',')
#     for i in range(1,len(b)):
#         for j in range(0,len(b)-i):#  注-i是为了提高运算速度
#             if int(b[j]) > int(b[j+1]):
#                 b[j],b[j+1]=b[j+1],b[j]
#         print(b)
# #函数名()
# def bi(b):
    # print(a)
    # print(b)
    # print(c)
#     a=0
#     for i in range(b+1):
#         a += i
#     return 10,19
# c = bi(20)
# print(c+10)
#判断三角形
# a=input('以空格为分隔符>>>')
# b=a.split(' ')
# c=[]
# for i in b:
#     c.append(int(i))
#     c.sort()
# if c[0]+c[1]>c[2]:
#     if c[0]**2+c[1]**2>c[2]**2:
#         print('锐角')
#     elif c[0]**2+c[1]**2<c[2]**2:
#         print('钝角')
#     elif c[0]**2+c[1]**2==c[2]**2:
#         print('直角')
# else:
#     print('错误')

#a=['qweasd',]
#通过文件安装
#1   通过有网的设备到网络上下载模块的文件(.whl)
#2   将文件传输到无望的设备上
#3   在cmd下通过命令安装   3.1   3.2
#异常处理语句
#异常  ：因程序的逻辑或语法错误导致的程序中断
#异常处理：对讲要发生的异常进行预防
#try ...except...语句
#如果try里面的执行的语句报错就执行except里面的语句就执行，如果没有报错，except里面的语句就不执行
#例
# try:
#     a=10
#     print(a+b)
# except NameError as e:
#     print('hello')
#try...excpet...else 语句
#只要不执行except下面的语句就执行else 语句
#例
# try:
#     a=10
#     print(a+b)
# except Exception as e:
#     print('hello')
# else:
#     print(123)
# finally:
#     print(111)
#触发异常（又叫自定义异常）
#raise(可以为报错开关，只要遇到就报错语，终止语句执行) typeError('hello')   注释：和上下代码没有任何关系，
# a=int(input('>>>'))
# if a>3:
#     raise NameError('hello')
# else:
#     raise TypeError('123')
#将数字转换成ASCII表中的字符
#print(chr())
#将ASCII表中的字符转换成数字
#print(ord())
#hex()十进制转十六进制
#oct()转八进制
#bin()转二进制
#int()任何进制转十进制
# for n in range(100,1000):
#     i = n // 100
#     j = n // 10 % 10
#     k = n % 10
#     if n == i ** 3 + j ** 3 + k ** 3:
#         print(n)
# def shiliu(y):
#     b =[str(i) for i in range(0,10)]
#     a =['{}'.format(chr(i)) for i in range(97,103)]
#     b.extend(a)
#     n=[]
#     while True :
#         if y >= 16:
#             c =y%16
#             y //=16
#         elif y < 16 and y !=0:
#             n.insert(0,y)
#             break
#         n.insert(0,c)
#     n = [b[i] for i in n]
#     n.insert(0,'0x')
#     return ("".join(n))
#    面向对象：将函数进行分类和封装，使其开发更高效
#  1、类(class)   创建一个类   class
#例
# class Xiaoai():
#     def 打电话(self):
#         print('打电话')
#         self.__发短信()
#     def __发短信(self):
#         print('发短信')
#     def 放歌(self):
#         print('放歌')
# Xiaoai().打电话()
#类名==函数名规则  》》》为了跟函数区分，默认的雷鸣首字母大写
#2、对象，也叫类的实例      方便在类的外部调用函数
#调用类里面的函数 ---格式  ：类名().函数名()     注：函数名是类里面的函数
#self 不属于函数的参数，self是类的实例，方便在类的内部调用函数
#3、  继承 :新的类继承旧的类中所有的函数
#多继承
#
# ai=小娜(a)
# ai.asd()
#4、多态（函数重写）  更改继承类中的某些函数的功能(如上)
#5、私有方法  将类中的函数变成私有函数,不允许继承
#在函数的前面加两个下划线__
# class hanshu():
#     def zhishuzhihe(self,a,b):
#         for i in range(a,b+1):
#             for j in range(2,i):
#6、   专有方法(函数)  ：类的专有函数，只要你是一类，都有的函数
#      __int__  任何一个类都有属性和方法
#属性：类中的方法具有的共同的特点（类似每个人都有身高和体重）





##########################
#对excel表格的操作
#读写追加
#向Excel表格中写入数据
#import xlwt   #批量操作
#打开一个空白excel的文件
#f=xlwt.Workbook(encoding='utf-8')#注：编码格式可以不写
#添加一个标签页(注：下面括号中是标签页的名称)
#sheet=f.add_sheet('python_test')
#向标签页中写入数据
#sheet.write(0,0,'写入的内容')#  注：第一个数字是行，第二个数字是列，都是从零开始；第三个是写入的内容
#保存该文件
#f.save('a.xls')
# import xlwt
# f=xlwt.Workbook()
# sheet=f.add_sheet('python_test')
# for i in range(1,10):
#     for j in range(1,i+1):
#         sheet.write(i-1,j-1,'{}*{}={}'.format(i,j,i*j))
# f.save('asd.xls')

# import xlwt
# ff=xlwt.Workbook()
# sheet=ff.add_sheet('python_test')



#将文件内容导入到excel表格中
#1、
# d = []
# with open('cc.txt','r',encoding='utf-8') as ff:
#     a = ff.read()
#     b=a.split('\n')
#     hang=len(b)
#     for i in b:
#         c=i
#         e=c.split(',')
#         lie=len(e)
#         d.append(e)
# import xlwt
# f = xlwt.Workbook(encoding='utf-8')
# sheet = f.add_sheet('python_tset')
# for i in range(len(b)):
#     for j in range(len(e)):
#         sheet.write(i, j, '{}'.format(d[i][j]))
# f.save('a.xls')
# #2、
# import xlwt
# with open('cc.txt','r',encoding='utf-8') as f:
#     a=f.read()
# a=a.split('\n')
# ff=xlwt.Workbook()
# sheet=ff.add_sheet('ttl')
# for i in range(len(a)):
#     k=a[i].split(',')
#     for j in range(len(k)):
#         sheet.write(i,j,k[j])
# ff.save('a.xls')






# #读取excel表格中的数据
# import xlrd
# #打开读取的excle表格的数据（注：文件不在同路径要加路径）
# f=xlrd.open_workbook('a.xls')
# #获取表格文件中有多少个标签页
# b=f.nsheets
# print(b)
# #获取表格中所有标签页的名称
# b=f.sheet_names()
# print(b)
# #进入要读取的标签页（两种方法）
# #1、
# #sheet=f.sheet_by_name('sheet1')#注：括号中为标签页名称
# #2、
# #通过索引值来进入操作的标签页
# sheet=f.sheets()[0]  #注：中括号中的数字为下标号(sheet是变量名)
# #读取标签页中的第几行
# b=sheet.row_values(0)   #
# print(b)
# #获取表格文件(标签页)中有多少行   row:是行
# c=sheet.nrows
# print(c)
# #读取表格文件（标签页）中第几列   col:是列
# b=sheet.col_values(0)
# #读取标签页中有多少列
# c=sheet.ncols
# print(c)
# #值读取某一个格子的数据
# for i in range(2,12):
#     b=sheet.cell(i,6).value   #注：cell是单元格
#     print(b)
# k=[]
# import xlrd
# f = xlrd.open_workbook('asd.xls')
# sheet = f.sheet_by_name('python_test')
# h=sheet.nrows
# lie=sheet.ncols
# for i in range(h):
#     for j in range(lie):
#         b = sheet.cell(i, j).value
#         k.append(b)
# b=0
# with open('c.txt','w',encoding='utf-8') as ff:
#     for ii in range(h):
#         for jj in range(lie):#0 1 2 3   0
#             ff.write('{} '.format(k[b]))#0 1 2 3
#             b += 1
#             if jj==lie-1:
#                 ff.write('\n')












# #包和模块的区别
# #对excel表格的追加
# #用的函数
# from xlutils.copy import copy#xlutils.copy路径
# import xlrd#   读取文件
# #  打开文件
# f = xlrd.open_workbook('a.xls')#  注：此处的  f  可执行xlrd的所有权限
# #复制文件
# new_f=copy(f)#复制一份文件，对新文件进行操作  (复制的new_f文件只有写入的权限）
# #获取要操作大的标签页（注：是对新复制的文件进行操作）
# sheet = new_f.get_sheet(0)#注：括号中的为标签页的下标号
# #sheet = new_f.sheet_by_name('sheet1')
# #追加内容
# sheet.write(7,0,'人生苦苦短')#不能给元格中有内容的的进行追加，如果追加自会覆盖原有的内容
# #删除表格中单元格中内容
# sheet.write(7,0,'')#注''英文单引号
# new_f.save('a.xls')#  注：保存文件名还是原来打开的文件名，如保存不是原来的文件名，则会新创建一个文件（而不是追加文件）
#
# # from xlutils.copy import copy
# # import xlrd
#





# #时间模块
#import time
# #时间戳
# #表示是从公元1970年8点开始到现在经过的秒数
# a= time.time()
# print(a)
#以元组的格式显示本地时间
#a=time.localtime()
# # 默认的是本地时间，如果传入参数（只能是时间戳———秒），显示的就是传入的参数的时间
# a=time.localtime(8999999999)
##wday表示周几，yday表示今年第几天（阳历），isdst表示夏令时（0不是1是）
# #以本地化显示时间
# b=time.strftime('%Y-%m-%d %H:%M:%S %w %j')# 注：大写H,M,S小时分钟秒，w周几，j一年的第几天
# print(b)
# #也可以传入参数是（参数是本地化时间）
# c=time.strftime('%Y-%m-%d %H:%M:%S %w %j',a)
# print(c)
#
# #将元组时间转换为时间戳(必须是9个参数,但只用前六个参数)
# a=(2019,12,1,23,13,2,35,23,33)
# b=time.mktime(a)
# print(b)
# #将现代时间转化为元组时间
# a=time.strptime('2019-12-12','%Y-%m-%d')
# print(a)
# #程序休息几秒(括号中为数字秒)
# time.sleep(9)
# #  例
# for i in range(10):
#     print(i)
#     time.sleep(2)


# a=input('输入年份空格分开>>>')
# import time
# a=time.strptime(a,'%Y %m %d')
# b=time.strftime('%Y-%m-%d-%w',a)
# cc=b.split('-')
# nianfen=int(cc[0])
# if nianfen%4==0 or nianfen%400==0:
#     print('是闰年')
#     print(cc[-1])
# else:
#     print('不是')
#     print(cc[-1])





# 手动输入一个日期打印出前一天
# a= input('输入一个日期,杠分开>>')
# import time
# a=time.strptime(a,'%Y-%m-%d')
# b=time.mktime(a)
# c=b-86400
# d=time.localtime(c)
# b=time.strftime('%Y-%m-%d %H:%M:%S %w %',d)
# print(b)




#爬虫：模仿浏览器，根据自己指定的规则批量下载网上的数据（用的模块requests）
#分类：1、聚焦爬虫(只针对某个网站进行爬虫)2、搜索爬虫（针对全网搜索进行爬虫）类似搜索引擎
#能够模仿浏览器：requests  urllib  urllib2\3  httpclient
#根据自己制定的规则的模块：re，BeautifuilSoup,Xpath
#写爬虫的步骤
######## 1、分析网址




#https://www.qiushibaike.com/text/page/3/
#class pachong():
# import requests
# import re
# oo={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
# }#
# for p in range(1,11):
#     a='https://www.qiushibaike.com/text/page/{}/'.format(p)
# #发送请求
#     b=requests.get(a,headers=oo)  #headers=oo应对开发的>>反爬技术
# #接受响应(读取响应)   1、text(以文本的方式读取）  2、content(以字节的方式接受)
# #c=b.text  #网页源代码
#     c=b.content.decode('utf-8')#  网页编码方式查看：网页的源代码中找meta的行尾显示编码方式
#
# ######2、
#
# #2、过滤
#     d=re.compile('<div class="content">(.*?)</span>',re.S)
#     f=d.findall(c)
#     ff=[]
#     for i in f:
#         i=i.replace('<span>','')
#         i=i.strip()
#         i=i.replace('<br/>','')
#         ff.append(i)
# with open('ac.txt','a',encoding='utf-8') as f:
#     for i in ff:
#         f.write(i+'\n')
# # 爬虫会服务器造成压力，所以有反爬程序


#
# #爬虫：爬取的资源任何资源，html文件，静态网页
# #动态网页：资源不在html文件中的，实时动态刷新的
# #加载网页资源     (浏览器中 按f12进入
# # 加载网页的方式（两种) JavaScript（都在JS中）   ajajx（都在XHR中）
# import requests
# import json #json是一种轻量级的数据传输格式
# #python 不认识json的数据，就认为是字字符串
# url='https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=12&city=410200'
# res=requests.get(url)
# qwe=res.text
# asd=json.loads(qwe)  #将json格式转化为字典
# #qwe=json.dumps(asd)  将字典转换成json格式
# print((asd['dats']['poi_list'][0]['address']))
#
#
#
#
#
#
#
#
#
# import pymysql
# #连接数据库(变量名一般为conn)
# conn=pymysql.connect(host='192.168.1.11',port=3306,user='root',passwd='123456')
# #创建游标(变量名一般为abc)  类似于vim中光标  vim a.out
# abc=conn.cursor()
# #执行sql语句
# abc.execute('show databases;')
# #fetchall 获取上一个sql语句的结果
# a=abc.fetchall()
# print(a)
# abc.execute('use qwe;')
#
#
# #abc.execute('create table py_test1(姓名 char(225),年龄 int,性别 char(225));')
# abc.execute('show databases;')
# print(abc.fetchall)
# #abc.execute('insert into py_test1 values("小明",90,"女"),("小刚",100,"男");')
# #事务（提交）
# #conn.commit()
# abc.execute('select * from py_test1;')
# print(abc.fetchall())
# for i in range(100):
#     abc.execute('insert into py_test1 valuees("{}",{},"{}");'.format("小明",100,"王"))
# abc.execute('select * from py_test1;')
# print(abc.fetchall())
# #获取上一个sql语句的结果(默认值获取结果中的第一条数据）
# #传入参数是一个数字，数字是几就获取几条sql语句的结果（注：如向一个表格中添加10行数据，要显示3行sql语句显示的是添加的前3行数据）
# a=abc.fetchmany(2)
# #每次只获取一条结果，本身有迭代的功能，不会重复，可以写多次（和readline性质一样）
# a=abc.fetchone()
# b=abc.fetchone()
# print(a.b)
# #断开连接
# conn.close()
#
#
#
# #自带的库，是与操作系统交互的
# #通过os模块来（间接）控制操作系统（如python不能直接用代码删除一个文件)
# import os
# #删除文件
# #os.remove('a.txt')
#
# #popen可以执行Windows命令（相当于在cmd中)
# b=os.popen('ping 192.168.1.1')
# print(b)
# # b=os.popen('ipconfig/all')
# # print(b.read())
#
#
#
# #获取当前所在的位置
# print(os.getcwd())
#
#
# #切换路径
# # os.chdir(r'D:')#注：r:是转义字符(路径需转义)
# # os.chdir(r'/')#切换到当前根目录
# print(os.getcwd())
# #获取当前目录下面的文件（列表显示）
# print(os.listdir('.'))





#当前目录下有多少个.py文件
# a=os.listdir(r'.')
# c=0
# for i in a:
#     if i.endswith('.py'):
#         c +=1
# print(c)

#薪资、公司名称、招聘岗位、工作地点、工作经验、学历、发布日期
#放excel











#
# import os
# #将文件与路径分隔开
# a=os.path.split(r'‪C:\Users\www\Desktop\脚本(6)(2).docx')
# print(a)
# #将文件的后缀名与路径分隔开
# a=os.path.splitext(r'‪C:\Users\www\Desktop\脚本(6)(2).docx')
# print(a)
#
# #判断文件是否是个目录(注：不是当前路径要加路径)
# b=os.path.isdir(r'e:\QQ文件夹')
# print(b)
# #判断文件是否是个普通文件(注：不是当前路径要加路径)
# b=os.path.isfile('asd.py')
# print(b)
#
# #创建文件夹
# os.mkdir('aaaaaa')
# #创建递归文件夹
# os.mkdirs('bbb/ccc/ddd')
#
# #删除空文件夹
# os.rmdir('aaaaaa')
# #删除递归文件
# os.removedirs('bbb/ccc/ddd')








#模：块：是一个.py文件   封装的代码、 函数
#包：是一个目录，封装的是模块，必须含有__init__.py文件



#面向对象和面向过程的区别
#面向过程：一步一步的通过代码来实现解决问题的步骤、、、性能高，不易维护，性能高
#面向对象：将函数进行分类封装，使开发更高效、、、易扩展，易维护，性能比较低


# #
# # #下载paramiko模块
# # #创建一个远程客户端
# import paramiko
# #
# # ssh123 = paramiko.SSHClient()
# # #跳过验证，不到know_hosts文件中去查找
# # ssh123.set_missing_host_key_policy( paramiko.AutoAddPolicy)
# # #连接主机
# # ssh123.connect(hostname='192.168.2.151',port='22',username='root',password='123456')
# # #执行命令（注：只能执行有结果的命令 ）
# # stuin,stuout,stuerr=ssh123.exec_command('ls -ls')#exec（执行）command（命令）
# # #stuin执行的命令
# # #stuout执行的结果
# # #stuerr执行的报错
# # print(stuout.read().decode())
# # #断开连接
# # ssh123.close()
#
# # a=input('输入命令，输入exit退出：')
# # import paramiko
# # ssh123=paramiko.SSHClient()
#
#
# # #用它来传输文件
# # #先建立一个通道
# # ssh123=paramiko.Transport(('192.168.2.151',22))#注两个括号中填写的是要连接的主机ip和端口号
# # #连接主机
# # ssh123.connect(username='root',password='123456')
# # #创建一个sftp客户端
# # sftp=paramiko.SFTPClient
# # #从linux下载文件到Windows上   不在同路径的要加路径
# # sftp.get('anaconda-ks.cfg','anaconda-ks.cfg')#注get是下载
# # #从Windows上传文件到linux
# # sftp.put('day1.py','/home/day1.py')#注put是上传
# # ssh123.close()
#
#
#
#
#
# #用代码发送邮件
#
# import smtplib  #简单邮件传输协议，，封装了smtp协议
# import email.mime.multipart#
# import email.mime.text#处理邮件中的正文
# #发件人
# fr='17637897624@163.com'
# #收件人
# res='lp109314@163.com'
# #服务器
# server='smtp.163.com'
# #授权码   授予登陆客户端的权限的密码
# password='zgx987'
# #创建一个空邮件
# message=email.mime.multipart.MIMEMultipart()
# #给邮件里添加一个发件人
# message['from']=fr
# #添加一个收件人
# message['to']=res
# #添加一个主题
# message['Subject']='python-learn'
# #写邮件正文
# text="哈哈哈哈，傻逼愚人节快乐！！！！"
#
#
#
#
# # 添加附件
# att2 = email.mime.text.MIMEText(open(r'C:\Users\www\Desktop\573458806.jpeg', 'rb').read(), 'base64', 'utf-8')
# att2["Content-Type"] = 'application/octet-stream'
# att2["Content-Disposition"] = 'attachment; filename="c:\\Users\\www\\Desktop\\573458806.jpeg"'
# ## 头部字段
# message.attach(att2)
#
# #处理正文文本
# txt=email.mime.text.MIMEText(text)
# message.attach(txt)
# #定义一个服务器
# smtp123=smtplib.SMTP_SSL(server,465)
# #登陆服务器
# smtp123.login(fr,password)#注密码是授权码
# #发送邮件
# smtp123.sendmail(fr,res,message.as_string())
# #断开连接
# smtp123.close()















#########socket
#套接字，提供了通信双方最底层的功能（发送和接收）
#如只管tcp/ip  的通信接收和发送，不管发送的内容


#两台主机实现通信

#server端  >百度服务器

import socket
#创建一个套接字，意为：创建一个有发送能力和接收能力的东西
#注下面括号中不写东西默认是使用的tcp和ipv4
#tcp:SOCK_STREAM   udp:SOCK_DGRAM
#这个套接字使用的是tcp协议和ipv4
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定ip地址(自己的）和端口号(随便写)
s.bind(('192.168.1.6',80))#接收的是个元组
#监听服务有没有开启
s.listen(3)#括号中的3表示最大的等待个数
while True:
    #接收请求，建立连接
     #第一个值是建立连接的信息（连接的通道）
     #第二只是客户端的ip地址和端口号
    client,addr = s.accept()
    #接收客户端发送的请求,1024每次接收的最大字节
    a=client.recv(1024)
    print(a.decode('utf-8'))
    #发送响应
    reg=input('>>>')
    #reg='吃过了'
    client.send(reg.encode('utf-8'))



# #通过UDP建立连接
# #服务器端
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(('192.168.1.6',8806))
# #z
# while True:
#     #第一个参数是哭护短的请求数据
#     #第二个是客户端的ip和端口号
#     client,addr=s.recvfrom(1024)
#     print(client.decode('utf-8'))
#     msg=input('>>>')
#     #msg='hello'
#     s.sendto(msg.encode('utf-8'),addr)#注此处用的是sendto 和s(套接字)







