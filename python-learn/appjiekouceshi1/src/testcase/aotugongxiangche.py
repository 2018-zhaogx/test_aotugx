#！/usr/bin/python
#-*- coding:utf-8 -*-
import unittest
from appium import webdriver
from time import sleep
from jiekou_kuangjia.report.HTMLTestRunner import HTMLTestRunner
from appjiekouceshi1.src.func.aotuwenjian import zyz,dzc,hwdc,ljyc,zxhd,gd



from appjiekouceshi1.src.testcase.aiaiai import log_rihzi

rizhi=log_rihzi('aotugongxiangche.py')

class DCT(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        d={
            "device": "android",
            "platformName": "Android",
            "platformVersion": "8.0.0",
            "deviceName": "a5d1b24c",
            "appPackage": "com.aotuzuche.tanker",
            "appActivity": ".business.welcome.WelcomeActivity",
            "noReset": "True"
        }

        #与手机APP建立连接
        cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=d)
        sleep(10.0)
        #生成日志
        rizhi.info('app建立连接!!!')

    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()

        rizhi.info('关闭APP')

    def test_1(self):
        cs=zyz(self.dr)
        print(cs)
        #self.assertEqual(cs,'自由租')
        sleep(0.1)
        rizhi.info('执行测试用例')

    def test_2(self):
        cs=dzc(self.dr)
        self.assertEqual(cs,'短租车')
        sleep(0.1)
        rizhi.info('执行测试用例')

    def test_3(self):
        cs=hwdc(self.dr)
        self.assertEqual(cs,'好玩的车')
        sleep(0.1)
        rizhi.info('执行测试用例')

    def test_4(self):
        cs=ljyc(self.dr)
        self.assertEqual(cs,'立即用车')
        sleep(0.1)
        rizhi.info('执行测试用例')

    def test_5(self):
        cs=zxhd(self.dr)
        self.assertEqual(cs,'最新活动')
        sleep(0.1)
        rizhi.info('执行测试用例')

    def test_6(self):
        cs=gd(self.dr)
        self.assertEqual(cs,'更多')
        sleep(0.1)
        rizhi.info('执行测试用例')

if __name__=='__main__':
    suit=unittest.TestSuite()
    #suit.addTest(unittest.makeSuite(DCT))
    suit.addTest(DCT('test_1'))
    # suit.addTest(DCT('test_2'))
    # suit.addTest(DCT('test_3'))
    # suit.addTest(DCT('test_4'))
    # suit.addTest(DCT('test_5'))
    # suit.addTest(DCT('test_6'))
    r_path = r'E:\PycharmProjects\python-learn\appjiekouceshi1\src\report\AOTU.html'

    f = open(r'E:\PycharmProjects\python-learn\appjiekouceshi1\src\report\AOTU.html', 'wb')
    runner = HTMLTestRunner(stream=f, title='接口测试报告', tester='赵冠星', description='结果如下',
                            verbosity=2)  # verbosity默认为0，是2 是输出信息更详细
    runner.run(suit)
    f.close()
    # oo=DCT()
    # oo.setUpClass()
    # oo.test_1()