from django.test.testcases import TestCase
from 臺灣言語工具.基本物件.字 import 字
from 用字.models import 用字表
from 用字.匯入資料 import 教典字物件


class 匯入詞彙方音差表單元試驗(TestCase):

    #    序號,方言差編碼,詞目,鹿港,三峽,臺北,宜蘭,臺南,高雄,金門,馬公,新竹,臺中

    def test_鹿港_粿(self):
        #    713,[方1]0716,蒸,炊粿　tsher-kér,
        self.assertTrue(用字表.有這个字無(字('粿', 'kér')))

    def test_鹿港_病院kah醫生館兩種講法(self):
        #    1,[方1]0001,醫院,"病院　pǐnn-ǐnn, 醫生館　i-sing-kuán",
        self.assertTrue(用字表.有這个字無(字('病', 'pǐnn')))

    def test_新竹_讀書_tsir_kah_tsu兩種音(self):
        #    14,[方1]0014,讀書,...,讀書　tha̍k-tsir; tha̍k-tsu
        self.assertTrue(用字表.有這个字無(字('書', 'tsir')))


class 提出一方音的陣列單元試驗(TestCase):

    def test_炊粿(self):
        self.assertEqual(
            教典字物件.提出一方音的陣列("炊粿　tsher-kér"),
            [["炊粿", "tsher-kér"], ]
        )

    def test_兩種講法(self):
        self.assertEqual(
            教典字物件.提出一方音的陣列("病院　pǐnn-ǐnn, 醫生館　i-sing-kuán"),
            [["病院", "pǐnn-ǐnn"], ["醫生館", "i-sing-kuán"]]
        )

    def test_兩種音(self):
        self.assertEqual(
            教典字物件.提出一方音的陣列("讀書　tha̍k-tsir; tha̍k-tsu"),
            [["讀書", "tha̍k-tsir"], ["讀書", "tha̍k-tsu"]]
        )
