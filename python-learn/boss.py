# #！/usr/bin/python
# #-*- coding:utf-8 -*-
# # import requests
# # import re
# # dizhi = ''
# # gongling = []
# # gongzi = []
# # xueli = []
# # dizhia=[]
# # for i in range(1,2):
# #     oo={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}
# #     a='https://www.zhipin.com/c101010100/?query=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&page={}&ka=page-{}'.format(i,i)
# #     b = requests.get(a, headers=oo)
# #     c = b.content.decode('utf-8')
# #     zw = re.compile('<div class="job-title">(.*?)</div>', re.S)
# #     gz = re.compile('<span class="red">(.*?)</span>', re.S)
# #     dz = re.compile('<div class="info-detail"></div>(.*?)<div class="info-company">',re.S)
# #     # gl = re.compile('</em>(.*?)<em',re.S)
# #     # xl = re.compile('</em>(..?)</p>',re.S)
# # #    dz = re.compile('<p>(.*?)<em class="vline">',re.S)
# #     zhiweii=zw.findall(c)
# #     gongzii=gz.findall(c)
# #     dizhii=dz.findall(c)
# #     # gongling = gl.findall(dd)
# #     # xuelii = xl.findall(dd)
# #     # dizhii = dz.findall(dd)
# # for i in dizhii:
# #     dizhi=dizhi+str(i)
# # dizhi=dizhi.replace('\n','')
# # dza = re.compile('<p>(.*?)<em class="vline"></em>')
# # print(dizhi)
# # dizhii=dza.findall(dizhi)
# # print(dizhii)
# # gonglinga = re.compile('</em>(.*?)<em class="vline">',re.S)
# # pp=dza.findall(gonglinga)
# # print(pp)
#
# # a= input('输入一个日期,杠分开>>')
# import time
# # a=time.strptime(a,'%Y-%m-%d')
# # b=time.mktime(a)
# # c=b-86400
# # d=time.localtime(c)
# # b=time.strftime('%Y-%m-%d',d)
# # print(b)
# # b=time.strptime(2019-01-10)
#
#
# # import re
# # import requests
# # class douban(object):
# #     def wangzhi(self,yeshu):
# #         wz='https://movie.douban.com/top250?start={}&filter='.format(yeshu)
# #         a={
# #             'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64;rv: 66.0)Gecko/20100101Firefox/66.0'
# #     }
# #         res = requests.get(wz, headers=a)
# #         html=res.content.decode('utf-8')
# #         return html
# #
# #     def gg(self,gc):
# #         names=[]
# #         haibao=[]
# #         dym=re.compile('<img width="100"(.*?)<div class="info">',re.S)
# #         dyms=dym.findall(gc)
# #         # print(dyms)
# #         for dd in dyms:
# #             ndy=re.compile(r'alt="(.*?)"',re.S)
# #             name=ndy.findall(dd)
# #             ny=re.compile(r'src="(.*?)" class="">\n',re.S)
# #             dhaibao=ny.findall(dd)
# #             names.extend(name)
# #             haibao.extend(dhaibao)
# #         return names,haibao
# #     def baoc(self,bc,ac):
# #         for a,b in enumerate(ac):
# #             qq=requests.get(b)
# #             qs=qq.content
# #             zz=bc[a]
# #             with open('tp\{}.jpg'.format(zz),'wb')as ff:
# #                 ff.write(qs)
# # db=douban()
# # for an in range(0,25,25):
# #     wz=db.wangzhi(an)
# #     tl,ij=db.gg(wz)
# #     db.baoc(tl,ij)
#
#
#
#
#
#
#
#
#
# # import re
# # import requests
# # class douban(object):
# #     def wangzhi(self,qwe):
# #         wz='https://movie.douban.com/top250?start={}&filter='.format(qwe)
# #         a={
# #             'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64;rv: 66.0)Gecko/20100101Firefox/66.0'
# #     }
# #         res = requests.get(wz, headers=a)
# #         html=res.content.decode('utf-8')
# #         return html
# #
# #     def gg(self,asd):
# #         names=[]
# #         haibao=[]
# #         dym=re.compile('<img width="100"(.*?)<div class="info">',re.S)
# #         dyms=dym.findall(asd)
# #         # print(dyms)
# #         for dd in dyms:
# #             ndy=re.compile(r'alt="(.*?)"',re.S)
# #             name=ndy.findall(dd)
# #             ny=re.compile(r'src="(.*?)" class="">\n',re.S)
# #             dhaibao=ny.findall(dd)
# #             names.extend(name)
# #             haibao.extend(dhaibao)
# #         return names,haibao
# #     def baocun(self,bc,ac):
# #         for a,b in enumerate(ac):
# #             qq=requests.get(b)
# #             qs=qq.content
# #             zz=bc[a]
# #             with open('{}.jpg'.format(zz),'wb')as ff:
# #                 ff.write(qs)
# # db=douban()
# # for an in range(0,50,25):
# #     wz=db.wangzhi(an)
# #     tl,ij=db.gg(wz)
# #     db.baocun(tl,ij)
#
import re
import requests
class doubian():
    def qingqiu(self,qwe):
        url='https://movie.douban.com/top250?start={}&filter='.format(25*qwe)
        head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}
        res=requests.get(url,headers=head)
        html=res.content.decode('utf-8')
        return html
    def guolv(self,asd):
        mm,dd,yyp,ppf=[],[],[],[]
        patt=re.compile('<div class="item">(.*?)<p class="quote">',re.S)
        items=patt.findall(asd)
        for i in items:
            m = re.compile('<img width="100" alt="(.*?)" src="',re.S)
            d = re.compile('导演: (.*?)&nbsp;&nbsp', re.S)
            yp = re.compile('v:average">(.*?)</span>', re.S)
            pf = re.compile('<span>(.*?)人评价</span>')
            new_m=m.findall(i)
            new_d=d.findall(i)
            new_yp = yp.findall(i)
            new_pf = pf.findall(i)
            mm.append(new_m)
            dd.append(new_d)
            yyp.append(new_yp)
            ppf.append(new_pf)
    #    return mm,dd,yyp,ppf
    # def savee(self,a,s,d,f):
        try:
            from xlutils.copy import copy
            import xlrd
            f=xlrd.open_workbook('open.xls')
            #f=xlrd.open_workbook('open.xls')
            sheet1=f.sheets()[0]
            num=sheet1.nrows
            new_f=copy(f)
            sheet=new_f.get_sheet(0)
            for i in range(len(mm)):
                sheet.write(i+num,0,mm[i])
                sheet.write(i+num,1,dd[i])
                sheet.write(i+num,2,yyp[i])
                sheet.write(i+num,3,ppf[i])
            new_f.save('open.xls')
        except:
            import xlwt
            f=xlwt.Workbook()
            sheet=f.add_sheet('sheet1')
            sheet.write(0, 0, '电影名')
            sheet.write(0, 1, '导演')
            sheet.write(0, 2, '影评')
            sheet.write(0, 3, '评分')
            for i in range(len(mm)):
                sheet.write(i + 1, 0, mm[i][0])
                sheet.write(i + 1, 1, dd[i][0])
                sheet.write(i + 1, 2, yyp[i][0])
                sheet.write(i + 1, 3, ppf[i][0])
            f.save('open.xls')
