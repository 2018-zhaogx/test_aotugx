#！/usr/bin/python
#-*- coding:utf-8 -*-
from appium import webdriver
from time import sleep
import unittest


class  QQ(object):

    d={
      "device": "android",
      "platformName": "Android",
      "platformVersion": "8.0.0",
      "deviceName": "a5d1b24c",
      "appPackage": "com.tencent.mobileqq",
      "appActivity": ".activity.SplashActivity",
      "noReset": "True"
    }
    @classmethod
    def setUpClass(cls):
        cls.dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=cls.d)
        sleep(0.2)

    def sousu(self):
        self.dr.find_element_by_id('com.tencent.mobileqq:id/et_search_keyword').click()
        sleep(0.1)

    def mingzi(self,qq=1248430625):
        self.dr.find_element_by_id('com.tencent.mobileqq:id/et_search_keyword').send_keys(qq)
        sleep(0.2)
    def dainji(self):
        self.dr.find_element_by_id('com.tencent.mobileqq:id/result_layout').find_elements_by_class_name('android.widget.AbsListView')[0].find_elements_by_class_name('android.widget.LinearLayout')[1].find_elements_by_class_name('android.widget.LinearLayout')[0].find_elements_by_class_name('android.widget.LinearLayout')[0].click()
        sleep(0.1)
    def shurukuang(self,wenzi):
        self.dr.find_element_by_id('com.tencent.mobileqq:id/input').send_keys(wenzi)
        sleep(0.1)
        self.dr.find_element_by_id('com.tencent.mobileqq:id/fun_btn').click()
        sleep(0.1)
    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()
if __name__=='__main__':
    gg=QQ()
    gg.setUpClass()
    gg.sousu()
    gg.mingzi()
    gg.dainji()
    gg.shurukuang(str('逼仔'))
    #gg.tearDownClass()
