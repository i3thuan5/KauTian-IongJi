# -*- coding: utf-8 -*-

from csv import DictReader
import io
from urllib.request import urlopen


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 教典字物件:
    github = 'https://github.com/g0v/moedict-data-twblg/raw/master/uni/'
    詞目總檔網址 = github + '%E8%A9%9E%E7%9B%AE%E7%B8%BD%E6%AA%94.csv'
    詞目總檔屬性網址 = github + '%E8%A9%9E%E7%9B%AE%E7%B8%BD%E6%AA%94.%E8%A9%9E%E7%9B%AE%E5%B1%AC%E6%80%A7%E5%B0%8D%E7%85%A7.csv'
    又音網址 = github + '%E5%8F%88%E9%9F%B3.csv'
    例句網址 = github + '%E4%BE%8B%E5%8F%A5.csv'

    #
    # 撈出教典的字
    #
    @classmethod
    def 全部資料(cls):
        yield from cls.詞目總檔()
        yield from cls.又見音表()
        yield from cls.例句()

    #
    # 主編碼,屬性,詞目,音讀,文白屬性,部首
    # 6,1,一月日,tsi̍t gue̍h-ji̍t/tsi̍t ge̍h-li̍t,0,
    #
    @classmethod
    def 詞目總檔(cls):
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
                        try:
                            for 字物件 in (
                                拆文分析器
                                .對齊組物件(漢字, 臺羅)
                                .篩出字物件()
                            ):
                                yield 字物件
                        except Exception as 錯誤:
                            print(錯誤)

    #
    # 該詞目在漳泉腔音讀以外的又見音。
    # 序號 主編碼 又音 又音類型(1.又唸作 2.俗唸作 3.合音唸作)
    #   3   72    tsa̍p-jī-tsí-tn̂g/tsa̍p-lī-tsí-tn̂g    1
    #
    @classmethod
    def 又見音表(cls):
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
                        try:
                            for 字物件 in (
                                拆文分析器
                                .對齊組物件(漢字, 臺羅)
                                .篩出字物件()
                            ):
                                yield 字物件
                        except Exception as 錯誤:
                            print(錯誤)

    #
    # 從例句檔撈字。
    # 因為詞目總檔不見得有包括例句的字。
    #
    @classmethod
    def 例句(cls):

        with urlopen(cls.例句網址) as 檔:
            with io.StringIO(檔.read().decode()) as 資料:
                for row in DictReader(資料):
                    音讀 = row['例句標音'].strip()
                    漢字 = row['例句'].strip()
                    try:
                        for 字物件 in (
                            拆文分析器
                            .對齊句物件(漢字, 音讀)
                            .篩出字物件()
                        ):
                            yield 字物件
                    except Exception as 錯誤:
                        print(錯誤)
