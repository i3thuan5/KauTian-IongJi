# -*- coding: utf-8 -*-

import csv
import io
from urllib.request import urlopen


from 教典.匯入資料 import 擲出字物件


class 教典名姓字物件:
    sheet = (
        'https://docs.google.com/spreadsheets/u/1/d/'
        '1yNKBf8NcYj00iH6zVETMB9LwNZf0HCg0fekp8zlNrRY/'
    )
    mia_bangtsi = (
        sheet +
        'export?format=csv&' +
        'id=1yNKBf8NcYj00iH6zVETMB9LwNZf0HCg0fekp8zlNrRY&gid=1608156122'
    )
    senn_bangtsi = (
        sheet +
        'export?format=csv&' +
        'id=1yNKBf8NcYj00iH6zVETMB9LwNZf0HCg0fekp8zlNrRY&gid=1612622647'
    )

    @classmethod
    def 全部資料(cls):
        yield from cls.mia()
        '出現罕用字，顛倒困擾'
        # yield from cls.senn()

    @classmethod
    def mia(cls):
        print('匯入mia...')

        eingtit = ['又', '官', '文', '泉', '甘', '白', '不標', ]
        beingtit = ['訓', '俗', ]

        with urlopen(cls.mia_bangtsi) as 檔:
            with io.StringIO(檔.read().decode()) as 資料:
                for kui, row in enumerate(csv.reader(資料)):
                    if kui == 0:
                        continue
                    for pit in row[1:]:
                        if row[0] in ['兔', '𠕆', ]:
                            continue
                        if pit.rstrip() == '':
                            continue
                        lo, *au = pit.split('(')
                        if len(au) == 0:
                            pass
                        elif len(au) == 1:
                            hing = au[0].rstrip(')')
                            if hing in eingtit:
                                pass
                            elif hing in beingtit:
                                continue
                            else:
                                lo = pit
                        yield from 擲出字物件(row[0], lo)

    @classmethod
    def senn(cls):
        print('匯入senn...')
        with urlopen(cls.senn_bangtsi) as 檔:
            with io.StringIO(檔.read().decode()) as 資料:
                for kui, row in enumerate(csv.reader(資料)):
                    if kui == 0:
                        continue
                    han = row[2].rstrip()
                    if len(han) >= 1:
                        pass
                    else:
                        ma = row[1].strip()
                        if len(ma) == 0:
                            print('姓漢字bô字元：{} {}'.format(kui + 1, row))
                            continue
                        han = chr(int(row[1], 16))
                    for lo in row[3:]:
                        if lo.rstrip() != '':
                            yield from 擲出字物件(han, lo)
