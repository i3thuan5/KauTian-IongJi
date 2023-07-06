from django.test.testcases import TestCase
from 試驗.用字表.test用字表試驗 import 用字表加詞
from django.core.management import call_command


class 這馬表試驗(TestCase, 用字表加詞):

    def test_有正規化(self):
        self.用字表create(漢字='來', 羅馬字='lâi')
        call_command('用字表重正規化')
