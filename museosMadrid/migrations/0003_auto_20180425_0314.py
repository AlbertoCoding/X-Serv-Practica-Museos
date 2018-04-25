# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museosMadrid', '0002_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='museo',
            name='comentario',
            field=models.ForeignKey(blank=True, to='museosMadrid.Comentario', null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='comentario',
            field=models.ForeignKey(blank=True, to='museosMadrid.Comentario', null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='museos',
            field=models.ManyToManyField(to='museosMadrid.Museo', blank=True),
        ),
    ]
