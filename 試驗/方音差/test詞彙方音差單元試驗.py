from django.test.testcases import TestCase
from 用字.詞彙方音差函式 import 提出一方音的講法


class 提出一方音的講法單元試驗(TestCase):
    def tearDown(self):
        self.assertEqual(
            提出一方音的講法(self.句),
            self.結果
        )

    def test_炊粿(self):
        self.句 = "炊粿　tsher-kér"
        self.結果 = [["炊粿", "tsher-kér"], ]

    def test_病院_醫生館_兩種講法(self):
        self.句 = "病院　pǐnn-ǐnn, 醫生館　i-sing-kuán"
        self.結果 = [["病院", "pǐnn-ǐnn"], ["醫生館", "i-sing-kuán"]]

    def test_tha̍kTtsir_tha̍kTsu_兩種音(self):
        self.句 = "讀書　tha̍k-tsir; tha̍k-tsu"
        self.結果 = [["讀書", "tha̍k-tsir"], ["讀書", "tha̍k-tsu"]]

    def test_暫無資料(self):
        self.句 = "暫無資料　"
        self.結果 = []

    def test_羅馬字括號(self):
        self.句 = "黃昏　hông-hun(書)"
        self.結果 = [["黃昏", "hông-hun"]]

    def test_羅馬字空白括號(self):
        self.句 = "師孫仔　sai-sun-á (背稱)"
        self.結果 = [["師孫仔", "sai-sun-á"]]

    def test_漢字括號(self):
        self.句 = "司孫(背稱)　sai-sun"
        self.結果 = [["司孫", "sai-sun"]]

    def test_羅馬字括號又見音_秤砣(self):
        self.句 = "秤砣　tshìn-thô(tô)"
        self.結果 = [["秤砣", "tshìn-thô"]]

    def test_漢羅兩爿括號_透中晝(self):
        self.句 = "(透)中晝　(thàu)-tiong-tàu"
        self.結果 = [["中晝", "tiong-tàu"]]
