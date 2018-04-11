# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0004_auto_20180325_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulationstagematch',
            name='cat_password',
            field=models.CharField(default=b'f1712181', max_length=100, verbose_name='Cat Password'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='simulationstagematch',
            name='rat_password',
            field=models.CharField(default=b'ba7f9764', max_length=100, verbose_name='Rat Password'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='simulationstagematch',
            name='system_password',
            field=models.CharField(default=b'8807f361', max_length=100, verbose_name='System Password'),
            preserve_default=True,
        ),
    ]
