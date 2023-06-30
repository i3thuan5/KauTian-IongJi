from 臺灣言語工具.基本物件.字 import 字
from 用字 import 教典
from unittest.case import skip, TestCase


class 用字試驗(TestCase):

    def test_又見音表(self):
        self.assertTrue(教典.有這个字無(字('觸', 'tau2')))

    def test_附錄地名提掉(self):
        self.assertFalse(教典.有這个字無(字('醫', 'penn7')))

    @skip('因為教典的詞目總檔有收基|ke')
    def test_附錄地名基隆_基提掉(self):
        self.assertFalse(教典.有這个字無(字('基', 'ke1')))

    def test_附錄地名基隆_隆提掉(self):
        self.assertFalse(教典.有這个字無(字('隆', 'lang5')))

    def test_那卡西ながし(self):
        self.assertFalse(教典.有這个字無(字('那', 'な')))

    def test_無這音(self):
        self.assertFalse(教典.有這个字無(字('媠', 'sui')))
