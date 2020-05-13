from django.test import TestCase
from 臺灣言語工具.基本物件.字 import 字
from 用字.models import 用字表


class 設定試驗(TestCase):

    def test_預設開教典(self):
        self.assertTrue(用字表.有這个字無(字('媠', 'suí')))

    def test_預設開標點(self):
        self.assertTrue(用字表.有這个字無(字('！', '!')))

    def test_預設開教典名姓(self):
        self.assertTrue(用字表.有這个字無(字('靄', 'Ai2')))
