#！/usr/bin/python
#-*- coding:utf-8 -*-
from jiekou_kuangjia.report import HTMLTestRunner
import unittest
#from jiekou_kuangjia.mm_test.test_denglu import denglu_ceshi

def Baogao(name,baogaodanming):
    suit = unittest.TestSuite()
    #suit.addTest(unittest.makeSuite(denglu_ceshi))


    #第三种方法添加测试用例：
    # 两个参数：1路径2通配符
    for i in name:
        dis=unittest.defaultTestLoader.discover(r'E:\PycharmProjects\python-learn\jiekou_kuangjia\mm_test',pattern='test_{}.py'.format(i.strip()))

        for j in dis:
            #返回值是列表
            suit.addTest(j)
    f = open(r'E:\PycharmProjects\python-learn\jiekou_kuangjia\report\{}.html'.format(baogaodanming), 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='接口测试报告', tester='赵冠星', description='结果如下')
    runner.run(suit)
    f.close()
if __name__=='__main__':
    pass