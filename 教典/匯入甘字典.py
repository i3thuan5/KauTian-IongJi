# -*- coding: utf-8 -*-

from csv import DictReader
import io
from urllib.request import urlopen


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.羅馬字 import 新白話字
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤


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
                    elif pit['chinese'] == '─':
                        continue
                    elif pit['chinese'].startswith('('):
                        continue
                    try:
                        句物件 = 拆文分析器.建立句物件(pit['chinese'], pit['word'])
                        for 字物件 in 句物件.篩出字物件():
                            yield 字物件.轉音(新白話字)
                    except 解析錯誤 as 錯誤:
                        print(錯誤, pit['example'])
