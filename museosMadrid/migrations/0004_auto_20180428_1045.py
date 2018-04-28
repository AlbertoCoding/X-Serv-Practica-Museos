# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museosMadrid', '0003_auto_20180425_0314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='museo',
            name='id',
        ),
        migrations.AddField(
            model_name='museo',
            name='museo_id',
            field=models.AutoField(default=0, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
