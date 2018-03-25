# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulationstagematch',
            name='cat_password',
            field=models.CharField(default=b'6b2d75e7-9', max_length=100, verbose_name='Cat Password'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationstagematch',
            name='rat_password',
            field=models.CharField(default=b'6637f0b6-d', max_length=100, verbose_name='Rat Password'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationstagematch',
            name='system_password',
            field=models.CharField(default=b'ba432ba1-6', max_length=100, verbose_name='System Password'),
            preserve_default=True,
        ),
    ]
