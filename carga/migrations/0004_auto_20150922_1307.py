# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0003_auto_20150922_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carga',
            name='dados',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='carga',
            name='id_carga',
            field=models.CharField(unique=True, max_length=6),
        ),
    ]
