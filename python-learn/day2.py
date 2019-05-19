#! /usr/bin/python
# -*- coding:utf-8 -*-
#字符串的内置函数  用法：变量名.函数()
# a = 'qwerasfd'
# #将字符串改大写
# b=a.upper()
# print(b)
# #将字符串改为小写
# a= 'QWERTASDF'
# b = a.swapcase()
# print(b)
# a = 'asddewfad'
# #替换元素中的数据
# b=a.replace('as','123')
# print(b)
# a= 'ahfiawafq'
# #以括号中的数据为分隔符，量数据分割成列表
# b=a.split('a')
# print(b)
# a='afihjiafiafi'
# #判断是否以括号中的数据开头
# b=a.startswith('as')
# print(b)
# b=a.endswith('if')
# print(b)
#将列表连接起来形成新的数据
#格式化字符串
# a='asdfasdf{}'
# b=110
#填充字符串
# c=a.format(b)
# print(c)
# d=input('请输入：')
# c=a.format(d)
# print(c)
# %站位 填充%  %s表示可填充任意数据， %d表示只能填充数字
# a= 'qer%s,12313%d'
# c=a %('asd',990)
# print(c)
#去除字符串左右的空格
# a=[11,22,33,44,55,66,77,88,99]
# b,c=[],[]
# for i in a:
#     if i>55:
#         b.append(i)
#     else:
#         c.append(i)
# print(b)
# print(c)
# a=0
# for i in range(1,101):
#     a += i
# print(a)
a = input('顾客总资产>>')
if a.startswith('-'):
    print('资金出错')
yuer = int(a)
o = []
gwqd = []
gwczjg = []
zongjia=[]
ss = []
goods = [
        {'1': '电脑', 'price': 1999},
        {'2': '鼠标', 'price': 10},
        {'3': '游艇', 'price': 20},
        {'4': '飞机', 'price':998},
]
print('余额：%d' %(yuer))
print('商品')
for i in goods:
    print(i)
def tianjiagouwuche():
    c = input('以空格分开，输入商品序号>>')
    p = c.split(' ')
    for e in p:
        e = int(e)
        e -= 1
        o.append(e)
    for p in o:
        if 0<=p<4:
            print('添加购物车成功')
        else:
            print('输入商品号错误，请从新输入。')
tianjiagouwuche()
print('购物车：')
for y in o:
    gwqd = goods[y]
    print(gwqd)
    jianzhi = gwqd.values()
    jianzhi=list(jianzhi)
    gwczjg.append(jianzhi)
for nn in range(len(gwczjg)):
    zongjia.append(gwczjg[nn][1])
    # gwpd.clear()
sum(zongjia)
goumaijia = sum(zongjia)
cg='ok'
if yuer >= goumaijia:
    print('输入ok购买成功')
    tt=input('>>')
    if cg==tt:
        print('购买成功')
else:
    print('余额不足')
# chongzhi = int(input('金额>>')
# yuer = yuer+chongzhi
