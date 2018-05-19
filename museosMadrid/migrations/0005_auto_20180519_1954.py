# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museosMadrid', '0004_auto_20180519_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='museos',
            field=models.ManyToManyField(to='museosMadrid.Museo', null=True, blank=True),
        ),
    ]
