# -*- coding: utf-8 -*-
import io
from urllib.request import urlopen
from pyexcel_ods3 import get_data
from kesi import Ku, TuiBeTse
from kesi.butkian.kongiong import 標點符號


class 教典字物件:
    教典ods網址 = 'https://sutian.moe.edu.tw/media/kautian.ods'

    def 全部資料(self):
        yield from self.新教典ods()
        '教育部《咱來學臺灣閩南語：讀文章蓋趣味01》、內政部 宗教百景'
        yield '𰹬', 'tsn̄g'

    def 新教典ods(self):
        with urlopen(self.教典ods網址) as 檔:
            with io.BytesIO(檔.read()) as 資料:
                kiatko = get_data(資料)

        for ji in self._tshue_ji(kiatko):
            phe = ji.hanlo.lower(), ji.lomaji.lower()
            if ji.hanlo not in 標點符號:
                yield phe

    def _tshue_ji(self, kiatko):
        for mia, pio in kiatko.items():
            if mia == '漢字羅馬字對應':
                continue
            piaute = pio[0]
            try:
                hanjiui = piaute.index('漢字')
                lomajiui = piaute.index('羅馬字')
            except ValueError:
                continue
            if mia == '詞目':
                luihingui = piaute.index('詞目類型')
            else:
                luihingui = None
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
                            if luihing and tsua[luihingui] != '附錄':
                                yield ji
                    except TuiBeTse:
                        pass
