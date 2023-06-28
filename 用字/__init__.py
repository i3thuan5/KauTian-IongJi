import json
from 用字.公家變數 import 教典檔名
from 用字.標點規範 import 提全部標點
from 臺灣言語工具.羅馬字 import 新白話字
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


class 字典:
    def __init__(self, 分詞):
        self._全部分詞 = set(分詞)

    def 全部分詞(self):
        return self._全部分詞

    def 有這个字無(self, 字物件):
        return self.有這對應無(字臺羅物件.型, 字臺羅物件.音)

    def 有這對應無(self, han, lo):
        ku = Ku(han.lstrip('-'), lo.lstrip('0').lstrip('-')).TL()
        字物件 = 拆文分析器.建立字物件(ku.hanlo, ku.lomaji)
        return 字物件.看分詞() in self.全部分詞()


with open(教典檔名) as 檔案:
    教典 = 字典(json.load(檔案))
標點 = 字典(提全部標點())
建議 = 字典(教典.全部分詞() | 標點.全部分詞())


__all__ = ['教典', '標點', '建議', ]
