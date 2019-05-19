#！/usr/bin/python
#-*- coding:utf-8 -*-
import requests
class qingqiu():
    def xinxi(self, id1, id2, token):
        url = "http://120.132.8.33:9000/api/Account/GetUserInfo"

        querystring = {"accountGuid": "%s" %(id1),
                       "targetAccountGuid": "%s" %(id2)}

        payload = ""
        headers = {
            'Content-Type': "application/json",
            'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
            'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
            'Language': "zh_CN",
            'APIVersion': "3.0",
            'TimeZone': "GMT+4",
            'AccessToken': "%s" % (token),
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

        res = response.json()
        return res