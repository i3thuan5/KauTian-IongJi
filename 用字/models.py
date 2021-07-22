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
        字臺羅物件 = 字物件.轉音(臺灣閩南語羅馬字拼音)
        字臺羅物件.型 = 字臺羅物件.型.lstrip('-')
        字臺羅物件.音 = 字臺羅物件.音.lstrip('0').lstrip('-')
        字臺羅物件.輕聲標記 = False
        字分詞 = 字臺羅物件.看分詞()
        if 字分詞 in cls._用字ê範圍:
            return True
        return cls.objects.filter(分詞=字分詞).exists()

    def clean(self):
        # 提掉舊的輕聲規範
        羅馬字 = self.羅馬字.lstrip('0').lstrip('-')
        漢字 = self.漢字.lstrip('-')
        try:
            詞物件 = 拆文分析器.對齊詞物件(漢字, 羅馬字)
        except 解析錯誤:
            raise ValidationError('漢羅ài攏是一ê字')
        if len(詞物件.篩出字物件()) > 1:
            raise ValidationError('漢羅ài攏是一ê字')
        字臺羅物件 = (
            詞物件.篩出字物件()[0]
            .轉音(臺灣閩南語羅馬字拼音)
        )
        字臺羅物件.輕聲標記 = False
        self.分詞 = 字臺羅物件.看分詞()
        super().clean()

    @classmethod
    def 這馬(cls):
        return 字典(cls.全部分詞())

    @classmethod
    def 全部分詞(cls):
        return cls._用字ê範圍 | set(cls.objects.values_list('分詞', flat=True))
