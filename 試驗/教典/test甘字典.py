from 臺灣言語工具.基本物件.字 import 字
from 用字 import 教典
from unittest.case import skip, TestCase


class 用字試驗(TestCase):

    def test_有文音字(self):
        self.assertTrue(教典.有這个字無(字('靄', 'Ai2')))

    def test_無白話音(self):
        self.assertFalse(教典.有這个字無(字('tok', '—')))

    def test_莫有點(self):
        self.assertFalse(教典.有這个字無(字('A3', '●')))

    def test_莫有括號(self):
        self.assertFalse(教典.有這个字無(字('hau3', '(蔻Khou3)')))
