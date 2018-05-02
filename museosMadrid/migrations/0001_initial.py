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
                ('horario', models.TextField(null=True, blank=True)),
                ('equipamiento', models.TextField(null=True, blank=True)),
                ('transporte', models.TextField(null=True, blank=True)),
                ('accesibilidad', models.BooleanField()),
                ('url', models.CharField(max_length=300, null=True, blank=True)),
                ('nombre_via', models.CharField(max_length=100, null=True, blank=True)),
                ('clase_via', models.CharField(max_length=20, null=True, blank=True)),
                ('tipo_num', models.CharField(max_length=5, null=True, blank=True)),
                ('num', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('localidad', models.CharField(max_length=50, null=True, blank=True)),
                ('provincia', models.CharField(max_length=30, null=True, blank=True)),
                ('codigo_postal', models.PositiveIntegerField(null=True, blank=True)),
                ('barrio', models.CharField(max_length=30, null=True, blank=True)),
                ('distrito', models.CharField(max_length=30, null=True, blank=True)),
                ('coordenada_x', models.IntegerField(null=True, blank=True)),
                ('coordenada_y', models.IntegerField(null=True, blank=True)),
                ('latitud', models.DecimalField(null=True, max_digits=23, decimal_places=20, blank=True)),
                ('longitud', models.DecimalField(null=True, max_digits=23, decimal_places=20, blank=True)),
                ('telefono', models.PositiveIntegerField(null=True, blank=True)),
                ('email', models.CharField(max_length=80, null=True, blank=True)),
                ('fax', models.PositiveIntegerField(null=True, blank=True)),
                ('tipo', models.CharField(max_length=100, null=True, blank=True)),
                ('n_comentarios', models.PositiveSmallIntegerField(default=0)),
                ('puntuacion', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(default=b'ejemplo', max_length=100)),
                ('password', models.CharField(default=b'ejemplo', max_length=50)),
                ('email', models.EmailField(default=b'ejemplo@ejemplo.com', max_length=100)),
                ('color_fondo', models.CharField(max_length=15, null=True, blank=True)),
                ('comentario', models.ForeignKey(blank=True, to='museosMadrid.Comentario', null=True)),
                ('museos', models.ManyToManyField(to='museosMadrid.Museo', null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='comentario',
            name='museo',
            field=models.ForeignKey(blank=True, to='museosMadrid.Museo', null=True),
        ),
    ]
