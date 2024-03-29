# -*- coding: utf-8 -*-
import io
import json
from urllib.request import urlopen
from pyexcel_ods3 import get_data
from kesi import Ku, TuiBeTse, kam_haphuat
from kesi.butkian.kongiong import 標點符號
from os.path import join, abspath, dirname
from csv import DictReader


def tsingkuihua(han, lo):
    ku = Ku(han.lstrip('-').lower(), lo.lstrip('0').lstrip('-').lower()).TL()
    return ku.hanlo, ku.lomaji


def 產生教典json():
    教典檔名 = join(dirname(abspath(__file__)), '..', '用字', '教典.json')

    全部用字 = []

    for han, lo in set(教典字物件().全部資料()):
        han, lo = han.lstrip('-'), lo.lstrip('-')
        if kam_haphuat(lo):
            全部用字.append(
                (han, lo)
            )
    with open(教典檔名, 'w') as 檔案:
        json.dump(
            sorted(全部用字), 檔案,
            indent=2,
            ensure_ascii=False
        )


class 教典字物件:
    教典ods網址 = 'https://sutian.moe.edu.tw/media/kautian.ods'
    教典名màiti̍h = join(dirname(__file__), 'mia-mai-tih.csv')
    其他來源csv = join(dirname(__file__), 'kithann.csv')

    def 全部資料(self):
        yield from self.新教典ods()
        yield from self.其他來源()

    def 新教典ods(self):
        with urlopen(self.教典ods網址) as 檔:
            with io.BytesIO(檔.read()) as 資料:
                kiatko = get_data(資料)

        for ji in self._tshue_ji(kiatko):
            han, lo = tsingkuihua(ji.hanlo.lower(), ji.lomaji.lower())
            if han not in 標點符號:
                yield han, lo
        piaute = kiatko['語音差異'][0]
        hanjiui = piaute.index('漢字')
        for tsua in kiatko['語音差異'][1:]:
            han = tsua[hanjiui]
            for lo_tsong in tsua[hanjiui+1:]:
                if lo_tsong.strip():
                    for lo in lo_tsong.split(','):
                        yield han, lo

    def _tshue_ji(self, kiatko):
        for mia, pio in kiatko.items():
            if mia not in ['詞目', '又唸作', '合音唸作', '俗唸作', '詞彙比較', '名']:
                continue
            piaute = pio[0]
            try:
                hanjiui = piaute.index('漢字')
                lomajiui = piaute.index('羅馬字')
            except ValueError:
                continue
            if mia == '詞目':
                luihingui = piaute.index('詞目類型')

                def tiaukiann(tsua):
                    return tsua[luihingui] != '附錄' or (
                        tsua[luihingui] == '附錄' and len(tsua[hanjiui]) == 1
                    )
            elif mia == '名':
                luihingui = piaute.index('類型')
                mài_ti̍h = set()
                with open(self.教典名màiti̍h) as tong:
                    for tsua in DictReader(tong):
                        mài_ti̍h.add(tsua['漢字'])

                def tiaukiann(tsua):
                    eingtit = ['又', '官', '文', '泉', '甘', '白', '不標', ]
                    return (
                        tsua[hanjiui] not in mài_ti̍h and
                        (luihingui >= len(tsua) or tsua[luihingui] in eingtit)
                    )
            else:
                def tiaukiann(tsua):
                    return True
            for tsua in pio[1:]:
                try:
                    hanji = tsua[hanjiui]
                    lomajitin = tsua[lomajiui]
                except IndexError:
                    '無羅馬字ê時，tsua無平長'
                    continue
                for lomaji in lomajitin.split('/'):
                    try:
                        for ji in Ku(hanji, lomaji).thianji():
                            if tiaukiann(tsua):
                                yield ji
                    except TuiBeTse:
                        pass

    def 其他來源(self):
        with open(self.其他來源csv) as tong:
            for tsua in DictReader(tong):
                yield tsua['漢字'], tsua['羅馬字']
