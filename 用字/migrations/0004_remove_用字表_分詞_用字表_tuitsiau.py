# Generated by Django 4.2.2 on 2023-07-03 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('用字', '0003_alter_用字表_分詞'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='用字表',
            name='分詞',
        ),
        migrations.AddConstraint(
            model_name='用字表',
            constraint=models.UniqueConstraint(fields=('漢字', '羅馬字'), name='tuitsiau'),
        ),
    ]
