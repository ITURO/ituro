# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0003_auto_20180325_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simulationstagematch',
            name='is_played',
        ),
        migrations.AlterField(
            model_name='simulationstagematch',
            name='cat_password',
            field=models.CharField(default=b'2b211be0', max_length=100, verbose_name='Cat Password'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='simulationstagematch',
            name='rat_password',
            field=models.CharField(default=b'4ee5429b', max_length=100, verbose_name='Rat Password'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='simulationstagematch',
            name='system_password',
            field=models.CharField(default=b'9adcff7a', max_length=100, verbose_name='System Password'),
            preserve_default=True,
        ),
    ]
