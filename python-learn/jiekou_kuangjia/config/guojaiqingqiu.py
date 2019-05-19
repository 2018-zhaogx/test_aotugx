#！/usr/bin/python
#-*- coding:utf-8 -*-
import requests

class qingqiu():

    def qingq(self,lujing):

        url = "http://120.132.8.33:9000/%s" %(lujing)

        payload = ""
        headers = {
            'Content-Type': "application/json",
            'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
            'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
            'Language': "zh_CN",
            'APIVersion': "3.0",
            'User-Agent': "PostmanRuntime/7.11.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "368defee-d71e-4d3e-a39c-5e4a3634e375,4d6fd129-bd55-4488-8024-ecb139184ce0",
            'Host': "120.132.8.33:9000",
            'accept-encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }

        response = requests.request("GET", url, data=payload, headers=headers)

        res = response.json()
        return res

if __name__=='__main__':
    pass
