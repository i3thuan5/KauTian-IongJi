import re


揣括號 = re.compile(r'\(.*?\)')

# 對詞彙方音差表內底提出逐个方音


def 提出一方言的講法(方音):
    # 1　1a; 1b, 2　2c,
    結果 = []
    講法陣列 = 方音.split(',')
    for 一講法 in 講法陣列:
        # 跳過標示暫無資料的欄位
        講法 = 一講法.strip().replace('暫無資料', '')
        if not 講法:
            continue

        # 取出此講法的全部漢字音讀
        漢字, 音讀 = 揣括號.sub('', 講法).split('　')
        音讀陣列 = 音讀.strip('-').split(';')
        for 一音讀 in 音讀陣列:
            # 括號總提掉
            音讀 = 一音讀.strip()
            結果.append([漢字, 音讀])
    return 結果
