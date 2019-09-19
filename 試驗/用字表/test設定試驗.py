from django.test import TestCase
from django.test.utils import override_settings
from 臺灣言語工具.基本物件.字 import 字
from 用字.models import 用字表
from 用字.models import _theh用字ê範圍


class 設定試驗(TestCase):
    def tearDown(self):
        '愛改轉來，別人才袂出問題'
        self.重讀用字設定()

    def test_預設開教典(self):
        self.assertTrue(用字表.有這个字無(字('媠', 'suí')))

    def test_預設開標點(self):
        self.assertTrue(用字表.有這个字無(字('！', '!')))

    def test_預設關掉(self):
        self.assertFalse(用字表.有這个字無(字('靄', 'Ai2')))

    @override_settings(IONGJI_KAUTIAN=True)
    def test_共教典開開(self):
        self.重讀用字設定()
        self.assertTrue(用字表.有這个字無(字('媠', 'suí')))

    @override_settings(IONGJI_KAUTIAN=False)
    def test_共教典關掉(self):
        self.重讀用字設定()
        self.assertFalse(用字表.有這个字無(字('媠', 'suí')))

    @override_settings(IONGJI_PHIAUTIAM=True)
    def test_共標點開開(self):
        self.重讀用字設定()
        self.assertTrue(用字表.有這个字無(字('！', '!')))

    @override_settings(IONGJI_PHIAUTIAM=False)
    def test_共標點關掉(self):
        self.重讀用字設定()
        self.assertFalse(用字表.有這个字無(字('！', '!')))

    @override_settings(IONGJI_KAMJITIAN=True)
    def test_共甘字典開開(self):
        self.重讀用字設定()
        self.assertTrue(用字表.有這个字無(字('靄', 'Ai2')))

    @override_settings(IONGJI_KAMJITIAN=False)
    def test_共甘字典關掉(self):
        self.重讀用字設定()
        self.assertFalse(用字表.有這个字無(字('靄', 'Ai2')))

    def 重讀用字設定(self):
        用字表._用字ê範圍 = _theh用字ê範圍()