tt=doubian()
for i in range(0,2,1):
    html=tt.qingqiu(i)
    tt.guolv(html)

#
# # a=[1,2,3,4]
# # b=[100,200,300,400]
# # c=list(zip(a,b))
# # print(c)
# # for i,j in c:
# #     print()
#
#
#
#
# #可以一直输入sql语句
# # while True:
# #     import pymysql
# #     a=input('输入sql语句,输入exit退出>>>')
# #     if a=='exit':
# #         conn.close()
# #         break
# #     conn=pymysql.connect(host='192.168.1.26',port=3306,user='root',passwd='123')
# #     abc=conn.cursor()
# #     try:
# #         abc.execute('a')
# #         conn.commit()
# #     except:
# #         print('语法错误')
# #         continue
# #     conn.commit()
#
#
#
# # import pymysql
# # conn=pymysql.connect(host='192.168.1.26',port=3306,user='root',passwd='123')
# # abc=conn.cursor()
# # abc.execute('show databases;')
# # conn.commit()
# # print(abc.fetchall())
#







import requests
import json
import xlrd
import xlwt
from xlutils.copy import copy
class zhilian():
    def wangzhi(self,qwe):
        url='https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=90&cityId=530&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=软件测试工程师&kt=3&=0&_v=0.15165695&x-zp-page-request-id=f4cef2a05cab414180e38a59801e967e-1554010613896-266039'.format(qwe*90)
        head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}
        res=requests.get(url,headers=head)
        htm=res.text
        html=json.loads(htm)
        return html
    def guolv(self,asd):
        o,a,s,d,f,g,h,j=[],[],[],[],[],[],[],[]
        for i in range(90):
            chengshi=asd['data']['results'][i]['city']['display']
            #dizhi=asd['data']['results'][i]['recentAndTotal']['businessArea']
            gongsim=asd['data']['results'][i]['company']['name']
            zhiwei=asd['data']['results'][i]['jobName']
            xinzi = asd['data']['results'][i]['salary']
            jingyan=asd['data']['results'][i]['workingExp']['name']
            xueli=asd['data']['results'][i]['eduLevel']['name']
            xinzidaiyu=asd['data']['results'][i]['jobTag']['searchTag']
            a.append(chengshi)
            #o.append(dizhi)
            s.append(gongsim)
            d.append(zhiwei)
            f.append(xinzi)
            g.append(jingyan)
            h.append(xueli)
            j.append(xinzidaiyu)
        return a,s,d,f,g,h,j
    def save(self,q,w,e,r,t,y,u):
        try:
            ff = xlrd.open_workbook('asdf.xls')
            sheet1 = ff.sheets()[0]
            num = sheet1.nrows
            new_f = copy(ff)
            sheet = new_f.sheet(0)
            for ii in range(len(q)):
                sheet.write(num+1, 0, q[ii])
                sheet.write(num+1, 1, w[ii])
                sheet.write(num+1, 2, e[ii])
                sheet.write(num+1, 3, r[ii])
                sheet.write(num+1, 4, t[ii])
                sheet.write(num+1, 5, y[ii])
                sheet.write(num+1, 6, u[ii])
                num += 1
            new_f.save('fasdf.xls')
        except:
            vv = 1
            f = xlwt.Workbook()
            sheet = f.add_sheet('sheet1')
            sheet.write(0, 0, '地址')
            sheet.write(0, 1, '公司名称')
            sheet.write(0, 2, '岗位')
            sheet.write(0, 3, '薪资')
            sheet.write(0, 4, '经验')
            sheet.write(0, 5, '学历')
            sheet.write(0, 6, '薪资待遇')
            for ii in range(len(q)):
                sheet.write(vv, 0, q[ii])
                sheet.write(vv, 1, w[ii])
                sheet.write(vv, 2, e[ii])
                sheet.write(vv, 3, r[ii])
                sheet.write(vv, 4, t[ii])
                sheet.write(vv, 5, y[ii])
                sheet.write(vv, 6, u[ii])
                vv += 1
            f.save('fasdf.xls')



tu=zhilian()
for i in range(2):
    asd=tu.wangzhi(i)
    q,w,e,r,t,y,u=tu.guolv(asd)
    tu.save(q,w,e,r,t,y,u)
# #职位 公司  地址  薪资 工作经验  学历
# import os
# os.rmdir('')


# import pymysql
# conn=pymysql.connect(host='192.168.1.17',port=3306,user='root',password='123')
# abc=conn.cursor()
# abc.execute('use ssss;')
#conn.commit()

