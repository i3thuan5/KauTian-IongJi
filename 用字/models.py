from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from django.db import models
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 用字表(models.Model):
    漢字 = models.CharField(max_length=5)
    羅馬字 = models.CharField(max_length=15)
    分詞 = models.CharField(max_length=20)
    
    @classmethod
    def 有這个字無(cls, 字物件):
        字臺羅物件 = 字物件.轉音(臺灣閩南語羅馬字拼音)
        字臺羅物件.音 = 字臺羅物件.音.lstrip('0')
        字分詞 = 字臺羅物件.看分詞()
        return cls.objects.filter(分詞=字分詞).exists()
        
    def save(self, *args, **kwargs):
        # 提掉舊的輕聲規範
        羅馬字 = self.羅馬字.lstrip('0')
        self.分詞 = (
            拆文分析器.對齊字物件(self.漢字, 羅馬字)
            .轉音(臺灣閩南語羅馬字拼音)
            .看分詞()
        )
        super(用字表, self).save(*args, **kwargs)