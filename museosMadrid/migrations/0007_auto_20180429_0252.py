# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museosMadrid', '0006_museo_puntuacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='nombre',
        ),
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default=b'ejemplo@ejemplo.com', max_length=100),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default=b'ejemplo', max_length=50),
        ),
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.CharField(default=b'ejemplo', max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='color_fondo',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='museos',
            field=models.ManyToManyField(to='museosMadrid.Museo', null=True, blank=True),
        ),
    ]
