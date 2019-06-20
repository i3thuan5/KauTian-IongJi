# -*- coding: utf-8 -*-
import json
from os.path import join, abspath, dirname
from 教典.匯入甘字典 import 甘字典字物件


def 產生json():
    檔名 = join(dirname(abspath(__file__)), '用字','甘字典.json')
    
    全部用字 = set()
    for 字物件 in 甘字典字物件().詞目():
        全部用字.add(
            字物件.看分詞()
        )
    with open(檔名, 'w') as 檔案:
        json.dump(
            sorted(全部用字), 檔案,
            indent=2,
            ensure_ascii=False
        )


if __name__ == '__main__':
    產生json()
