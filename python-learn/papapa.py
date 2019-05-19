#！/usr/bin/python
#-*- coding:utf-8 -*-
# import requests
# import json
# class zhaogongzuo():
#     def Wz(self,qwe):
#         url='https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=90&cityId=530&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&=0&_v=0.82536652&x-zp-page-request-id=e51e796b180d490b823f0ac959a9611f-1554640860337-690623'.format(qwe*90)
#         head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/66.0'}
#         res=requests.get(url,headers=head)
#         htm=res.text
#         html=json.loads(htm)
#     def Gl(self,html):
#         zhiwei=html['']
# import time
# a=time.time()
# a=time.localtime(8000172800)
# aa=time.strftime('%Y-%m-%d %H:%M:%S %w %j',a)
# a=time.mktime(a)
# a=time.strptime('2019-09-11','%Y-%m-%d')
# print(a)
import os




import requests
import json
class zhilian():
    def wangzhi(self,qwe):
        url='https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=90&cityId=530&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=软件测试工程师&kt=3&=0&_v=0.15165695&x-zp-page-request-id=f4cef2a05cab414180e38a59801e967e-1554010613896-266039'.format(qwe*90)
        head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}
        res=requests.get(url,headers=head)
        htm=res.text
        html=json.loads(htm)
        return html
    def guolv(self,asd):
        a,s,d,f,g,h,j=[],[],[],[],[],[],[]
        for i in range(90):
            #chengshi=asd['data']['results'][i]['city']['display']
            chengshi=asd['data']['results'][i]['city']['display']
            #dizhi=asd['data']['results'][i]['businessArea']
            gongsim=asd['data']['results'][i]['company']['name']
            zhiwei=asd['data']['results'][i]['jobName']
            xinzi = asd['data']['results'][i]['salary']
            jingyan=asd['data']['results'][i]['workingExp']['name']
            xueli=asd['data']['results'][i]['eduLevel']['name']
            xinzidaiyu=asd['data']['results'][i]['jobTag']['searchTag']
            a.append(chengshi)
            s.append(gongsim)
            d.append(zhiwei)
            f.append(xinzi)
            g.append(jingyan)
            h.append(xueli)
            j.append(xinzidaiyu)
        return list(zip(a,s,d,f,g,h,j))
    def xls_save(self,vv):
        try:
            import xlrd
            from xlutils.copy import copy
            ff = xlrd.open_workbook('asdf.xls')
            sheet1 = ff.sheets()[0]
            num = sheet1.nrows
            new_f = copy(ff)
            sheet = new_f.sheet(0)
            for q, w, x, e, r, t, y, u in vv:
                sheet.write(num+1, 0, q)
                sheet.write(num+1, 1, w)
                sheet.write(num+1, 2, x)
                sheet.write(num+1, 3, e)
                sheet.write(num+1, 4, r)
                sheet.write(num+1, 5, t)
                sheet.write(num+1, 6, y)
                sheet.write(num+1, 7, u)
                num += 1
            new_f.save('asdf.xls')
        except:
            import xlwt
            nn = 1
            f = xlwt.Workbook()
            sheet = f.add_sheet('sheet1')
            sheet.write(0, 0, '地址')
            sheet.write(0, 1, '公司名称')
            sheet.write(0, 2, '岗位')
            sheet.write(0, 3, '薪资')
            sheet.write(0, 4, '经验')
            sheet.write(0, 5, '学历')
            sheet.write(0, 6, '薪资待遇')

            for q, w, e, r, t, y, u in vv:
                sheet.write(nn, 0, q)
                sheet.write(nn, 1, w)
                sheet.write(nn, 2, e)
                sheet.write(nn, 3, r)
                sheet.write(nn, 4, t)
                sheet.write(nn, 5, y)
                sheet.write(nn, 6, u)
                nn += 1
            f.save('asdf.xls')
    def txt_save(self,vv):
        import xlrd
        import xlwt
        try:
            with open('zhilian.txt','a',encoding='utf-8') as ff:
                for i in vv:
                    i=str(i)
                    ff.write(i+'\n')
        except:
            with open('zhilian.txt', 'w',encoding='utf-8') as f:
                    for i in vv:
                        i = str(i)
                        f.write(i+'\n')
    # def mysql_save(self, vv):
    #     import pymysql
    #     conn=pymysql.connect(host='192.168.1.17',port=3306,user='root',password='123')
    #     abc=conn.cursor()
    #     abc.execute('use ssss;')
    #     conn.commit()
    #     abc.execute('create table zhilain ("地址" char(255),"公司名" char(255),"岗位" char(255),"薪资" char(255),"经验" char(255),"学历" char(255),"薪资待遇" char(255))')
    #     conn.commit()
    #     for i in range(len(vv)):
    #         abc.execute('insert into zhilian("{}","{}","{}","{}","{}","{}","{}"'.format(vv[i][0],vv[i][1],vv[i][2],vv[i][3],vv[i][4],vv[i][5],vv[i][6],))
    #         conn.commit()

tu=zhilian()
for i in range(8):
    ffoo=tu.wangzhi(i)
    vv=tu.guolv(ffoo)
    tu.xls_save(vv)








