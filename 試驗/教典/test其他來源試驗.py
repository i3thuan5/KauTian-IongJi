from 用字 import 教典
from unittest.case import TestCase


class 用字試驗(TestCase):

    def test_牽水tsn̄g(self):
        self.assertTrue(教典.有這對應無('𰹬', 'tsn̄g'))
