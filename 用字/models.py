from django.db import models
from 臺灣言語工具.基本物件.公用變數 import 標點符號
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


class 用字表(models.Model):
    加入時間 = models.DateTimeField(auto_now_add=True)
    分詞 = models.CharField(max_length=200, unique=True)

    @classmethod
    def 全部分詞(cls):
        return set(cls.objects.all().values_list('分詞', flat=True))

    @classmethod
    def 有這个字無(cls, 字物件):
        分詞 = 字物件.轉音(臺灣閩南語羅馬字拼音).看分詞()
        try:
            if cls.是標點符號無(字物件):
                return True
            return cls.objects.filter(分詞=分詞).exists()
        except:
            return False

    @classmethod
    def 是標點符號無(cls, 字物件):
        if 字物件.型 in 標點符號 and 字物件.音 in 標點符號:
            return True
        return False

    def __str__(self):
        return self.分詞
