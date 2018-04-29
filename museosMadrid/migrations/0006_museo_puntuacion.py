# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museosMadrid', '0005_auto_20180429_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='museo',
            name='puntuacion',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
