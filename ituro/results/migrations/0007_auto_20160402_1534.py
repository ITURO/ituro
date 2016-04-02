# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0006_auto_20160402_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colorselectingresult',
            name='place_partial',
        ),
        migrations.RemoveField(
            model_name='stairclimbingresult',
            name='downstair7',
        ),
        migrations.AlterField(
            model_name='firefighterresult',
            name='is_complete',
            field=models.BooleanField(default=False, verbose_name='Extinguished all candles'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stairclimbingresult',
            name='downstair1',
            field=models.BooleanField(default=False, verbose_name='DownStair #1'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stairclimbingresult',
            name='downstair2',
            field=models.BooleanField(default=False, verbose_name='DownStair #2'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stairclimbingresult',
            name='downstair3',
            field=models.BooleanField(default=False, verbose_name='DownStair #3'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stairclimbingresult',
            name='downstair4',
            field=models.BooleanField(default=False, verbose_name='DownStair #4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stairclimbingresult',
            name='downstair5',
            field=models.BooleanField(default=False, verbose_name='DownStair #5'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stairclimbingresult',
            name='downstair6',
            field=models.BooleanField(default=False, verbose_name='DownStair #6'),
            preserve_default=True,
        ),
    ]
