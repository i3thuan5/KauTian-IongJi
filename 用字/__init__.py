import json
from 用字.公家變數 import 教典檔名
from 用字.標點規範 import 提全部標點
from 用字.書寫 import tsingkuihua


class 字典:
    def __init__(self, 對照):
        self._全部對照 = set(對照)

    def 全部對照(self):
        return self._全部對照

    def 有這个字無(self, 字物件):
        return self.有這對應無(字物件.型, 字物件.音)

    def 有這對應無(self, han, lo):
        han, lo = tsingkuihua(han, lo)
        return (han, lo) in self.全部對照()


def _thakkautian():
    jitian = set()
    with open(教典檔名) as 檔案:
        for ji in json.load(檔案):
            jitian.add(tuple(ji))
    return 字典(jitian)


教典 = _thakkautian()
標點 = 字典(提全部標點())
建議 = 字典(教典.全部對照() | 標點.全部對照())


__all__ = ['教典', '標點', '建議', ]
