#！/usr/bin/python
#-*- coding:utf-8 -*-




#创建日志
import os
import logging
import datetime


logs = os.path.join(r'E:\PycharmProjects\python-learn\appjiekouceshi1\src\logs', str(datetime.datetime.now().date())+".out")
print(logs)



#创建日志输出的格式
formatter=logging.Formatter(fmt='%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',datefmt='%d-%m-%Y:%H:%M:%S')
print(formatter)

#日志输出到控制台
con_handler=logging.StreamHandler()

#加载日志格式
con_handler.setFormatter(formatter)

#将日志输出到文本
fil_handler=logging.FileHandler(logs,encoding='utf_8')

#加载日志格式
fil_handler.setFormatter(formatter)

#定义一个函数（name是查看日志的文件名加后缀）
def log_rihzi(name):
    #获取文件名字传日志中
    logger= logging.getLogger(name)
    #加入一个手柄
    logger.addHandler(con_handler)
    logger.addHandler(fil_handler)

    #设置日志等级
    logger.setLevel(logging.INFO)

    return logger

# gg=log_rihzi('aiaiai.py')
# gg.info('hahahaha')






