from 用字 import 教典
from unittest.case import TestCase


class 用字語音方言差試驗(TestCase):

    #    序號,方言差編碼,字目,鹿港,三峽,臺北,宜蘭,臺南,高雄,金門,馬公,新竹,臺中
    #    2 1,[方]005,欲,berh,berh,beh,beh,beh,beh,berh,boh,beh,beh

    def test_鹿港_粿(self):
        self.assertTrue(教典.有這對應無('母', 'biór'))

    def test_指_無收著臺中腔(self):
        #    26,[方]358,指,tsńg,... ,x
        self.assertFalse(教典.有這對應無('指', 'x'))
