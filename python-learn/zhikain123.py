# #！/usr/bin/python
# #-*- coding:utf-8 -*-
# import requests
# import json
# import xlrd
# import xlwt
# from xlutils.copy import copy
# class zhilian():
#     def wangzhi(self,qwe):
#         url='https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=90&cityId=530&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=软件测试工程师&kt=3&=0&_v=0.15165695&x-zp-page-request-id=f4cef2a05cab414180e38a59801e967e-1554010613896-266039'.format(qwe*90)
#         head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}
#         res=requests.get(url,headers=head)
#         htm=res.text
#         html=json.loads(htm)
#         return html
#     def guolv(self,asd):
#         a,s,d,f,g,h,j=[],[],[],[],[],[],[]
#         for i in range(90):
#             chengshi=asd['data']['results'][i]['city']['display']
#             gongsim=asd['data']['results'][i]['company']['name']
#             zhiwei=asd['data']['results'][i]['jobName']
#             xinzi = asd['data']['results'][i]['salary']
#             jingyan=asd['data']['results'][i]['workingExp']['name']
#             xueli=asd['data']['results'][i]['eduLevel']['name']
#             xinzidaiyu=asd['data']['results'][i]['jobTag']['searchTag']
#             a.append(chengshi)
#             s.append(gongsim)
#             d.append(zhiwei)
#             f.append(xinzi)
#             g.append(jingyan)
#             h.append(xueli)
#             j.append(xinzidaiyu)
#         return a,s,d,f,g,h,j
#     def save(self,q,w,e,r,t,y,u):
#         try:
#             ff = xlrd.open_workbook('asdf.xls')
#             sheet1 = ff.sheets()[0]
#             num = sheet1.nrows
#             new_f = copy(ff)
#             sheet = new_f.sheet(0)
#             for ii in range(len(q)):
#                 sheet.write(num+1, 0, q[ii])
#                 sheet.write(num+1, 1, w[ii])
#                 sheet.write(num+1, 2, e[ii])
#                 sheet.write(num+1, 3, r[ii])
#                 sheet.write(num+1, 4, t[ii])
#                 sheet.write(num+1, 5, y[ii])
#                 sheet.write(num+1, 6, u[ii])
#                 num += 1
#             new_f.save('asdf.xls')
#         except:
#             vv = 1
#             f = xlwt.Workbook()
#             sheet = f.add_sheet('sheet1')
#             sheet.write(0, 0, '地址')
#             sheet.write(0, 1, '公司名称')
#             sheet.write(0, 2, '岗位')
#             sheet.write(0, 3, '薪资')
#             sheet.write(0, 4, '经验')
#             sheet.write(0, 5, '学历')
#             sheet.write(0, 6, '薪资待遇')
#             for ii in range(len(q)):
#                 sheet.write(vv, 0, q[ii])
#                 sheet.write(vv, 1, w[ii])
#                 sheet.write(vv, 2, e[ii])
#                 sheet.write(vv, 3, r[ii])
#                 sheet.write(vv, 4, t[ii])
#                 sheet.write(vv, 5, y[ii])
#                 sheet.write(vv, 6, u[ii])
#                 vv += 1
#             f.save('asdf.xls')
#
#
#
# tu=zhilian()
# for i in range(2):
#     asd=tu.wangzhi(i)
#     q,w,e,r,t,y,u=tu.guolv(asd)
#     tu.save(q,w,e,r,t,y,u)
#
#
#
#
# import requests
# import json
# import xlrd
# import xlwt
# from xlutils.copy import copy
# class zhilian():
#     def wangzhi(self,qwe):
#         url='https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=90&cityId=530&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=软件测试工程师&kt=3&=0&_v=0.15165695&x-zp-page-request-id=f4cef2a05cab414180e38a59801e967e-1554010613896-266039'.format(qwe*90)
#         head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}
#         res=requests.get(url,headers=head)
#         htm=res.text
#         html=json.loads(htm)
#         return html
#     def guolv(self,asd):
#         a,s,d,f,g,h,j=[],[],[],[],[],[],[]
#         for i in range(90):
#             chengshi=asd['data']['results'][i]['city']['display']
#             gongsim=asd['data']['results'][i]['company']['name']
#             zhiwei=asd['data']['results'][i]['jobName']
#             xinzi = asd['data']['results'][i]['salary']
#             jingyan=asd['data']['results'][i]['workingExp']['name']
#             xueli=asd['data']['results'][i]['eduLevel']['name']
#             xinzidaiyu=asd['data']['results'][i]['jobTag']['searchTag']
#             a.append(chengshi)
#             s.append(gongsim)
#             d.append(zhiwei)
#             f.append(xinzi)
#             g.append(jingyan)
#             h.append(xueli)
#             j.append(xinzidaiyu)
#         return a,s,d,f,g,h,j
#     def save(self,q,w,e,r,t,y,u):
#         try:
#             ff = xlrd.open_workbook('fasdf.xls')
#             sheet1 = ff.sheets()[0]
#             num = sheet1.nrows
#             new_f = copy(ff)
#             sheet = new_f.sheet(0)
#             for ii in range(len(q)):
#                 sheet.write(num+1, 0, q[ii])
#                 sheet.write(num+1, 1, w[ii])
#                 sheet.write(num+1, 2, e[ii])
#                 sheet.write(num+1, 3, r[ii])
#                 sheet.write(num+1, 4, t[ii])
#                 sheet.write(num+1, 5, y[ii])
#                 sheet.write(num+1, 6, u[ii])
#                 num += 1
#             new_f.save('asdf.xls')
#         except:
#             vv = 1
#             f = xlwt.Workbook()
#             sheet = f.add_sheet('sheet1')
#             sheet.write(0, 0, '地址')
#             sheet.write(0, 1, '公司名称')
#             sheet.write(0, 2, '岗位')
#             sheet.write(0, 3, '薪资')
#             sheet.write(0, 4, '经验')
#             sheet.write(0, 5, '学历')
#             sheet.write(0, 6, '薪资待遇')
#             for ii in range(len(q)):
#                 sheet.write(vv, 0, q[ii])
#                 sheet.write(vv, 1, w[ii])
#                 sheet.write(vv, 2, e[ii])
#                 sheet.write(vv, 3, r[ii])
#                 sheet.write(vv, 4, t[ii])
#                 sheet.write(vv, 5, y[ii])
#                 sheet.write(vv, 6, u[ii])
#                 vv += 1
#             f.save('fasdf.xls')
#
#
#
# tu=zhilian()
# for i in range(2):
#     asd=tu.wangzhi(i)
#     q,w,e,r,t,y,u=tu.guolv(asd)
#     tu.save(q,w,e,r,t,y,u)
#
# with open('asdfg.txt','r') as f:
#     a=f.readlines()
#     print(a)











