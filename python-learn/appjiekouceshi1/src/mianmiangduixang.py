#！/usr/bin/python
#-*- coding:utf-8 -*-
# from appium import webdriver
# from time import sleep
# import unittest


# class  QQ(object):
#
#     d={
#       "device": "android",
#       "platformName": "Android",
#       "platformVersion": "8.0.0",
#       "deviceName": "a5d1b24c",
#       "appPackage": "com.tencent.mobileqq",
#       "appActivity": ".activity.SplashActivity",
#       "noReset": "True"
#     }
#     @classmethod
#     def setUpClass(cls):
#         cls.dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=cls.d)
#         sleep(10.0)
#
#     def sousu(self):
#         self.dr.find_element_by_id('com.tencent.mobileqq:id/et_search_keyword').click()
#         sleep(2.0)
#
#     def mingzi(self,mingz='张立博'):
#         self.dr.find_element_by_id('com.tencent.mobileqq:id/et_search_keyword').find_element_by_xpath('//android.widget.RelativeLayout[@content-desc="搜索聊天或者联系人"]/android.widget.EditText').send_keys(mingz)
#         sleep(2.0)
#     def dainji(self):
#         self.dr.find_element_by_id('com.tencent.mobileqq:id/name').find_element_by_class_name('android.widget.RelativeLayout').click()
#         sleep(1.0)
#     def shurukuang(self,wenzi):
#         self.dr.find_element_by_id('com.tencent.mobileqq:id/input').send_keys(wenzi)
#         sleep(0.5)
#         self.dr.find_element_by_id('com.tencent.mobileqq:id/fun_btn').click()
#         sleep(2.0)
#     @classmethod
#     def tearDownClass(cls):
#         cls.dr.quite()
# if __name__=='__main__':
#     gg=QQ()
#     gg.setUpClass()
#     gg.sousu()
#     gg.mingzi()
#     gg.dainji()
#     gg.shurukuang('haha')
#     gg.tearDownClass()






from appium import webdriver
from time import sleep
import unittest
import xlrd


class DS(unittest.TestCase):

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
    @classmethod
    def setUpClass(cls):

        cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=cls.d)
        sleep(10.0)
    #跳转密码登录跳转
    def tiao_zhuan(self):
        self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
        sleep(2.0)

    def login(self,phone,passwd):

        # 向手机账号输入框输入手机号
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(phone)
        # # 清除输入
        # self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').clear()
        # #重新输入手机号
        # self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(phone)
        # 向手机密码框输入密码
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys(passwd)
        sleep(2.0)

        # 点击登录
        self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()

        sleep(2.0)

    def test_qqweizi(self):
        self.tiao_zhuan()
        jj = self.dieshengewnjain()
        for j in range(1):
            self.login(int(jj[j][0]),jj[j][1])
            if j==0:
                text=self.dr.find_element_by_id('com.qk.butterfly:id/tv_tag1').text

                self.assertEqual(text,'热门')
                print('登录成功')
                sleep(0.2)
                self.tuichudenglu()
            # else:
            #     text=self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').text
            #     sleep(0.1)
            #     self.assertEqual(text,'登录')
            #     print('失败')
            #     sleep(0.1)



    def tuichudenglu(self):
        #find_element_by_class_name()定位一个class属性的元素，要求该元素唯一
        #find_elements_by_class_name()定位多个class属性的元素，元素是多个
        self.dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')[3].click()
        sleep(0.1)
        #模拟人工下划(屏幕下划，手指上画）

        #获取当前屏幕分辨率
        size=self.dr.get_window_size()
        x1=size['width']*0.5
        y1=size['height']*0.25
        y2=size['height']*0.75
        for i in range(2):
            self.dr.swipe(x1,y2,x1,y1)

        self.dr.find_element_by_id('com.qk.butterfly:id/v_me_setting').click()
        sleep(0.1)
        self.dr.find_element_by_id('com.qk.butterfly:id/v_me_grade').click()
        sleep(0.1)
        self.dr.find_element_by_id('com.qk.butterfly:id/tv_ok').click()
        sleep(0.1)

    def dieshengewnjain(self):
        f=xlrd.open_workbook(r'c:\Users\www\Desktop\碟声文件.xlsx')
        sheet=f.sheets()[0]
        num = sheet.nrows
        list1=[]
        for i in range(1,num):
            list1.append(sheet.row_values(i))


        return list1






    # 关闭app的函数
    @classmethod
    def tearDownClass(cls):
        sleep(2.0)
        cls.dr.quit()


if __name__ == '__main__':
    unittest.main()
    #gg=DS()
    # gg.setUpClass()
    # gg.tiao_zhuan()
    # gg.login()
    # gg.tuichudenglu()
    # gg.tearDownClass()
