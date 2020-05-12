from unittest.case import TestCase, skip
from 臺灣言語工具.基本物件.字 import 字
from 用字 import 教典名姓


@skip
class Senn(TestCase):

    def test_irn(self):
        self.assertTrue(教典名姓.有這个字無(字('釔', 'It')))

    def test_unicode(self):
        self.assertTrue(教典名姓.有這个字無(字('\U0002F829', 'Pau')))
