# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museosMadrid', '0005_auto_20180519_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='titulo',
            field=models.CharField(default=b'Pagina del usuario', max_length=300),
        ),
    ]
