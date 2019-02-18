from django.contrib import admin
from 用字.models import 用字表

# 佇admin的名顯示"用字表"


class 用字管理表(用字表):
    class Meta:
        proxy = True
        verbose_name = "用字表"
        verbose_name_plural = verbose_name


class 用字表後台(admin.ModelAdmin):
    # change list
    list_display = ['id', '漢字', '羅馬字', '分詞', ]
    search_fields = ['id', '漢字', '羅馬字', '分詞', ]
    # change view
    fields = ('漢字', '羅馬字',)


admin.site.register(用字管理表, 用字表後台)
