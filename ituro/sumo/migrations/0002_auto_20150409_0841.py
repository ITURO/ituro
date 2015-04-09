# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sumo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sumogroupmatch',
            name='order',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Order'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sumogroupteam',
            name='average',
            field=models.IntegerField(default=0, verbose_name='Average'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sumogroupteam',
            name='order',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Order'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sumogroupteam',
            name='point',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Point'),
            preserve_default=True,
        ),
    ]
