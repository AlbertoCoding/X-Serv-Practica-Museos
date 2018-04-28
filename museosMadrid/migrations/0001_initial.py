# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('autor', models.CharField(max_length=50)),
                ('texto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Museo',
            fields=[
                ('museo_id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('horario', models.TextField(blank=True)),
                ('equipamiento', models.TextField(blank=True)),
                ('transporte', models.TextField(blank=True)),
                ('accesibilidad', models.BooleanField()),
                ('url', models.CharField(max_length=300)),
                ('nombre_via', models.CharField(max_length=100, blank=True)),
                ('clase_via', models.CharField(max_length=20, blank=True)),
                ('tipo_num', models.CharField(max_length=5, blank=True)),
                ('num', models.PositiveSmallIntegerField(blank=True)),
                ('localidad', models.CharField(max_length=50, blank=True)),
                ('provincia', models.CharField(max_length=30, blank=True)),
                ('codigo_postal', models.PositiveIntegerField(blank=True)),
                ('barrio', models.CharField(max_length=30, blank=True)),
                ('distrito', models.CharField(max_length=30, blank=True)),
                ('coordenada_x', models.IntegerField(blank=True)),
                ('coordenada_y', models.IntegerField(blank=True)),
                ('latitud', models.DecimalField(max_digits=23, decimal_places=20, blank=True)),
                ('longitud', models.DecimalField(max_digits=23, decimal_places=20, blank=True)),
                ('telefono', models.PositiveIntegerField(blank=True)),
                ('email', models.CharField(max_length=80, blank=True)),
                ('tipo', models.CharField(max_length=100, blank=True)),
                ('comentario', models.ForeignKey(blank=True, to='museosMadrid.Comentario', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('comentario', models.ForeignKey(blank=True, to='museosMadrid.Comentario', null=True)),
                ('museos', models.ManyToManyField(to='museosMadrid.Museo', blank=True)),
            ],
        ),
    ]
