from 用字.公家變數 import 甘字典檔名
import json
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 用字.公家變數 import 教典檔名
from 用字.標點規範 import 提全部標點


class 字典:
    def __init__(self, 分詞):
        self._全部分詞 = set(分詞)

    def 全部分詞(self):
        return self._全部分詞

    def 有這个字無(self, 字物件):
        字臺羅物件 = 字物件.轉音(臺灣閩南語羅馬字拼音)
        # 不檢查輕聲符
        字臺羅物件.音 = 字臺羅物件.音.lstrip('0')
        return 字臺羅物件.看分詞() in self.全部分詞()


with open(教典檔名) as 檔案:
    教典 = 字典(json.load(檔案))
標點 = 字典(提全部標點())
with open(甘字典檔名) as 檔案:
    甘字典 = 字典(json.load(檔案))

__all__ = ['教典', '標點', '甘字典']
