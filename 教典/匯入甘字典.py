# -*- coding: utf-8 -*-

from csv import DictReader
import io
from urllib.request import urlopen
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 教典字物件:
    github = 'https://github.com/fhl-net/Kam-Ui-lim_1913_Kam-Ji-tian.git/'

#     def 全部資料(self):
#         yield from self.詞目()
        
    def 詞目(self):
        with urlopen(self.資料網址) as tsuliau:
            with io.StringIO(tsuliau.read().decode('utf-8')) as tong:
                for pit in DictReader(tong):
                    if pit['word'][0].isupper():
                        continue
                    elif pit['chinese'] == '●':
                        continue
                    elif pit['chinese'] == '—':
                        continue
                    elif pit['chinese'].startswith_fws('('):
                        continue
                    print(pit)
#                     yield 拆文分析器.建立句物件(pit['word'], pit['chinese'])



