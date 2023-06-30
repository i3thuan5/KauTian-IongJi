from unittest.case import TestCase
from 臺灣言語工具.基本物件.字 import 字
from 用字 import 教典


class Mia(TestCase):

    def test_erm(self):
        self.assertTrue(教典.有這對應無('鍼', 'tserm'))

    def test_ionn(self):
        self.assertTrue(教典.有這對應無('薔', 'tshiônn'))

    def test_異體字mài_較袂攪擾(self):
        self.assertFalse(教典.有這對應無('兔', 'thoo2'))

    def test_訓用mài(self):
        '教典本文收才準算'
        self.assertFalse(教典.有這對應無('呆', 'phái'))
