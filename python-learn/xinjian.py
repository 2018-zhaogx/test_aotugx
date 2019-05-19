#！/usr/bin/python
#-*- coding:utf-8 -*-
# import paramiko
# #
# # ssh123 = paramiko.SSHClient()
# # #跳过验证，不到know_hosts文件中去查找
# # ssh123.set_missing_host_key_policy( paramiko.AutoAddPolicy)
# # #连接主机
# # ssh123.connect(hostname='192.168.1.14',port=22,username='root',password='123456')
# # #执行命令（注：只能执行有结果的命令 ）
# # stuin,stuout,stuerr=ssh123.exec_command('ls -ls')#exec（执行）command（命令）
# # #stuin执行的命令
# # #stuout执行的结果
# # #stuerr执行的报错
# # print(stuout.read().decode())
# # #断开连接
# # ssh123.close()

#
# def asd(a,b,c):
#     aa = list(a)
#     if b+c>len(a):
#         print(aa)
#         for i in range(len(aa)-b):
#             aa.pop(b)
#         cc=''.join(aa)
#         print(cc)
#     else:
#         for i in range(c):
#             aa.pop(b)
#         cc=''.join(aa)
#         print(cc)
# asd('qweqqwasd',1,3)

