#！/usr/bin/python
#-*- coding:utf-8 -*-
###连接linux的mysql数据库
# import pymysql
# conn=pymysql.connect(host='192.168.1.17',port=3306,user='root',password='123')
# abc=conn.cursor()
# abc.execute('use ssss')













import pymysql
conn = pymysql.connect(host='192.168.1.14',port = 3306,user ='root',password='123')
abc=conn.cursor()
abc.execute('use stu;')
abc.execute('show databases;')
abc.execute('select * from ar;')
a=abc.fetchall()
print(a)
conn.close()
print(a)


#数据库
#excle表格
#时间模块
#os模块
#爬虫
#文件的操作
#
