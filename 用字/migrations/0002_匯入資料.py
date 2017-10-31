# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 11:27
from __future__ import unicode_literals

from csv import DictReader
import io
from urllib.request import urlopen

from django.db import migrations


from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


def 匯入用字(app, editor):
    用字表 = app.get_model("用字", "用字表")
    for 字物件 in 教典資料.全部資料():
        用字表.objects.get_or_create(分詞=字物件.轉音(臺灣閩南語羅馬字拼音).看分詞())


class 教典資料:
    詞目總檔網址 = 'https://github.com/g0v/moedict-data-twblg/raw/master/uni/%E8%A9%9E%E7%9B%AE%E7%B8%BD%E6%AA%94.csv'
    詞目總檔屬性網址 = 'https://github.com/g0v/moedict-data-twblg/raw/master/uni/%E8%A9%9E%E7%9B%AE%E7%B8%BD%E6%AA%94.%E5%B1%AC%E6%80%A7%E5%B0%8D%E7%85%A7.csv'
    又音網址 = 'https://github.com/g0v/moedict-data-twblg/raw/master/uni/%E5%8F%88%E9%9F%B3.csv'

    @classmethod
    def 全部資料(cls):
        yield from cls._詞目總檔()
        yield from cls._又見音表()

    @classmethod
    def _詞目總檔(cls):
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
                        整理後漢字 = 文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 漢字)
                        整理後臺羅 = 文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 臺羅)
                        try:
                            for 字物件 in (
                                拆文分析器
                                .對齊組物件(整理後漢字, 整理後臺羅)
                                .篩出字物件()
                            ):
                                yield 字物件
                        except Exception as 錯誤:
                            print(錯誤)

    @classmethod
    def _又見音表(cls):
        資料 = {}
        with urlopen(cls.詞目總檔網址) as 檔:
            with io.StringIO(檔.read().decode()) as 字串資料:
                for row in DictReader(字串資料):
                    主編碼 = row['主編碼'].strip()
                    漢字 = row['詞目'].strip()
                    音讀 = row['音讀'].split('/')[0].strip()
                    資料[主編碼] = (漢字, 音讀)

        with urlopen(cls.又音網址) as 檔:
            with io.StringIO(檔.read().decode()) as 字串資料:
                for row in DictReader(字串資料):
                    if row['又音類型(1.又唸作 2.俗唸作 3.合音唸作)'] == '3':
                        continue
                    主編碼 = row['主編碼'].strip()
                    (優勢腔漢字, _優勢腔音讀) = 資料[主編碼]
                    優勢腔整理後漢字 = 文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 優勢腔漢字)
                    for 一音 in row['又音'].split('/'):
                        臺羅 = 一音.strip()
                        整理後臺羅 = 文章粗胚.建立物件語句前處理減號(臺灣閩南語羅馬字拼音, 臺羅)
                        try:
                            for 字物件 in (
                                拆文分析器
                                .對齊組物件(優勢腔整理後漢字, 整理後臺羅)
                                .篩出字物件()
                            ):
                                yield 字物件
                        except Exception as 錯誤:
                            print(錯誤)


class Migration(migrations.Migration):

    dependencies = [
        ('用字', '0001_initial'),
    ]

    operations = [
        # migrations.RunPython(匯入用字, lambda *x:x),
    ]
