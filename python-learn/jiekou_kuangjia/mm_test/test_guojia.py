#！/usr/bin/python
#-*- coding:utf-8 -*-
import unittest
from jiekou_kuangjia.config.guojaiqingqiu import qingqiu
from jiekou_kuangjia.data.guojaiduqu import duqu
class guojia(unittest.TestCase):
    qing=qingqiu().qingq
    du=duqu().duq()
    def test_guojia1(self):

        print(self.du[0][0])
        f=self.qing(self.du[0][0])
        self.assertEqual(f['msg'],'OK')

    def test_guojia2(self):

        for i in range(1,len(self.du)):
            f = self.qing(self.du[i][0])
            self.assertNotEqual(f['msg'], 'OK')

if __name__=='__main__':
    unittest.main()