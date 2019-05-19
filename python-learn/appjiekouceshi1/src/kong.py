#！/usr/bin/python
#-*- coding:utf-8 -*-
#第一步导入appium模块中的webdriver类
from appium import webdriver
from time import sleep


#面向过程
####获取系统版本号（cmd中)  adb shell getprop ro.build.version.release
####获取活动名和包名的方法（cmd中）adb shell dumpsys window | findstr mCurrentFocus

d={
  "device": "android",
  "platformName": "Android",
  "platformVersion": "8.0.0",
  "deviceName": "a5d1b24c",
  "appPackage": "com.qk.butterfly",  #app包名
  "appActivity": ".main.LauncherActivity",   #APP活动页
  "noReset": "True"
}

#写死的   ttp:127.0.0.1:4723/wd/hub
#测试脚本是appium服务器与手机建立连接的过程
dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=d)

sleep(8.0)

##元素是id，就是用id定位方法    click()点击的意思
#dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').click()


# #获取微信的文字
# #先定位上一级，在定位下面的元素。没有id的找class
# text=dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
# text1=dr.find_element_by_id('com.qk.butterfly:id/v_login_wb').find_element_by_class_name('android.widget.TextView').text
# text2=dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name('android.widget.TextView').text
# print(text)
# print(text1)
# print(text2)

#点击密码登录
dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()


#插入等待时间,休眠几秒
sleep(2.0)

#send_keys()输入的是字符串。
#  什么时候可以用send_keys()?
#  1 向手机的输入输入框内输入数据的时候
#  2 clickable~~true
#  3 enabled ---》 true
#  4 foucsable --》 true
#向手机账号输入框输入手机号
dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('17637897624')
#向手机密码框输入密码
dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('123456zgx')
sleep(2.0)

#点击登录
dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()

sleep(10.0)
#退出app，包括后台进程也关掉
dr.quit()
