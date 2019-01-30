# Kau3-tian2 Iong7-ji7 教典用字
[![Build Status](https://travis-ci.org/i3thuan5/kau3-tian2_iong7-ji7.svg?branch=master)](https://travis-ci.org/i3thuan5/kau3-tian2_iong7-ji7)
[![Coverage Status](https://coveralls.io/repos/github/i3thuan5/kau3-tian2_iong7-ji7/badge.svg?branch=master)](https://coveralls.io/github/i3thuan5/kau3-tian2_iong7-ji7?branch=master)

這个套件鬥檢查django做底的資料庫，逐句的漢字佮羅馬字敢有合教典用字。

比論講，資料庫有一句：
* 阮是教典用字。 **Guá** sī kàu-tián iōng-jī. 

這个套件會掠著錯誤 **[字：阮 Guá]**

### Usage 使用
```
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 用字.models import 用字表


def 檢查對齊狀態(hanji, lomaji):
    句物件 = 拆文分析器.對齊句物件(hanji, lomaji)
    毋著的字 = []
    字物陣列 = 句物件.篩出字物件()
    for 一字物 in 字物陣列:
        敢有 = 用字表.有這个字無(一字物)
        ...  
```
### Prerequisite 條件

目前干焦支援django。

### Development 開發

這个模組的理路是共教典內底的字轉做[字物件](https://github.com/i3thuan5/tai5-uan5_gian5-gi2_kang1-ku7/blob/master/%E6%96%87%E4%BB%B6/%E5%9F%BA%E6%9C%AC%E7%89%A9%E4%BB%B6.md#%E4%B8%8A%E6%89%8B)，敆做一个.json檔，了後共json檔藏佇用字表內底。

開發這个套件的試驗主要是咧檢查用字表的程式。所擺你若有改程式，請先重算一擺才閣走試驗。

```
python 產生json.py
python manage.py test
```


