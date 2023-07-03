from kesi import Ku
from 用字.書寫 import tsingkuihua
from django.db import models
from django.core.exceptions import ValidationError
from 用字 import 字典
from 用字 import 建議


class 用字表(models.Model):
    漢字 = models.CharField(max_length=5)
    羅馬字 = models.CharField(max_length=15)
    _用字ê範圍 = 建議.全部對照()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['漢字', '羅馬字'], name='tuitsiau'),
        ]

    @classmethod
    def 有這个字無(cls, 字物件):
        return cls.有這對應無(字物件.型, 字物件.音)

    @classmethod
    def 有這對應無(cls, han, lo):
        han, lo = tsingkuihua(han, lo)
        if (han, lo) in cls._用字ê範圍:
            return True
        return cls.objects.filter(漢字=han, 羅馬字=lo).exists()

    def clean(self):
        hantng = len(list(Ku(self.漢字).thianji()))
        lotng = len(list(Ku(self.羅馬字).thianji()))
        if hantng != 1 or lotng != 1:
            raise ValidationError('漢羅攏ài拄好一ê字，漢字有{}字，羅馬字有{}字'.format(
                hantng, lotng
            ))
        self.漢字, self.羅馬字 = tsingkuihua(self.漢字, self.羅馬字)
        super().clean()

    @classmethod
    def 這馬(cls):
        return 字典(cls.全部對照())

    @classmethod
    def 全部對照(cls):
        tsuanpoo = set(cls._用字ê範圍)
        for ji in cls.objects.values_list('漢字', '羅馬字'):
            tsuanpoo.add(tuple(ji))
        return tsuanpoo
