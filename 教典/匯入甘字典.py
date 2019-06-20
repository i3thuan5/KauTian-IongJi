# -*- coding: utf-8 -*-

from _ast import Try
from csv import DictReader
import io
from urllib.request import urlopen

import 臺灣言語工具


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


class 甘字典字物件:
    資料網址 = 'https://github.com/fhl-net/Kam-Ui-lim_1913_Kam-Ji-tian/raw/master/dict.csv'

    def 詞目(self):
        with urlopen(self.資料網址) as tsuliau:
            with io.StringIO(tsuliau.read().decode('utf-8')) as tong:
                for pit in DictReader(tong):
                    pit['chinese'] = pit['chinese'].strip()
                    pit['word'] = pit['word'].strip()
                    if pit['word'].isupper():
                        continue
                    elif pit['chinese'] == '●':
                        continue
                    elif pit['chinese'] == '—':
                        continue
                    elif pit['chinese'].startswith('('):
                        continue
                    try:
                        字物件 = 拆文分析器.建立字物件(pit['chinese'], pit['word'])
                        yield 字物件.轉音(臺灣閩南語羅馬字拼音)
                    except 臺灣言語工具.解析整理.解析錯誤.解析錯誤 as 錯誤:
                        print(錯誤)
