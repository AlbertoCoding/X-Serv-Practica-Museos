# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museosMadrid', '0006_usuario_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='count',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
