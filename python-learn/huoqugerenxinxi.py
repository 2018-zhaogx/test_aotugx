#！/usr/bin/python
#-*- coding:utf-8 -*-
import requests
import unittest
import HTMLTestRunner
class Huoqugerenxinxi(unittest.TestCase):

    def xinxi(self,token):
        url = "http://120.132.8.33:9000/api/Account/GetUserInfo"

        querystring = {"accountGuid":"0c9a2e9b-ba05-4921-b801-1337abb33038","targetAccountGuid":"0c9a2e9b-ba05-4921-b801-1337abb33038"}

        payload = ""
        headers = {
            'Content-Type': "application/json",
            'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
            'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
            'Language': "zh_CN",
            'APIVersion': "3.0",
            'TimeZone': "GMT+4",
            'AccessToken': "%s" %(token),
            'User-Agent': "PostmanRuntime/7.11.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "d8ce0643-7c66-4156-9492-0e4a2184b42e,449f2261-fc62-4238-b990-ab5771308e30",
            'Host': "120.132.8.33:9000",
            'accept-encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

        res=response.json()
        return res

    def test_01(self):
        ff=self.xinxi('38df0e73c5894ceaa76c3cf19f9c16b0')
        self.assertEqual(ff['msg'],'OK')

    def test_02(self):
        ff=self.xinxi('39df0e73c5894ceaa76c3cf19f9c16b0')
        self.assertNotEqual(ff['code'],'0')

if __name__=='__main__':
    #unittest.main()
    suit=unittest.TestSuite()
    suit.addTest(unittest.makeSuite(Huoqugerenxinxi))
    f=open('gerenxinxi.html','wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=f,title="接口测试报告",tester='赵冠星',description='结果如下')
    runner.run(suit)
    f.close()