#！/usr/bin/python
#-*- coding:utf-8 -*-
import requests
import unittest
import xlrd
import HTMLTestRunner
class denglu(unittest.TestCase):
    def setUp(self):
        print("开始")

    def tearDown(self):
        print("结束")

    def q(self,phone,password):

        url = "http://120.132.8.33:9000/api/Account/LoginByPhone"

        payload = "{\r\n    \"phone\":\"%s\",\r\n    \"password\":\"%s\",\r\n    \"zone\":\"86\",\r\n    \"loginType\":0,\r\n    \"isAuto\":0,\r\n    \"deviceId\":\"ec:89:14:54:93:007\"\r\n}\r\n" %(phone,password)
        headers = {
            'Content-Type': "application/json",
            'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
            'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
            'Language': "zh_CN",
            'APIVersion': "3.0",
            'User-Agent': "PostmanRuntime/7.11.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "7368d4ca-cb5b-41c9-92af-09e0f133a3c4,6f37668d-7619-4ebd-ae62-15cb353942ec",
            'Host': "120.132.8.33:9000",
            'accept-encoding': "gzip, deflate",
            'content-length': "152",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }

        response = requests.request("POST", url, data=payload, headers=headers)

        res=response.json()
        return res

    def Wenjian(self):
        f=xlrd.open_workbook(r'c:\Users\www\Desktop\工作簿0.xlsx')
        sheet=f.sheets()[0]
        num=sheet.nrows
        Wenjian=[]
        for i in range(num):
            if i != 0:
                Wenjian.append((sheet.row_values(i)))
        return Wenjian

    def test_1(self):
        Wenjian=self.Wenjian()
        print((int(Wenjian[0][0]),int(Wenjian[0][1])))
        qq=self.q(int(Wenjian[0][0]),int(Wenjian[0][1]))
        self.assertEqual(qq['msg'],'OK')
        print("登录成功")
    def test_2(self):
        Wenjian=self.Wenjian()
        for i in range(1,len(Wenjian)):
            print(int(Wenjian[i][0]))
            ww=self.q(int(Wenjian[i][0]),int(Wenjian[i][1]))
            self.assertNotEqual(ww['code'],0)
            print("登录失败，数据错误，请从新输入")

if __name__=='__main__':
    # unittest.main()

    #创建一个测试套件
    suit = unittest.TestSuite()
    #将测试用例添加到测试套件中(两种方法)
    #方法一（单个添加）
    # suit.addTest(denglu('test_1'))
    # suit.addTest(denglu('test_2'))
    #方法二
    #将denglu类中所有的以test开头的函数都添加到测试套件中（添加整个类）
    suit.addTest(unittest.makeSuite(denglu))
    #打开一个空文件（后缀名是.html)
    f = open('asd.html','wb')
    #定义测试报告的信息
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='接口测试报告',tester='赵冠星',description='结果如下')
    #执行测试套件
    runner.run(suit)
    f.close()

