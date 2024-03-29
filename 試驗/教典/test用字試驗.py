from 用字 import 教典
from unittest.case import TestCase


class 用法試驗(TestCase):

    def test_傳統調符(self):
        self.assertTrue(教典.有這對應無('來', 'lâi'))

    def test_數字調(self):
        self.assertTrue(教典.有這對應無('來', 'lai5'))

    def test_大寫(self):
        self.assertTrue(教典.有這對應無('來', 'Lâi'))

    def test_輕聲符(self):
        self.assertTrue(教典.有這對應無('來', '--lâi'))

    def test_舊輕聲(self):
        self.assertTrue(教典.有這對應無('來', '0lai5'))

    def test_干焦輕聲(self):
        self.assertTrue(教典.有這對應無('啦', '0lah4'))

    def test_無實調(self):
        self.assertTrue(教典.有這對應無('啦', 'lah4'))

    def test_羅馬字佮羅馬字(self):
        self.assertFalse(教典.有這對應無('lai5', 'lai5'))

    def test_漢羅長短bôkâng(self):
        self.assertFalse(教典.有這對應無('來', 'lai5-lai5'))
