from unittest.case import TestCase
from 臺灣言語工具.基本物件.字 import 字


class Mia(TestCase):
    'https://docs.google.com/spreadsheets/u/1/d/1yNKBf8NcYj00iH6zVETMB9LwNZf0HCg0fekp8zlNrRY/export?format=csv&id=1yNKBf8NcYj00iH6zVETMB9LwNZf0HCg0fekp8zlNrRY&gid=1608156122'

    def test_erm(self):
        self.assertTrue(教典名姓.有這个字無(字('鍼', 'tserm')))

    def test_ionn(self):
        self.assertTrue(教典名姓.有這个字無(字('薔', 'tshiônn')))
