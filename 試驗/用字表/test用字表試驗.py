from unittest.case import TestCase
from 臺灣言語工具.基本物件.字 import 字
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤



class 用字表試驗(TestCase):
    
    def test_無加字(self):
        漢 = '媠'
        羅 = 'khiáu'
        self.assertFalse(用字表.有這个字無(字(漢, 羅)))
                        
    def test_加一字(self):
        漢 = '媠'
        羅 = 'khiáu'
        用字表.objects.create(漢, 羅)
        self.assertTrue(用字表.有這个字無(字(漢, 羅)))
    
    def test_數字調(self):
        漢 = '媠'
        羅 = 'khiau2'
        用字表.objects.create(漢, 羅)
        self.assertTrue(用字表.有這个字無(字(漢, 羅)))
    
    def test_大寫(self):
        漢 = '媠'
        羅 = 'Khiáu'
        用字表.objects.create(漢, 羅)
        self.assertTrue(用字表.有這个字無(字(漢, 羅)))
    
    def test_足濟字(self):
        漢 = '媠媠'
        羅 = 'khiáu-khiáu'
        with self.assertRaises(解析錯誤):
            用字表.objects.create(漢, 羅)
    
    def test_加符號(self):
        漢 = '~'
        羅 = '―'
        用字表.objects.create(漢, 羅)
        self.assertTrue(用字表.有這个字無(字(漢, 羅)))