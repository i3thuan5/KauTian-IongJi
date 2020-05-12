# Kau3-tian2 Iong7-ji7 教典用字
[![Build Status](https://travis-ci.org/i3thuan5/kau3-tian2_iong7-ji7.svg?branch=master)](https://travis-ci.org/i3thuan5/kau3-tian2_iong7-ji7)
[![Coverage Status](https://coveralls.io/repos/github/i3thuan5/kau3-tian2_iong7-ji7/badge.svg?branch=master)](https://coveralls.io/github/i3thuan5/kau3-tian2_iong7-ji7?branch=master)

這个套件包含[教典的字](https://github.com/g0v/moedict-data-twblg/tree/master/uni)佮[標點符號](https://language.moe.gov.tw/001/upload/files/site_content/m0001/hau/c2.htm)，幫你鬥掠出無合教典的字！

比論講，資料庫有一句：
* 阮是教典用字。 **Guá** sī kàu-tián iōng-jī. 

這个套件掠會著錯誤 **[字：阮 Guá]**

## Installation 安裝

```
pip install kau3-tian2-iong7-ji7
```

## Dependencies 需要的套件

* 臺灣言語工具


## Usage 使用
```
from 臺灣言語工具.基本物件.字 import 字
from 用字 import 建議
建議.有這个字無(字('來', 'lâi'))
```

## Usage of Django model 佇Django使用

本套件目前支援django，有先寫便一个 `用字表` 予使用者加字。

1. 到 `settings.py`，佇 `INSTALLED_APPS` 加上 `用字`。

```
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    ...
+   '用字',
]
```

2. Migrate

```
python manage.py migrate
```

3. 完成！會當用本套件矣。

```
from 臺灣言語工具.基本物件.字 import 字
from 用字.models import 用字表

用字表.有這个字無(字('來', 'lâi'))
```
大量查一kái資料庫ê做法
```
表 = 用字表.這馬()
表.有這个字無(字('來', 'lâi'))
```


4. Option: `settings.py` 決定預設用字範圍，範例
```
IONGJI_KAUTIAN = True
IONGJI_PHIAUTIAM = True
IONGJI_KAMJITIAN = False
```
5. Option. 去後台加字

```
python manage.py runserver
```

## 分開判斷
### [教育部辭典](https://twblg.dict.edu.tw/holodict_new/)詞條、又音 kah 腔口差 ê 用字。
```
from 臺灣言語工具.基本物件.字 import 字
from 用字 import 教典
教典.有這个字無(字('來', 'lâi'))
```

### [教育部標點符號](https://language.moe.gov.tw/001/Upload/FILES/SITE_CONTENT/M0001/HAU/c2.htm) ê 設定。
```
from 臺灣言語工具.基本物件.字 import 字
from 用字 import 標點
標點.有這个字無(字("「", '"'))
```

### [甘字典](http://taigi.fhl.net/dick/) ê 文音。
```
from 臺灣言語工具.基本物件.字 import 字
from 用字 import 甘字典
甘字典.有這个字無(字("「", '"'))
```

## Development 開發

這个模組的理路是共教典內底的字轉做[字物件](https://github.com/i3thuan5/tai5-uan5_gian5-gi2_kang1-ku7/blob/master/%E6%96%87%E4%BB%B6/%E5%9F%BA%E6%9C%AC%E7%89%A9%E4%BB%B6.md#%E4%B8%8A%E6%89%8B)，敆做一个.json檔，了後共json檔藏佇用字表內底。

開發這个套件的試驗主要是咧檢查用字表的程式。所擺你若有改程式，請先重算一擺才閣走試驗。

```
python senn_json.py
python manage.py test
```


