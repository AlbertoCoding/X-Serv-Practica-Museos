# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museosMadrid', '0004_auto_20180428_2216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='museo',
            name='comentario',
        ),
        migrations.AddField(
            model_name='comentario',
            name='museo',
            field=models.ForeignKey(blank=True, to='museosMadrid.Museo', null=True),
        ),
    ]
