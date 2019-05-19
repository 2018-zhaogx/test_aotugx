#！/usr/bin/python
#-*- coding:utf-8 -*-

from selenium import webdriver
from time import sleep
######qq空间登录



# dr = webdriver.Firefox()
# dr.get('https://qzone.qq.com/')
# sleep(2)
# dr.switch_to.frame('login_frame')
# dr.find_element_by_id('switcher_plogin').click()
# sleep(1)
# dr.find_element_by_id('u').click()
# dr.find_element_by_id('u').send_keys(1416689834)
# dr.find_element_by_id('p').click()
# dr.find_element_by_id('p').send_keys('zhaoguanxing987..')
#
#
# dr.find_element_by_id('login_button').click()
# sleep(5)
#
# #点击退出
# dr.find_element_by_id('tb_logout').click()
# sleep(2)
#
# #会出现弹出框  alert
# #切换到alert上去，自动点击确定
# we= dr.switch_to.alert()
# print(we.text)
# #确定点击退出
# we.accept()
# #取消，点击取消



#
# #####qq邮箱登录
# dr = webdriver.Firefox()
# dr.get('https://mail.qq.com/cgi-bin/loginpage')
# dr.switch_to.frame('login_frame')
# dr.find_element_by_link_text('账号密码登录').click()
# dr.find_element_by_class_name('uin_del')







# dr.get('file:///C:/Users/www/Desktop/abc.html')
# #切换到弹出框
# dr.find_element_by_xpath('/html/body/input').click()
# sleep(3)
#
# ww = dr.switch_to_alert()
# print(ww.text)
#
# #输入内容
# ww.send_keys('哈哈')
#
# #点击确定
# ww.accept()
#
# # #点击取消
# # ww.dismiss()


#
# dr = webdriver.Firefox()
# dr.get('https://qzone.qq.com/')
# sleep(2)
# #定位到框架(先找到ifram)  id  name两种元素定位
# dr.switch_to.frame('login_frame')
# # #还有就是xpath定位
# # ww=dr.find_element_by_xpath('//*[@id="login_frame"]')
# # dr.switch_to_alert(ww)
#
# # #如果框架套框架，这是切换到上一级框架
# # dr.switch_to.parent_frame()
#
# #退出框架(退出到最初的页面)
# dr.switch_to_default_content()
#

dr = webdriver.Firefox()
ww = dr.get('https://www.douban.com/')#1号窗口

sleep(3)

#获取当前窗口的标识号（句柄）
print(dr.current_window_handle)

dr.find_element_by_xpath('/html/body/div[1]/div[1]/ul/li[2]/a').click()#2号窗口
sleep(3)
#获取所有窗口的标识（列表形式显示，可以去下标）
qw=dr.window_handles
print(qw)
sleep(3)
#切换窗口
#浏览器本身是无法决定什么时候打开哪一个窗口
#是按照窗口打开的顺序给出矿口标号（唯一标识这个窗口的字符串）
dr.switch_to.window(qw[-1])
print(dr.title)

