from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 用字 import 教典
from unittest.case import TestCase


class 用法試驗(TestCase):
    def test_傳統調符(self):
        self.assertTrue(教典.有這个字無(拆文分析器.對齊字物件('來', 'lâi')))

    def test_數字調(self):
        self.assertTrue(教典.有這个字無(拆文分析器.對齊字物件('來', 'lai5')))

    def test_大寫(self):
        self.assertTrue(教典.有這个字無(拆文分析器.對齊字物件('來', 'Lâi')))

    def test_輕聲符(self):
        self.assertTrue(教典.有這个字無(拆文分析器.對齊字物件('來', 'lai5', 輕聲標記=True)))

    def test_舊輕聲(self):
        self.assertTrue(教典.有這个字無(拆文分析器.對齊字物件('來', '0lai5')))

    def test_干焦輕聲(self):
        self.assertTrue(教典.有這个字無(拆文分析器.對齊字物件('啦', '0lah4')))

    def test_無實調(self):
        self.assertTrue(教典.有這个字無(拆文分析器.對齊字物件('啦', 'lah4')))

    def test_羅馬字佮羅馬拆文分析器.對齊字物件(self):
        self.assertFalse(教典.有這个字無(拆文分析器.對齊字物件('lai5', 'lai5')))

    def test_句物件應用(self):
        hanji = '林--先-生'
        lomaji = 'Lîm--sian-sinn'
        句物件 = 拆文分析器.建立句物件(hanji, lomaji)
        for 字物件 in 句物件.篩出字物件():
            self.assertTrue(教典.有這个字無(字物件), 字物件)
