# -*- coding: utf-8 -*-
from 用字.匯入資料 import 教典字物件
import json
from 用字.公家 import 教典檔名


def 產生json():
    全部用字 = set()
    for 字物件 in 教典字物件.全部資料():
        全部用字.add(
            字物件.看分詞()
        )
    with open(教典檔名, 'w') as 檔案:
        json.dump(
            sorted(全部用字), 檔案,
            indent=2,
            ensure_ascii=False
        )


if __name__ == '__main__':
    產生json()
