#！/usr/bin/python
#-*- coding:utf-8 -*-
import yaml

with open(r'e:\PycharmProjects\python-learn\appjiekouceshi1\src\element\myde.yaml','r',encoding='utf-8')as fb:
    #a=yaml.load(fb)使用yaml模块的load方法将yaml文件中的数据转换成python字典的形式
    item_data=yaml.load(fb,Loader=yaml.FullLoader)  #返回值是字典格式
    # print(item_data)
    #     # print(item_data['three']['wx_id'])





def wx(driver):

    text = driver.find_element_by_id(item_data['three']['wx_id']).find_element_by_class_name(
        item_data['TextView_class']).text
    return text
def wb(driver):

    text = driver.find_element_by_id(item_data['three']['wb_id']).find_element_by_class_name(
        item_data['TextView_class']).text
    return text

def qq(driver):

    text = driver.find_element_by_id(item_data['three']['qq_id']).find_element_by_class_name(
        item_data['TextView_class']).text
    return text

def pd(driver):

    text = driver.find_element_by_id(item_data['three']['pd_id']).find_element_by_class_name(
        item_data['TextView_class']).text
    return text


