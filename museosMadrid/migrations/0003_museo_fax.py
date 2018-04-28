# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museosMadrid', '0002_auto_20180428_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='museo',
            name='fax',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
