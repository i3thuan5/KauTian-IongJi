from 用字.models import 用字表
from django.test.testcases import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 試驗.用字表.test用字表試驗 import 用字表加詞


class 這馬表試驗(TestCase, 用字表加詞):

    def test_有加著字(self):
        漢 = '媠'
        羅 = 'khiáu'
        self.用字表create(漢字=漢, 羅馬字=羅)
        self.assertTrue(用字表.這馬().有這个字無(拆文分析器.對齊字物件(漢, 羅))

    def test_提出來了後就bôtshap資料庫有加著字(self):
        漢 = '媠'
        羅 = 'khiáu'
        表 = 用字表.這馬()
        self.用字表create(漢字=漢, 羅馬字=羅)
        self.assertFalse(表.有這个字無(拆文分析器.對齊字物件(漢, 羅))
