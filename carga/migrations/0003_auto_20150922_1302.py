# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0002_auto_20150922_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carga',
            name='dados',
            field=models.TextField(),
        ),
    ]
