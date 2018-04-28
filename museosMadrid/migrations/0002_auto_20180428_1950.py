# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museosMadrid', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='museo',
            name='barrio',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='clase_via',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='codigo_postal',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='coordenada_x',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='coordenada_y',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='distrito',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='email',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='equipamiento',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='horario',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='latitud',
            field=models.DecimalField(null=True, max_digits=23, decimal_places=20, blank=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='localidad',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='longitud',
            field=models.DecimalField(null=True, max_digits=23, decimal_places=20, blank=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='nombre_via',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='num',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='provincia',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='telefono',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='tipo',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='tipo_num',
            field=models.CharField(max_length=5, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='transporte',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='url',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
    ]
