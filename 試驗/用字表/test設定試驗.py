from django.test import TestCase
from 臺灣言語工具.基本物件.字 import 字
from 用字.models import 用字表
from django.test.utils import override_settings


class 設定試驗(TestCase):
    def test_預設開教典(self):
        self.assertTrue(用字表.有這个字無(字('媠', 'suí')))

    def test_預設開標點(self):
        self.assertTrue(用字表.有這个字無(字('！', '!')))

    @override_settings(敢開教典=True)
    def test_共教典開開(self):
        self.assertTrue(用字表.有這个字無(字('媠', 'suí')))

    @override_settings(敢開教典=False)
    def test_共教典關掉(self):
        self.assertFalse(用字表.有這个字無(字('媠', 'suí')))

    @override_settings(敢開標點=True)
    def test_共標點開開(self):
        self.assertTrue(用字表.有這个字無(字('！', '!')))

    @override_settings(敢開標點=False)
    def test_共標點關掉(self):
        self.assertFalse(用字表.有這个字無(字('！', '!')))
