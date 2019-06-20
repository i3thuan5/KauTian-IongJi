import json
from 用字.公家變數 import 甘字典檔名
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


with open(甘字典檔名) as 檔案:
    _全部分詞 = set(json.load(檔案))


class 甘字典:

    @classmethod
    def 全部分詞(cls):
        return _全部分詞

    @classmethod
    def 有這个字無(cls, 字物件):
        字臺羅物件 = 字物件.轉音(臺灣閩南語羅馬字拼音)
        # 不檢查輕聲符
        字臺羅物件.音 = 字臺羅物件.音.lstrip('0')
        return 字臺羅物件.看分詞() in cls.全部分詞()
