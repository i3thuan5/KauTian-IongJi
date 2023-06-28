from kesi import Ku, TuiBeTse
from 用字.書寫 import tsingkuihua
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from django.db import models
from django.core.exceptions import ValidationError
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 用字 import 字典
from 用字 import 建議


class 用字表(models.Model):
    漢字 = models.CharField(max_length=5)
    羅馬字 = models.CharField(max_length=15)
    分詞 = models.CharField(max_length=20, blank=True)
    _用字ê範圍 = 建議.全部分詞()

    @classmethod
    def 有這个字無(cls, 字物件):
        return cls.有這對應無(字物件.型, 字物件.音)

    @classmethod
    def 有這對應無(cls, han, lo):
        han, lo = tsingkuihua(han, lo)
        字物件 = 拆文分析器.建立字物件(han, lo)
        字分詞 = 字物件.看分詞()
        if 字分詞 in cls._用字ê範圍:
            return True
        return cls.objects.filter(分詞=字分詞).exists()

    def clean(self):
        hantng = len(list(Ku(self.漢字).thianji()))
        lotng = len(list(Ku(self.羅馬字).thianji()))
        if hantng != 1 or lotng != 1:
            raise ValidationError('漢羅攏ài拄好一ê字，漢字有{}字，羅馬字有{}字'.format(
                hantng, lotng
            ))
        han, lo = tsingkuihua(self.漢字, self.羅馬字)
        字物件 = 拆文分析器.建立字物件(han, lo)
        self.分詞 = 字物件.看分詞()
        super().clean()

    @classmethod
    def 這馬(cls):
        return 字典(cls.全部分詞())

    @classmethod
    def 全部分詞(cls):
        return cls._用字ê範圍 | set(cls.objects.values_list('分詞', flat=True))
