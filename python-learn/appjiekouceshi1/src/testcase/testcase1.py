#！/usr/bin/python
#-*- coding:utf-8 -*-
from appjiekouceshi1.src.func.myde import wb,wx,qq,pd
from appium import webdriver
import unittest
from time import sleep
from jiekou_kuangjia.report.HTMLTestRunner import HTMLTestRunner


#导入日志
from appjiekouceshi1.src.testcase.aiaiai import log_rihzi
#给日志一个变量
goo = log_rihzi(name='testcase1.py')



#from appjiekouceshi1.src.until.acc import REPORT_DIR

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        d={
          "device": "android",
          "platformName": "Android",
          "platformVersion": "8.0.0",
          "deviceName": "a5d1b24c",
          "appPackage": "com.qk.butterfly",  #app包名
          "appActivity": ".main.LauncherActivity",   #APP活动页
          "noReset": "True"
        }

        cls.dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=d)
        sleep(5.0)
        goo.info('app建立连接完成!!!')
    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()
        goo.info('app关闭')

    def test_wx(self):
        g=wx(self.dr)
        self.assertEqual(g,'微信')
        goo.info('执行测试用例')

    def test_wb(self):
        g=wb(self.dr)
        self.assertEqual(g,'微博')
        goo.info('执行测试用例')

    def test_qq(self):
        g = qq(self.dr)
        self.assertEqual(g,'QQ')
        goo.info('执行测试用例')

    def test_pd(self):
        g = pd(self.dr)
        self.assertEqual(g,'密码')
        goo.info('执行测试用例')

#运行测试脚本，生成测试报告
if __name__=='__main__':
    #unittest.main()


    suit = unittest.TestSuite()
    suit.addTest(Test('test_wx'))
    suit.addTest(Test('test_wb'))
    suit.addTest(Test('test_qq'))
    suit.addTest(Test('test_pd'))

    # suit.addTest(unittest.makeSuite(denglu_ceshi))

    #将测试报告写入html文件
    #生成测试报告路径
    #将路径写死
    r_path =r'E:\PycharmProjects\python-learn\appjiekouceshi1\src\report\hahaha.html'
    #将路径写活
    #r_path=REPORT_DIR+'HTMLReport.html'


    f = open(r'E:\PycharmProjects\python-learn\appjiekouceshi1\src\report\hahaha.html', 'wb')
    runner = HTMLTestRunner(stream=f, title='接口测试报告', tester='赵冠星', description='结果如下',verbosity=2)#verbosity默认为0，是2 是输出信息更详细
    runner.run(suit)
    f.close()



