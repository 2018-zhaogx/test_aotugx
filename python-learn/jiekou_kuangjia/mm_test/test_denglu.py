#！/usr/bin/python
#-*- coding:utf-8 -*-
import unittest
from jiekou_kuangjia.config.qingqiu import jiekouqingqiu
from jiekou_kuangjia.data.duqu import Shuju

class denglu_ceshi(unittest.TestCase):
    #denglu=jiekouqingqiu().q
    def test_1(self):
        Wenjian = Shuju().Wenjian()
        qq = jiekouqingqiu().q(int(Wenjian[0][0]), int(Wenjian[0][1]))
        self.assertEqual(qq['msg'], 'OK')
        print("登录成功")

    def test_2(self):
        Wenjian = Shuju().Wenjian()
        for i in range(1, len(Wenjian)):
            print(int(Wenjian[i][0]))
            ww = jiekouqingqiu().q(int(Wenjian[i][0]), int(Wenjian[i][1]))
            self.assertNotEqual(ww['code'], 0)
            print("登录失败，数据错误，请从新输入")
if __name__=='__main__':
    unittest.main()