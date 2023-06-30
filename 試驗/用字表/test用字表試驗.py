from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.test.testcases import TestCase
from django.urls import reverse
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 用字.models import 用字表


class 用字表加詞:
    def 用字表create(self, 漢字, 羅馬字):
        lang = User.objects.create_superuser(
            'ithuan', 'ithuan@ithuan.tw', 'it'
        )
        self.client.force_login(lang)

        autai_url = reverse('admin:用字_用字管理表_add')
        response = self.client.post(
            autai_url,
            {'漢字': 漢字, '羅馬字': 羅馬字}
        )
        self.assertEqual(response.status_code, 302)


class 用字表試驗(TestCase, 用字表加詞):

    def test_無加字(self):
        漢 = '媠'
        羅 = 'khiáu'
        self.assertFalse(用字表.有這个字無(拆文分析器.對齊字物件(漢, 羅))

    def test_加一字(self):
        漢 = '媠'
        羅 = 'khiáu'
        self.用字表create(漢字=漢, 羅馬字=羅)
        self.assertTrue(用字表.有這个字無(拆文分析器.對齊字物件(漢, 羅))

    def test_數字調(self):
        漢 = '媠'
        羅 = 'khiau2'
        self.用字表create(漢字=漢, 羅馬字=羅)
        self.assertTrue(用字表.有這个字無(拆文分析器.對齊字物件(漢, 羅))

    def test_大寫(self):
        漢 = '媠'
        羅 = 'Khiáu'
        self.用字表create(漢字=漢, 羅馬字=羅)
        self.assertTrue(用字表.有這个字無(拆文分析器.對齊字物件(漢, 羅))

    def test_一定àithinn字bēsái詞(self):
        漢 = '符合'
        羅 = 'hù-ha̍p'
        with self.assertRaises(ValidationError):
            用字表(漢字=漢, 羅馬字=羅).full_clean()

    def test_加符號(self):
        漢 = '~'
        羅 = '―'
        self.用字表create(漢字=漢, 羅馬字=羅)
        self.assertTrue(用字表.有這个字無(拆文分析器.對齊字物件(漢, 羅))

    def test_輕聲符(self):
        self.用字表create(漢字='媠', 羅馬字='--khiáu')
        self.assertTrue(用字表.有這个字無(
            拆文分析器.對齊字物件('媠', '--khiáu'))

    def test_輕聲符2(self):
        self.用字表create(漢字='媠', 羅馬字='--khiáu')
        self.assertTrue(用字表.有這个字無(
            拆文分析器.對齊字物件('媠', 'khiáu'))

    def test_輕聲符4(self):
        self.用字表create(漢字='媠', 羅馬字='khiáu')
        self.assertTrue(用字表.有這个字無(
            拆文分析器.對齊字物件('媠', '--khiáu'))

    def test_0輕聲符(self):
        self.用字表create(漢字='媠', 羅馬字='0khiáu')
        self.assertTrue(用字表.有這个字無(
            拆文分析器.對齊字物件('媠', '0khiáu'))

    def test_0輕聲符2(self):
        self.用字表create(漢字='媠', 羅馬字='0khiáu')
        self.assertTrue(用字表.有這个字無(
            拆文分析器.對齊字物件('媠', 'khiáu'))

    def test_0輕聲符4(self):
        self.用字表create(漢字='媠', 羅馬字='khiáu')
        self.assertTrue(用字表.有這个字無(
            拆文分析器.對齊字物件('媠', '0khiáu'))
