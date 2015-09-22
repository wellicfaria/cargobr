# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0004_auto_20150922_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carga',
            name='dados',
            field=models.TextField(),
        ),
    ]
