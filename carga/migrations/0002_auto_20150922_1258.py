# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carga',
            name='id_carga',
            field=models.CharField(max_length=6),
        ),
    ]
