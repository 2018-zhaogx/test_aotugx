#！/usr/bin/python
#-*- coding:utf-8 -*-


#          web测试
#1、下载模块  selenium
#2、浏览器搜索 selenium浏览器驱动 下载火狐或者谷歌浏览器插件（压缩文件）
# 压缩文件版本必须保持一致尽量浏览器和插件都是最新版）
#3、把两个压缩包放到（运行一个.py文件,显示结果框第一行python.exe前面的路径），然后将压缩包解压到当前目录下。（不要创建一个目录解压）
#selenium :是web自动化测试工具集
#版本：selenium1.0和selenium2.0、selenium3.0（1.0 和2.0差别大，2.0和3.0差别不不大）

#selenium是嵌入到Firefox浏览器中的一个插件，实现看简单的浏览器操作的录制和与回放功能
#selenium的优点:1开源免费，
            # 2多浏览器支持
            # 3多平台支持函
            # 4多语言支持
            # 5对web页面有良好的支持
            # 6简单（AIP)简单、灵活（用于发言语言驱动）



########selenium Grid,是一种自动化测试复辅助工具，
# 利用它，可以很方便的同时在多台机器上和易构环境中并行运行多个测试用例


#selenium RC：是selenium1.0 的核心，支持多种不同的语言编写自动化测试脚本，负责控制浏览器的行为。
#
#selenium 1.0和 2.0；区别：selenium RC在浏览器中运行JavaScript应用，是浏览器内置控制器的JavaScript翻译器来来翻译和执行自动化脚本
#                   作用：针对各个浏览器而开发，通过原生浏览器或者浏览器扩展直接控制浏览器的



from selenium import webdriver
import time

#定义一个浏览器（打开）
dr = webdriver.Firefox()

#请求网页
dr.get('https://www.baidu.com')
time.sleep(5)
# dr.get('https://jingdong.com')
# time.sleep(3)
# #回到网页的上一步(后退)
# dr.back()
#
# #前进
# time.sleep(2)
# dr.forward()

#定位   id
dr.find_element_by_id('kw').send_keys('python')

#点击函数click()
dr.find_element_by_id('su').click()

#输入函数send_keys()

# #定位  class   但是为了python中class，在这他取的是class_name()
# dr.find_element_by_class_name('').click()
# #dr.find_elements_by_class_name('')[0].click()

#定位  name  通过name定位
dr.find_element_by_name('tj_trnews').click()
time.sleep(3)
dr.back()

#通过link_text  文本定位   （前提要保证文本的唯一性)

dr.find_element_by_link_text('hao123')
time.sleep(2)
dr.back()

#partial link_text    模糊文本定位(多用于首页)

dr.find_element_by_partial_link_text('hao').click()

#tag_name  定位  通过标签页定位   copy xpath来找路径
dr.find_element_by_tag_name('')

#css 定位   可以通过css路径或css选择器定位（在复制里）
dr.find_element_by_css_selector()

#xpath 定位  路径定位
dr.find_element_by_xpath('')


#动作：click()  点击       clear（）  清除     send_keys() 输入

#定位一组，定位多个数据
#ww = dr.find_elements_by_id('su')

        #层级定位：先定为一个顶层的元素(父元素),在定位这个元素下面的元素(子元素)，   多用于复杂的场景下(父元素是唯一的element是单数不加s)
# dr.get('https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index')
# aa=dr.find_element_by_id('searchHotelLevelSelect').find_elements_by_tag_name('option')
# for i in aa:
#     i.click()
#     time.sleep(3)




# #获取网页标题
# print(dr.title) #一般用做断言，判断请求到的网页的标题是否含预期结果
#
# #获取请求的网址
# print(dr.current_url)

# #设置浏览器窗口大小
# dr.set_window_size(100,200)
# time.sleep(2)
#
# #设置浏览器窗口的位置
# dr.set_window_position(400,400)

#浏览器窗口最大化
dr.maximize_window()
time.sleep(3)
#浏览器窗口最小化
dr.minimize_window()



# #关闭浏览器
# dr.close()


















































