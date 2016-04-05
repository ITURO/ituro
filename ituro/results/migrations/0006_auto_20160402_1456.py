# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0005_auto_20150411_1241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='selfbalancingresult',
            options={'ordering': ['disqualification', '-score', '-seconds', '-milliseconds', '-headway_amount', 'parcour3_minutes', 'parcour3_seconds', 'parcour3_milliseconds'], 'verbose_name': 'Self Balancing Result', 'verbose_name_plural': 'Self Balancing Results'},
        ),
        migrations.RemoveField(
            model_name='selfbalancingresult',
            name='headway_milliseconds',
        ),
        migrations.RemoveField(
            model_name='selfbalancingresult',
            name='headway_minutes',
        ),
        migrations.RemoveField(
            model_name='selfbalancingresult',
            name='headway_seconds',
        ),
        migrations.RemoveField(
            model_name='selfbalancingresult',
            name='impact',
        ),
        migrations.RemoveField(
            model_name='stairclimbingresult',
            name='downstairs',
        ),
        migrations.AddField(
            model_name='basketballresult',
            name='basket5',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Basket 5'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='firefighterresult',
            name='extinguish_penalty',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Extinguish with penalty Count'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='firefighterresult',
            name='interfering_robot',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Interfering Robot Count'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='firefighterresult',
            name='is_complete',
            field=models.BooleanField(default=True, verbose_name='Extinguished all candles'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='firefighterresult',
            name='touching_candles',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Touching Candles Count'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scenarioresult',
            name='obtain_block',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Obtained Block Count'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scenarioresult',
            name='total_referee_point',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Total Referee Point'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='selfbalancingresult',
            name='parcour3_milliseconds',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Parcour3 Milliseconds'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='selfbalancingresult',
            name='parcour3_minutes',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Parcour3 Minutes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='selfbalancingresult',
            name='parcour3_seconds',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Parcour3 Seconds'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stairclimbingresult',
            name='downstair1',
            field=models.BooleanField(default=False, verbose_name='Stair #1'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stairclimbingresult',
            name='downstair2',
            field=models.BooleanField(default=False, verbose_name='Stair #2'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stairclimbingresult',
            name='downstair3',
            field=models.BooleanField(default=False, verbose_name='Stair #3'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stairclimbingresult',
            name='downstair4',
            field=models.BooleanField(default=False, verbose_name='Stair #4'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stairclimbingresult',
            name='downstair5',
            field=models.BooleanField(default=False, verbose_name='Stair #5'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stairclimbingresult',
            name='downstair6',
            field=models.BooleanField(default=False, verbose_name='Stair #6'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stairclimbingresult',
            name='downstair7',
            field=models.BooleanField(default=False, verbose_name='Stair #7'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stairclimbingresult',
            name='is_complete',
            field=models.BooleanField(default=False, verbose_name='Is Complete?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stairclimbingresult',
            name='stair5',
            field=models.BooleanField(default=False, verbose_name='Stair #5'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stairclimbingresult',
            name='stair6',
            field=models.BooleanField(default=False, verbose_name='Stair #6'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stairclimbingresult',
            name='stair7',
            field=models.BooleanField(default=False, verbose_name='Stair #7'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stairclimbingresult',
            name='touching_plexy',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Touching Plexy Count'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='firefighterresult',
            name='extinguish_failure',
            field=models.PositiveSmallIntegerField(verbose_name='Pre-extinguishing Count'),
            preserve_default=True,
        ),
    ]
