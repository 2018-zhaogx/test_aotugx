#！/usr/bin/python
#-*- coding:utf-8 -*-
from jiekou_kuangjia.report.baogao import Baogao
with open('a.txt','r')as f:
    bb=f.readlines()
if 'all' in bb:
    Baogao('*',all)
else:
    Baogao(bb,bb)