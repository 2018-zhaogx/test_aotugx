#！/usr/bin/python
#-*- coding:utf-8 -*-

import HTMLTestRunner
#产生测试报告，第三方模块,需放在同级目录



import unittest
#unittest :python 自带的单元测试的框架
#使用unittest中unittest.TestCase这个类
#自动化测试用例进行用例管理
#所有的测试用例的函数必须以test开头，否则他不认为是测试用例
class qwe(unittest.TestCase):
    def setUp(self):#注：执行每一个测试用例前都执行一次；初始化测试环境
        #如：self.c=1
        print('开始')

    def tearDown(self):#注：执行每个测试用例后都执行一次；清理测试环(清除上一次执行留下的痕迹)
        print("结束")

    def test_1(self):
        a=4+5
        self.assertEqual(a,9)
        print(123)

    def test_2(self):
        b=6-5
        self.assertEqual(b,1)
        print(456)

if __name__=='__main__':
    #统一执行测试,测试的函数必须以test开头，否则不去执行(注：执行的先后顺序是按照test后面的字符串以ascii码进行排序执行）
    unittest.main()



#自动化测试（python的框架）
#测试用例的框架：（6个目录）
# config(包)    ——请求接口
# data         ——读取文件
# 接口_test    ——测试用例
# report     ——生成测试报告
# driver    ——控制运行的
# log(日志)

#用的工具的框架:
#pycharm
#unittest /pytest
#HTMLTsetRunner /allure
#xlrd /pymysql
#requests

















#import json
#import requests
# url = "http://120.132.8.33:9000/api/Account/LoginByPhone"
#
# payload = "{\r\n    \"phone\":\"15993835273\",\r\n    \"password\":\"111111\",\r\n    \"zone\":\"86\",\r\n    \"loginType\":0,\r\n    \"isAuto\":0,\r\n    \"deviceId\":\"ec:89:14:54:93:007\"\r\n}\r\n"
# headers = {
#     'Content-Type': "application/json",
#     'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
#     'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
#     'Language': "zh_CN",
#     'APIVersion': "3.0",
#     'User-Agent': "PostmanRuntime/7.11.0",
#     'Accept': "*/*",
#     'Cache-Control': "no-cache",
#     'Postman-Token': "7368d4ca-cb5b-41c9-92af-09e0f133a3c4,9eae6449-1228-414f-b199-ad3c66f22302",
#     'Host': "120.132.8.33:9000",
#     'accept-encoding': "gzip, deflate",
#     'content-length': "152",
#     'Connection': "keep-alive",
#     'cache-control': "no-cache"
#     }
#
# response = requests.request("POST", url, data=payload, headers=headers)
#
# print(response.text)
# #方法1
# res=response.json()
#
# if res['code']==0:
#     print('成功')
# #方法2
# res=response.text
# msg=json.loads(res)
# if msg['code']==0:
#     print('成功')




#          web测试
#1、下载模块  selenium
from selenium import webdriver

dr = webdriver.Firefox()
