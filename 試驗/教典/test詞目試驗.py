from 用字 import 教典
from unittest.case import skip, TestCase


class 用字試驗(TestCase):

    def test_又見音表(self):
        self.assertTrue(教典.有這對應無('觸', 'tau2'))

    def test_附錄地名提掉(self):
        self.assertFalse(教典.有這對應無('醫', 'penn7'))

    @skip('因為教典的詞目總檔有收基|ke')
    def test_附錄地名基隆_基提掉(self):
        self.assertFalse(教典.有這對應無('基', 'ke1'))

    def test_附錄地名基隆_隆提掉(self):
        self.assertFalse(教典.有這對應無('隆', 'lang5'))

    def test_那卡西ながし(self):
        self.assertFalse(教典.有這對應無('那', 'な'))

    def test_無這音(self):
        self.assertFalse(教典.有這對應無('媠', 'sui'))

    def test_姓(self):
        self.assertTrue(教典.有這對應無('薛', 'sih'))
