#！/usr/bin/python
#-*- coding:utf-8 -*-
import yaml
from appium import webdriver

with open(r'E:\PycharmProjects\python-learn\appjiekouceshi1\src\element\aotu.yaml','r',encoding='utf-8') as fb:
    #使用yaml模块的load方法将yaml文件中的数据转换成python字典的形式
    item_data = yaml.load(fb, Loader=yaml.FullLoader)
    # print(item_data['id1']['ziyouzuche'])
    # print(item_data['id1']['duanzuche'])
    # print(item_data['id1']['haowandeche'])
    # print(item_data['id1']['lijiyongche'])
    # print(item_data['id1']['zuixinhuodong'])
    # print(item_data['id1']['gengduo'])
def zyz(driver):
    text=driver.find_element_by_id(item_data['id1']['ziyouzuche']).text
    return text

def dzc(driver):
    text = driver.find_element_by_id(item_data['id1']['duanzuche']).text
    return text

def hwdc(driver):
    text=driver.find_element_by_id(item_data['id1']['haowandeche']).text
    return text

def ljyc(driver):
    text = driver.find_element_by_id(item_data['id1']['lijiyongche']).text
    return text

def zxhd(driver):
    text = driver.find_element_by_id(item_data['id1']['zuixinhuodong']).find_element_by_class_name(
        item_data['cla1'])[3].text
    return text

def gd(driver):
    text = driver.find_element_by_id(item_data['id1']['gengduo']).text
    return text
