#！/usr/bin/python
#-*- coding:utf-8 -*-


#########面向对象######
# from appium import webdriver
# from time import sleep
# import unittest
# class DS(unittest.TestCase):
#     d = {
#         "device": "android",
#         "platformName": "Android",
#         "platformVersion": "8.0.0",
#         "deviceName": "a5d1b24c",
#         "appPackage": "com.qk.butterfly",
#         "appActivity": ".main.LauncherActivity",
#         "noReset": "True"
#     }
#     # #初始化测试环境的方法/函数
#     # def setUp(self):
#     #     self.dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=self.d)
#     #     sleep(10.0)
#
#
#     #所有的用例执行之前，跑一次，就只跑一次
#     @classmethod
#     def setUpClass(cls):
#         cls.dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=cls.d)
#         sleep(10.0)
#
#
#     #检查四个文字大的函数/方法
#     #断言文字是否存在
#     def test_weixinwenzi(self):
#         #获取微信的文字
#         #先定位上一级，在定位下面的元素。没有id的找class
#         text=self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
#         print(text)
#         self.assertEqual(text,'微信')
#
#
#     def test_weibowenzi(self):
#
#         text=self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wb').find_element_by_class_name('android.widget.TextView').text
#         print(text)
#         self.assertEqual(text,'微博')
#
#     def test_qqweizi(self):
#
#         text=self.dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name('android.widget.TextView').text
#         print(text)
#         self.assertEqual(text,'QQ')
#
#     # #关闭app的函数
#     # def tearDown(self):
#     #       self.dr.quit()
#
#     #所有的用例执行之后，跑一次，就跑一次
#     @classmethod
#     def tearDownClass(cls):
#         cls.dr.quit()
#
# if __name__=='__main__':
#     unittest.main()





from appium import webdriver
from time import sleep


class DS(object):

    # 测试脚本与appium服务器进行连接的参数数据
    d = {
        "device": "android",
        "platformName": "Android",
        "platformVersion": "8.0.0",
        "deviceName": "a5d1b24c",
        "appPackage": "com.qk.butterfly",
        "appActivity": ".main.LauncherActivity",
        "noReset": "True"
    }

    # 建立连接的函数
    def __init__(self):

        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.d)
        sleep(10.0)
    #跳转密码登录跳转
    def tiao_zhuan(self):
        self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
        sleep(2.0)

    def login(self,phone,pswd):
        # 向手机账号输入框输入手机号
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(phone)
        # 向手机密码框输入密码
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys(pswd)
        sleep(2.0)

        # 点击登录
        self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()

        sleep(10.0)

    def test_qqweizi(self):


        text=self.dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name('android.widget.TextView').text
        print(text)
        self.assertEqual(text,'QQ')
    # 关闭app的函数
    def close_app(self):
        sleep(10.0)
        self.dr.quit()


if __name__ == '__main__':
    go = DS()  # 创建一个DS类的实例，赋值给变量go
    # 调用DS类的方法
    go.tiao_zhuan()
    #执行登录
    go.login('17637897624','123456zgx')
    go.close_app()




