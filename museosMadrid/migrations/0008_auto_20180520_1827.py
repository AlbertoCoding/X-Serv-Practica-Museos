# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museosMadrid', '0007_usuario_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='color_fondo',
        ),
        migrations.AddField(
            model_name='usuario',
            name='bgcolor',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='usuario',
            name='cletras',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='usuario',
            name='tletras',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
