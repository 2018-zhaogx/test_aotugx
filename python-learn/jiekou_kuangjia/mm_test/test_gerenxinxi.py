#！/usr/bin/python
#-*- coding:utf-8 -*-
import unittest
from jiekou_kuangjia.config.qingqiu1 import qingqiu
from jiekou_kuangjia.data.duqu1 import duqu

class xinxi_ceshi(unittest.TestCase):
    qingq=qingqiu().xinxi
    def test_01(self):
        duq=duqu().shuju1()
        f = self.qingq(duq[0][0],duq[0][1],duq[0][2])
        self.assertEqual(f['msg'], 'OK')

    def test_02(self):
        duq = duqu().shuju1()
        for i in range(1,len(duq)):
            f = self.qingq(duq[i][0],duq[i][1],duq[i][1])
            self.assertNotEqual(f['code'], '0')
# if __name__=='__main__':
#     unittest.main()