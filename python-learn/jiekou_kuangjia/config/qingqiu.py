#！/usr/bin/python
#-*- coding:utf-8 -*-
import requests
#from jiekou_kuangjia.data.duqu import Shuju
class jiekouqingqiu():

    def q(self, phone, password):
        url = "http://120.132.8.33:9000/api/Account/LoginByPhone"

        payload = "{\r\n    \"phone\":\"%s\",\r\n    \"password\":\"%s\",\r\n    \"zone\":\"86\",\r\n    \"loginType\":0,\r\n    \"isAuto\":0,\r\n    \"deviceId\":\"ec:89:14:54:93:007\"\r\n}\r\n" % (
        phone, password)
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

        res = response.json()
        return res

if __name__=='__main__':
    # shu=Shuju().Wenjian()
    # for i in range(len(shu)):
    #     aa=jiekouqingqiu().q(int(shu[i][0]),int(shu[i][1]))
    #     print(aa)
    pass