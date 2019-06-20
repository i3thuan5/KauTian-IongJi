from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from django.db import models
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from django.conf import settings
from 用字 import 標點
from 用字 import 教典
from 用字.甘字典規範 import 甘字典


class 用字表(models.Model):
    漢字 = models.CharField(max_length=5)
    羅馬字 = models.CharField(max_length=15)
    分詞 = models.CharField(max_length=20)

    @classmethod
    def 有這个字無(cls, 字物件):
        字臺羅物件 = 字物件.轉音(臺灣閩南語羅馬字拼音)
        字臺羅物件.音 = 字臺羅物件.音.lstrip('0')
        有無 = False
        # 先揣教典、標點json
        敢開教典 = getattr(settings, '敢開教典', True)
        敢開標點 = getattr(settings, '敢開標點', True)
        敢開甘字典 = getattr(settings, '敢開甘字典', False)
        if 敢開教典:
            有無 = 有無 or 教典.有這个字無(字臺羅物件)
        if 敢開標點:
            有無 = 有無 or 標點.有這个字無(字臺羅物件)
        if 敢開甘字典:
            有無 = 有無 or 甘字典.有這个字無(字臺羅物件)
        # 揣用字表
        if 有無 is False:
            字分詞 = 字臺羅物件.看分詞()
            有無 = 有無 or cls.objects.filter(分詞=字分詞).exists()
        return 有無

    def save(self, *args, **kwargs):
        # 提掉舊的輕聲規範
        羅馬字 = self.羅馬字.lstrip('0')
        self.分詞 = (
            拆文分析器.對齊字物件(self.漢字, 羅馬字)
            .轉音(臺灣閩南語羅馬字拼音)
            .看分詞()
        )
        super(用字表, self).save(*args, **kwargs)
