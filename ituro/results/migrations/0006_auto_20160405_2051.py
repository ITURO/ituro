# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0005_auto_20150411_1241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basketballresult',
            options={'ordering': ['disqualification', '-score', 'minutes', 'seconds', 'milliseconds'], 'verbose_name': 'Basketball Result', 'verbose_name_plural': 'Basketball Results'},
        ),
        migrations.AlterModelOptions(
            name='selfbalancingresult',
            options={'ordering': ['disqualification', '-score', '-seconds', '-milliseconds', '-headway_amount', 'stage3_minutes', 'stage3_seconds', 'stage3_milliseconds'], 'verbose_name': 'Self Balancing Result', 'verbose_name_plural': 'Self Balancing Results'},
        ),
        migrations.RemoveField(
            model_name='basketballresult',
            name='total',
        ),
        migrations.RemoveField(
            model_name='colorselectingresult',
            name='obtain',
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
            name='interfering_robots',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Interfering Robots Count'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='firefighterresult',
            name='is_complete',
            field=models.BooleanField(default=False, verbose_name='Extinguish All Candles'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='firefighterresult',
            name='pre_start_extinguish',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Pre-start Extinguish Count'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='firefighterresult',
            name='touching_candles',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Touching Candles Count'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scenarioresult',
            name='blocks',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Obtained blocks'),
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
            name='stage3_milliseconds',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Stage3 Milliseconds'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='selfbalancingresult',
            name='stage3_minutes',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Stage3 Minutes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='selfbalancingresult',
            name='stage3_seconds',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Stage3 Seconds'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stairclimbingresult',
            name='down1',
            field=models.BooleanField(default=False, verbose_name='Down #1'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stairclimbingresult',
            name='down2',
            field=models.BooleanField(default=False, verbose_name='Down #2'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stairclimbingresult',
            name='down3',
            field=models.BooleanField(default=False, verbose_name='Down #3'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stairclimbingresult',
            name='down4',
            field=models.BooleanField(default=False, verbose_name='Down #4'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stairclimbingresult',
            name='down5',
            field=models.BooleanField(default=False, verbose_name='Down #5'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stairclimbingresult',
            name='down6',
            field=models.BooleanField(default=False, verbose_name='Down #6'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stairclimbingresult',
            name='is_complete',
            field=models.BooleanField(default=False, verbose_name='Finish the race ?'),
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
        migrations.AlterField(
            model_name='colorselectingresult',
            name='place_partial',
            field=models.PositiveSmallIntegerField(verbose_name='Cylinder Not in Leaving Area Count'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='firefighterresult',
            name='extinguish_failure',
            field=models.PositiveSmallIntegerField(verbose_name='Extinguish with Penalty Count'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='firefighterresult',
            name='wall_hit',
            field=models.PositiveSmallIntegerField(verbose_name='Touching Wall Count'),
            preserve_default=True,
        ),
    ]
