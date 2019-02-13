from django.test.testcases import TestCase
from 臺灣言語工具.基本物件.字 import 字
from 用字.models import 用字表
from unittest.case import skip


class 用字試驗(TestCase):

    def test_字物件(self):
        self.assertTrue(用字表.有這个字無(字('來', 'lai5')))

    def test_輕聲有(self):
        self.assertTrue(用字表.有這个字無(字('來', '0lai5')))

    def test_無輕聲(self):
        self.assertTrue(用字表.有這个字無(字('巧', '0khiau2')))

    def test_干焦輕聲(self):
        self.assertTrue(用字表.有這个字無(字('啦', '0lah4')))

    def test_無實調(self):
        self.assertTrue(用字表.有這个字無(字('啦', 'lah4')))

    def test_羅馬字佮羅馬字(self):
        self.assertFalse(用字表.有這个字無(字('lai5', 'lai5')))

    def test_又見音表(self):
        self.assertTrue(用字表.有這个字無(字('觸', 'tau2')))

    def test_例句表(self):
        self.assertTrue(用字表.有這个字無(字('𪜶', '0in1')))

    def test_附錄地名提掉(self):
        self.assertFalse(用字表.有這个字無(字('醫', 'penn7')))

    @skip('因為教典的詞目總檔有收基|ke')
    def test_附錄地名基隆_基提掉(self):
        self.assertFalse(用字表.有這个字無(字('基', 'ke1')))

    def test_附錄地名基隆_隆提掉(self):
        self.assertFalse(用字表.有這个字無(字('隆', 'lang5')))

    def test_大寫(self):
        self.assertTrue(用字表.有這个字無(字('啊', 'Ah')))

    def test_無這音(self):
        self.assertFalse(用字表.有這个字無(字('媠', 'sui')))

    def test_傳統調符(self):
        self.assertTrue(用字表.有這个字無(字('成', 'sîng')))

    def test_那卡西ながし(self):
        self.assertFalse(用字表.有這个字無(字('那', 'な')))
