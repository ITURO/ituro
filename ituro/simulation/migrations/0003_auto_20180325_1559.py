# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0002_auto_20180325_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulationstagematch',
            name='cat_password',
            field=models.CharField(default=b'89ade5a0', max_length=100, verbose_name='Cat Password'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='simulationstagematch',
            name='rat_password',
            field=models.CharField(default=b'1f065ec1', max_length=100, verbose_name='Rat Password'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='simulationstagematch',
            name='system_password',
            field=models.CharField(default=b'2375d1da', max_length=100, verbose_name='System Password'),
            preserve_default=True,
        ),
    ]
