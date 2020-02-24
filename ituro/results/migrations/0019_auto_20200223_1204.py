# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0018_auto_20200219_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mazeresult',
            name='project',
        ),
        migrations.DeleteModel(
            name='MazeResult',
        ),
        migrations.RemoveField(
            model_name='innovativejuryresult',
            name='digital_design',
        ),
        migrations.RemoveField(
            model_name='linefootballresult',
            name='dribble_milliseconds',
        ),
        migrations.RemoveField(
            model_name='linefootballresult',
            name='dribble_minutes',
        ),
        migrations.RemoveField(
            model_name='linefootballresult',
            name='dribble_seconds',
        ),
        migrations.RemoveField(
            model_name='stairclimbingresult',
            name='down1',
        ),
        migrations.RemoveField(
            model_name='stairclimbingresult',
            name='down2',
        ),
        migrations.RemoveField(
            model_name='stairclimbingresult',
            name='down3',
        ),
        migrations.RemoveField(
            model_name='stairclimbingresult',
            name='down4',
        ),
        migrations.RemoveField(
            model_name='stairclimbingresult',
            name='down5',
        ),
        migrations.RemoveField(
            model_name='stairclimbingresult',
            name='down6',
        ),
        migrations.AddField(
            model_name='constructionresult',
            name='carried_block',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='carried_block'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='constructionresult',
            name='refere_point',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='refere_point'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stairclimbingresult',
            name='floor_landing',
            field=models.BooleanField(default=False, verbose_name='floor landing'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stairclimbingresult',
            name='stair8',
            field=models.BooleanField(default=False, verbose_name='Stair #8'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stairclimbingresult',
            name='stair9',
            field=models.BooleanField(default=False, verbose_name='Stair #9'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='trafficresult',
            name='light_fail',
            field=models.PositiveSmallIntegerField(default=0, verbose_name=b'fail light'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='trafficresult',
            name='light_succeed',
            field=models.PositiveSmallIntegerField(default=0, verbose_name=b'succeed light'),
            preserve_default=True,
        ),
    ]
