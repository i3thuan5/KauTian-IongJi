from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from django.conf import settings
from django.db import models
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 用字 import 標點
from 用字 import 教典
from 用字 import 甘字典
from 用字 import 字典


def _theh用字ê範圍():
    範圍 = set()
    if getattr(settings, 'IONGJI_KAUTIAN', True):
        範圍 |= 教典.全部分詞()
    if getattr(settings, 'IONGJI_PHIAUTIAM', True):
        範圍 |= 標點.全部分詞()
    if getattr(settings, 'IONGJI_KAMJITIAN', False):
        範圍 |= 甘字典.全部分詞()
    return 範圍


class 用字表(models.Model):
    漢字 = models.CharField(max_length=5)
    羅馬字 = models.CharField(max_length=15)
    分詞 = models.CharField(max_length=20)
    _用字ê範圍 = _theh用字ê範圍()

    @classmethod
    def 有這个字無(cls, 字物件):
        字臺羅物件 = 字物件.轉音(臺灣閩南語羅馬字拼音)
        字臺羅物件.音 = 字臺羅物件.音.lstrip('0')
        字臺羅物件.輕聲標記 = False
        字分詞 = 字臺羅物件.看分詞()
        if 字分詞 in cls._用字ê範圍:
            return True
        return cls.objects.filter(分詞=字分詞).exists()

    def save(self, *args, **kwargs):
        # 提掉舊的輕聲規範
        羅馬字 = self.羅馬字.lstrip('0')
        字臺羅物件 = (
            拆文分析器.對齊字物件(self.漢字, 羅馬字)
            .轉音(臺灣閩南語羅馬字拼音)
        )
        字臺羅物件.輕聲標記 = False
        self.分詞 = 字臺羅物件.看分詞()
        super(用字表, self).save(*args, **kwargs)

    @classmethod
    def 這馬(cls):
        return 字典(cls.全部分詞())

    @classmethod
    def 全部分詞(cls):
        return cls._用字ê範圍 | set(cls.objects.values_list('分詞', flat=True))
