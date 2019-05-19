#！/usr/bin/python
#-*- coding:utf-8 -*-
# import pymysql
# conn=pymysql.connect(host='192.168.2.151',user='root',password='123')
# abc=conn.cursor()
# abc.execute()
# conn.commit()
# a=abc.fetchall()
# import xlwt
# f=xlwt.Workbook()
# sheet=f.add_sheet('sheet1')
# sheet.write(0,0,'sfs')
# f.save('a.xls')
# import xlrd
# from  xlutils.copy import copy
# f=xlrd.open_workbook('a.xls')
# sheet=f.sheets()[0]
# nuw=sheet.nrows
# sum=sheet.ncols
# new_f=copy(f)
# sheet=new_f.get_sheet(0)
# #os模块
# import os
# os.remove('a.txt')#删除文件
# os.popen('windows命令')#连接Windows系统的cmd
# os.getcwd()#查看当前路径
# os.chdir('路径')#切换路径
# os.listdir('.')#查看当前路径的文件名加后缀
# #选择法
# a= [23,123,45,21]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)
#
import time
import os
os.mkdir('aaa987')
os.chdir('./aaa987')
for i in range(10):
    with open('{}.txt'.format(i),'w',encoding='utf-8') as ff:
        for j in range(10,20):
            ff.write('{}'.format(i)+'\n')
time.sleep(10)
for i in range(10):
    os.remove('{}.txt'.format(i))
os.chdir('../')
os.rmdir('aaa987')

#paramiko模块
# import paramiko
# ssh123=paramiko.SSHClient()#创建一个客户端
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy)#跳过验证
# ssh123.connect(hostname='192.168.2.151',port='22',username='root',password='123456')
# stuin,stuout,stuerr=ssh123.exec_command('ls -ls')
# print(stuout.read().decode())
#
#
# import paramiko
# ssh123=paramiko.SSHClient()
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# ssh123.connect(hostname=,port=,username=,password=)
# stuin,stuout,stuerr=ssh123.exec_command('ls -ls')
# print(stuout.rand().decode())
# ssh123.close()

#用paramiko模块来互传windows 和linux的文件
import paramiko
ssh123=paramiko.Transport(('192.168.2.151',22))#
ssh123.connect(username='root',password='123456')
sftp=paramiko.SFTPClient
sftp.get('linux文件','windwos存放路径')
sftp.put(windows文件,linux存放路径)




