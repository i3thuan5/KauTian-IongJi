# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='用字表',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('加入時間', models.DateTimeField(auto_now_add=True)),
                ('分詞', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]
