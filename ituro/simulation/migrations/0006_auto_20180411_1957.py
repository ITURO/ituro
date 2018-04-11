# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0005_auto_20180411_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulationstagematch',
            name='cat_password',
            field=models.CharField(default=b'1a805532', max_length=100, verbose_name='Cat Password'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='simulationstagematch',
            name='rat_password',
            field=models.CharField(default=b'bfe592e9', max_length=100, verbose_name='Rat Password'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='simulationstagematch',
            name='system_password',
            field=models.CharField(default=b'1acc1200', max_length=100, verbose_name='System Password'),
            preserve_default=True,
        ),
    ]
