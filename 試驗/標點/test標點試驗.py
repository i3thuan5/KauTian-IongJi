from unittest.case import TestCase, skip
from 用字 import 標點


class 標點試驗(TestCase):

    def test_引號(self):
        self.assertTrue(標點.有這對應無("「", '"'))

    @skip('予言語工具分析器處理濟字的標點')
    def test_刪節號(self):
        self.assertTrue(標點.有這對應無("……", '...'))

    @skip('英文沒有書名號')
    def test_書名號(self):
        self.assertTrue(標點.有這對應無("《", ''))

    @skip('英文沒有間隔號')
    def test_間隔號(self):
        self.assertTrue(標點.有這對應無("．", ''))
