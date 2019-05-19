#！/usr/bin/python
#-*- coding:utf-8 -*-
from jiekou_kuangjia.report import HTMLTestRunner
import unittest
def BaoGao():
    suit = unittest.TestSuite()
    dis = unittest.defaultTestLoader.discover(r'E:\PycharmProjects\python-learn\jiekou_kuangjia\mm_test',pattern='test1_*.py')
    for i in dis:
        suit.addTest(i)
    f = open(r'E:\PycharmProjects\python-learn\jiekou_kuangjia\report\asd1.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='接口测试报告', tester='赵冠星', description='结果如下')
    runner.run(suit)
    f.close()

if __name__=='__main__':
    BaoGao()