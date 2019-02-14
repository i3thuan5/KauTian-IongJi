from unittest.case import TestCase
from 臺灣言語工具.基本物件.字 import 字
from 用字 import 標點



class 標點試驗(TestCase):
    
    def test_引號(self):
        self.assertTrue(標點.有這个字無(字("「", '"')))