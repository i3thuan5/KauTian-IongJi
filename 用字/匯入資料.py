# -*- coding: utf-8 -*-

from csv import DictReader
import io
from urllib.request import urlopen


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 用字.詞彙方言差函式 import 揣括號
from 用字.詞彙方言差函式 import 提出一方言的講法


class 教典字物件:
    github = 'https://github.com/g0v/moedict-data-twblg/raw/master/uni/'
    詞目總檔網址 = github + '%E8%A9%9E%E7%9B%AE%E7%B8%BD%E6%AA%94.csv'
    詞目總檔屬性網址 = github + '%E8%A9%9E%E7%9B%AE%E7%B8%BD%E6%AA%94.%E8%A9%9E%E7%9B%AE%E5%B1%AC%E6%80%A7%E5%B0%8D%E7%85%A7.csv'
    又音網址 = github + '%E5%8F%88%E9%9F%B3.csv'
    例句網址 = github + '%E4%BE%8B%E5%8F%A5.csv'
    詞彙方言差網址 = github + '%E8%A9%9E%E5%BD%99%E6%96%B9%E8%A8%80%E5%B7%AE.csv'
    語音方言差網址 = github + '%E8%AA%9E%E9%9F%B3%E6%96%B9%E8%A8%80%E5%B7%AE.csv'

    #
    # 撈出教典的字
    #
    @classmethod
    def 全部資料(cls):
        yield from cls.詞目總檔()
        yield from cls.又見音表()
        yield from cls.例句()
        yield from cls.詞彙方言差()
        yield from cls.語音方言差()

    #
    # 主編碼,屬性,詞目,音讀,文白屬性,部首
    # 6,1,一月日,tsi̍t gue̍h-ji̍t/tsi̍t ge̍h-li̍t,0,
    #
    @classmethod
    def 詞目總檔(cls):
        print('匯入詞目總檔...')
        會使的屬性 = set()
        with urlopen(cls.詞目總檔屬性網址) as 檔:
            with io.StringIO(檔.read().decode()) as 資料:
                for row in DictReader(資料):
                    if '地名' not in row['屬性'].strip():
                        會使的屬性.add(row['編號'].strip())
        with urlopen(cls.詞目總檔網址) as 檔:
            with io.StringIO(檔.read().decode()) as 資料:
                for row in DictReader(資料):
                    音讀 = row['音讀'].strip()
                    if 音讀 == '' or row['屬性'].strip() not in 會使的屬性:
                        continue
                    漢字 = row['詞目'].strip()
                    for 一音 in 音讀.split('/'):
                        臺羅 = 一音.strip()
                        yield from 擲出字物件(漢字, 臺羅)

    #
    # 該詞目在漳泉腔音讀以外的又見音。
    # 序號 主編碼 又音 又音類型(1.又唸作 2.俗唸作 3.合音唸作)
    #   3   72    tsa̍p-jī-tsí-tn̂g/tsa̍p-lī-tsí-tn̂g    1
    #
    @classmethod
    def 又見音表(cls):
        print('匯入又見音表...')
        資料 = {}
        with urlopen(cls.詞目總檔網址) as 檔:
            with io.StringIO(檔.read().decode()) as 字串資料:
                for row in DictReader(字串資料):
                    主編碼 = row['主編碼'].strip()
                    漢字 = row['詞目'].strip()
                    資料[主編碼] = 漢字

        with urlopen(cls.又音網址) as 檔:
            with io.StringIO(檔.read().decode()) as 字串資料:
                for row in DictReader(字串資料):
                    if row['又音類型(1.又唸作 2.俗唸作 3.合音唸作)'] == '3':
                        continue
                    主編碼 = row['主編碼'].strip()
                    漢字 = 資料[主編碼]
                    for 一音 in row['又音'].split('/'):
                        臺羅 = 一音.strip()
                        yield from 擲出字物件(漢字, 臺羅)

    #
    # 從例句檔撈字。
    # 因為詞目總檔不見得有包括例句的字。
    #
    @classmethod
    def 例句(cls):
        print('匯入例句表...')
        with urlopen(cls.例句網址) as 檔:
            with io.StringIO(檔.read().decode()) as 資料:
                for row in DictReader(資料):
                    音讀 = row['例句標音'].strip()
                    漢字 = row['例句'].strip()
                    yield from 擲出字物件(漢字, 音讀)

    @classmethod
    def 詞彙方言差(cls):
        print('匯入詞彙方言差...')
        with urlopen(cls.詞彙方言差網址) as 檔:
            with io.StringIO(檔.read().decode()) as 表:
                for row in DictReader(表):
                    for key, val in sorted(row.items()):
                        if key in ['序號', '方言差編碼', '詞目']:
                            continue
                        講法陣列 = 提出一方言的講法(val)
                        for 一講法 in 講法陣列:
                            yield from 擲出字物件(一講法[0], 一講法[1])
    #
    # 字的方言表
    #

    @classmethod
    def 語音方言差(cls):
        print('匯入語音方言差...')
        with urlopen(cls.語音方言差網址) as 檔:
            with io.StringIO(檔.read().decode()) as 表:
                for row in DictReader(表):
                    漢字 = 揣括號.sub('', row['字目'])
                    for key in ['鹿港', '三峽', '臺北', '宜蘭', '臺南', '高雄',
                                '金門', '馬公', '新竹', '臺中', ]:
                        # 該腔口無收著
                        if row[key] == 'x':
                            continue
                        # 提出一个腔口的無仝講法
                        音 = 揣括號.sub('', row[key]).replace(' ', '')
                        音陣列 = 音.split(';')
                        for 一音 in 音陣列:
                            yield from 擲出字物件(漢字, 一音)


def 擲出字物件(句漢, 句羅):
    try:
        for 字物件 in (
            拆文分析器
            .對齊句物件(句漢, 句羅)
            .篩出字物件()
        ):
            yield 字物件
    except Exception as e:
        print('擲出字物件:', str(e))
