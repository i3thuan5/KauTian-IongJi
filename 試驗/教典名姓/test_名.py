from unittest.case import TestCase
from 臺灣言語工具.基本物件.字 import 字
from 用字 import 教典名姓


class Mia(TestCase):

    def test_erm(self):
        self.assertTrue(教典名姓.有這个字無(字('鍼', 'tserm')))

    def test_ionn(self):
        self.assertTrue(教典名姓.有這个字無(字('薔', 'tshiônn')))

    def test_訓用mài(self):
        self.fail()

    def test_俗用mài(self):
        self.fail()
