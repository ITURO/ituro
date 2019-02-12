# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0011_auto_20170301_1304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scenarioresult',
            options={'ordering': ['disqualification', '-score', 'minutes', 'seconds', 'milliseconds'], 'verbose_name': 'Scenario Result', 'verbose_name_plural': 'Scenario Results'},
        ),
        migrations.AlterModelOptions(
            name='selfbalancingresult',
            options={'ordering': ['disqualification', '-score', '-headway_amount'], 'verbose_name': 'Self Balancing Result', 'verbose_name_plural': 'Self Balancing Results'},
        ),
        migrations.RemoveField(
            model_name='scenarioresult',
            name='is_finished',
        ),
        migrations.RemoveField(
            model_name='scenarioresult',
            name='sign_failed',
        ),
        migrations.RemoveField(
            model_name='selfbalancingresult',
            name='stage3_milliseconds',
        ),
        migrations.RemoveField(
            model_name='selfbalancingresult',
            name='stage3_minutes',
        ),
        migrations.RemoveField(
            model_name='selfbalancingresult',
            name='stage3_seconds',
        ),
        migrations.AddField(
            model_name='scenarioresult',
            name='is_stopped',
            field=models.BooleanField(default=False, verbose_name='Is stopped?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stairclimbingresult',
            name='plexi_touch',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Plexi Touch Count'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='basketballresult',
            name='basket4',
            field=models.PositiveSmallIntegerField(verbose_name='Moving Basket 1'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='basketballresult',
            name='basket5',
            field=models.PositiveSmallIntegerField(verbose_name='Moving Basket 2'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scenarioresult',
            name='is_parked',
            field=models.BooleanField(default=False, verbose_name='Is parked?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='selfbalancingresult',
            name='headway_amount',
            field=models.PositiveSmallIntegerField(verbose_name='Headway Amount (mm)'),
            preserve_default=True,
        ),
    ]
