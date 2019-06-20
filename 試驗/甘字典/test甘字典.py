from 臺灣言語工具.基本物件.字 import 字
from unittest.case import TestCase
from 用字 import 甘字典


class 用字試驗(TestCase):

    def test_有文音字(self):
        self.assertTrue(甘字典.有這个字無(字('靄', 'Ai2')))

    def test_白話字(self):
        self.assertTrue(甘字典.有這个字無(字('嚵', 'Chham5')))

    def test_莫有點(self):
        self.assertFalse(甘字典.有這个字無(字('●', 'A3')))

    def test_莫有括號(self):
        self.assertFalse(甘字典.有這个字無(字('(蔻Khou3)', 'hau3')))
