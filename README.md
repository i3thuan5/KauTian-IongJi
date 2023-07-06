# KauTian-IongJi 教典用字

這个套件包含[教典](https://sutian.moe.edu.tw/zh-hant/siongkuantsuguan/)附錄以外ê詞目羅馬字、詞彙比較kah名、佮[標點符號](https://language.moe.gov.tw/001/upload/files/site_content/m0001/hau/c2.htm)，kā咱掠出無合教典ê字！

```py3
>>> from 用字 import 建議

>>> 建議.有這對應無('來', 'lâi')
True
```

## Installation 安裝

```bash
pip install kau3-tian2-iong7-ji7
```

## Usage 使用

```py3
>>> from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
>>> from 用字 import 建議

>>> 建議.有這个字無(拆文分析器.對齊字物件('來', 'lâi'))
True

>>> 建議.有這个字無(拆文分析器.對齊字物件('囡', 'kiánn'))
False
```

`臺灣言語工具`ê物仔嘛ē-tàng用！

```py3
>>> from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
>>> from 用字 import 建議

>>> 建議.有這个字無(拆文分析器.對齊字物件('來', 'lâi'))
True
```
若規句欲檢查
```py3
>>> from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
>>> from 用字 import 建議

>>> for ji in 拆文分析器.對齊句物件('你來', 'Lí lâi').篩出字物件():
...    建議.有這个字無(ji)
...
True
True
```

## Usage of Django Model 佇Django使用
本套件目前支援django，有先寫便一个 `用字表` 予使用者加字。

1. 到 `settings.py`，佇 `INSTALLED_APPS` 加上 `用字`。
```py3
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    ...
+   '用字',
]
```
2. Migrate：
```bash
python manage.py migrate
```
3. 完成！會當用本套件矣：
```py3
from 用字.models import 用字表

>>> 用字表.有這對應無('來', 'lâi')
True

>>> from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器

>>> 用字表.有這个字無(拆文分析器.對齊字物件('來', 'lâi'))
True
```

## Adding Chars in 用字表 用字表加字

已經有會自動tī admin site註冊，ē-tàng直接tī admin site操作。

若是程式操作，一定ài先`full_clean()`做書寫正規化，親像：

```py3
from 用字.models import 用字表

>>> 字 = 用字表(漢字='來', 羅馬字='lâi')
>>> 字.full_clean()
>>> 字.save()
```


### Optional: 加速 Django 用字表大量查

Kā用字表ê狀態讀入記憶體，適合大量袂更新用字ê時：

```py3
>>> from 用字.models import 用字表

>>> 表 = 用字表.這馬()
>>> 表.有這个字無(拆文分析器.對齊字物件('來', 'lâi'))
True
```


## 分開判斷
### [教育部辭典](https://twblg.dict.edu.tw/holodict_new/)詞條、又音 kah 腔口差 kah 名姓 ê 用字。
```py3
>>> from 用字 import 教典
>>> 教典.有這對應無('來', 'lâi')
True
>>> from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
>>> 教典.有這个字無(拆文分析器.對齊字物件('來', 'lâi'))
True
```

### [教育部標點符號](https://language.moe.gov.tw/001/Upload/FILES/SITE_CONTENT/M0001/HAU/c2.htm) ê 設定

```py3
>>> from 用字 import 標點
>>> 標點.有這對應無('來', 'lâi')
True
>>> from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
>>> 標點.有這个字無(拆文分析器.對齊字物件("「", '"'))
True
```

## Development 開發

這个模組的理路是共教典內底的字敆做一个.json檔，了後共json檔藏佇用字表內底。

開發這个套件的試驗主要是咧檢查用字表的程式。所擺若有改程式，請先重算一擺才閣走試驗。

```bash
tox -e build
tox -e testSiuSu
tox -e testTsingHap
```
