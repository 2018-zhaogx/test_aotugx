#！/usr/bin/python
#-*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.keys import Keys
import os

if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']


dr = webdriver.Firefox()
dr.get('https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_d131c4278e7d4b57b0095f132cea61fd')



# print(dr.get_cookies())
# dr.delete_all_cookies()
# dr.add_cookie({'name': 'BAIDUID', 'value': 'xxxxxx'})
# dr.add_cookie({'name': 'BDUSS', 'value': 'xxxxxx'})

# dr.get('https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_d131c4278e7d4b57b0095f132cea61fd')

# sleep(3)
# dr.quit()





dr.find_element_by_class_name('user_login').click()
dr.find_element_by_css_selector('div.login-tab:nth-child(3) > a:nth-child(1)').click()
# dr.find_element_by_class_name('clear-btn').click()
dr.find_element_by_css_selector('html body div#content div.login-wrap div.w div.login-form div.login-box div.mc div.form form#formlogin div.item.item-fore1 input#loginname.itxt').send_keys(17637897624)
dr.find_element_by_xpath('//*[@id="nloginpwd"]').send_keys('zhaoguanxing987')
sleep(1)
dr.find_element_by_id('loginsubmit').click()
sleep(14)

dr.find_element_by_xpath('//*[@id="key"]').send_keys('iphone XR')
sleep(2)
dr.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/div[2]/button').click()
sleep(5)
dr.find_element_by_id('J_AD_100000177760').click()
sleep(2)
ck=dr.window_handles
print(ck)
sleep(2)
dr.switch_to.window(ck[-1])
sleep(2)
dr.find_element_by_id('InitCartUrl').click()

dr.quit()






