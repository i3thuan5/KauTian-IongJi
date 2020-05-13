from 臺灣言語工具.基本物件.字 import 字
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤


def 全部標點():
    return (
        ('。', '.'), ('，', ','), ('、', ','), ('；', ';'),
        ('：', ':'), ('？', '?'), ('！', '!'),
        # 引號
        ('「', '"'), ('」', '"'), ('「', '“'), ('」', '”'),
        ('『', "'"), ('』', "'"), ('『', "‘"), ('』', "’"),
        # 書名號
        ('《', '"'), ('》', '"'), ('《', '“'), ('》', '”'),
        ('〈', '"'), ('〉', '"'), ('〈', '“'), ('〉', '”'),
        # 夾注號甲式
        ('（', '('), ('）', ')'),
        # 破折號、夾注號乙式
        ('──', '──'),
        # 刪節號
        ('……', '...'),
        # 連接號
        ('～', '~'),
        # 間隔號
        ('．', '．'),
    )


def 提全部標點():
    全部用字 = set()
    for 一標點 in 全部標點():
        try:
            全部用字.add(
                字(一標點[0], 一標點[1]).看分詞()
            )
        except 解析錯誤:
            print('無法度匯入標點{}{}'.format(一標點[0], 一標點[1]))
    return 全部用字
