# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basketballresult',
            options={'ordering': ['disqualification', '-score', 'total', 'minutes', 'seconds', 'milliseconds'], 'verbose_name': 'Basketball Result', 'verbose_name_plural': 'Basketball Results'},
        ),
        migrations.AlterModelOptions(
            name='colorselectingresult',
            options={'ordering': ['disqualification', '-score', 'minutes', 'seconds', 'milliseconds'], 'verbose_name': 'Color Selecting Result', 'verbose_name_plural': 'Color Selecting Results'},
        ),
        migrations.AlterModelOptions(
            name='firefighterresult',
            options={'ordering': ['disqualification', '-score', 'minutes', 'seconds', 'milliseconds'], 'verbose_name': 'Fire Fighter Result', 'verbose_name_plural': 'Fire Fighter Results'},
        ),
        migrations.AlterModelOptions(
            name='mazeresult',
            options={'ordering': ['disqualification', 'minutes', 'seconds', 'milliseconds'], 'verbose_name': 'Maze Result', 'verbose_name_plural': 'Maze Results'},
        ),
        migrations.AlterModelOptions(
            name='selfbalancingresult',
            options={'ordering': ['disqualification', '-score', '-seconds', '-milliseconds', '-headway_amount', 'headway_minutes', 'headway_seconds', 'headway_milliseconds'], 'verbose_name': 'Self Balancing Result', 'verbose_name_plural': 'Self Balancing Results'},
        ),
        migrations.AlterModelOptions(
            name='stairclimbingresult',
            options={'ordering': ['disqualification', '-score', 'minutes', 'seconds', 'milliseconds'], 'verbose_name': 'Stair Climbing Result', 'verbose_name_plural': 'Stair Climbing Results'},
        ),
        migrations.RemoveField(
            model_name='basketballresult',
            name='miliseconds',
        ),
        migrations.RemoveField(
            model_name='colorselectingresult',
            name='miliseconds',
        ),
        migrations.RemoveField(
            model_name='firefighterresult',
            name='miliseconds',
        ),
        migrations.RemoveField(
            model_name='innovativeresult',
            name='miliseconds',
        ),
        migrations.RemoveField(
            model_name='linefollowerresult',
            name='miliseconds',
        ),
        migrations.RemoveField(
            model_name='mazeresult',
            name='miliseconds',
        ),
        migrations.RemoveField(
            model_name='scenarioresult',
            name='miliseconds',
        ),
        migrations.RemoveField(
            model_name='selfbalancingresult',
            name='headway_miliseconds',
        ),
        migrations.RemoveField(
            model_name='selfbalancingresult',
            name='miliseconds',
        ),
        migrations.RemoveField(
            model_name='stairclimbingresult',
            name='miliseconds',
        ),
        migrations.AddField(
            model_name='basketballresult',
            name='milliseconds',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Milliseconds'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='colorselectingresult',
            name='milliseconds',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Milliseconds'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='firefighterresult',
            name='milliseconds',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Milliseconds'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='innovativeresult',
            name='milliseconds',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Milliseconds'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='linefollowerresult',
            name='milliseconds',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Milliseconds'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mazeresult',
            name='milliseconds',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Milliseconds'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scenarioresult',
            name='milliseconds',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Milliseconds'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='selfbalancingresult',
            name='headway_milliseconds',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Headway Milliseconds'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='selfbalancingresult',
            name='milliseconds',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Milliseconds'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stairclimbingresult',
            name='milliseconds',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Milliseconds'),
            preserve_default=False,
        ),
    ]
