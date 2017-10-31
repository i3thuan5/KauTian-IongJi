import json

from 臺灣言語工具.基本物件.公用變數 import 標點符號
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 用字.公家 import 用字檔名


with open(用字檔名) as 檔案:
    _全部分詞 = set(json.load(檔案))


class 用字表:

    @classmethod
    def 全部分詞(cls):
        return _全部分詞

    @classmethod
    def 有這个字無(cls, 字物件):
        return 字物件.轉音(臺灣閩南語羅馬字拼音).看分詞() in cls.全部分詞()

    @classmethod
    def 是標點符號無(cls, 字物件):
        if 字物件.型 in 標點符號 and 字物件.音 in 標點符號:
            return True
        return False
