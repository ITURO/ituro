# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0012_auto_20170328_1154'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='selfbalancingresult',
            options={'ordering': ['disqualification', '-score', 'minutes', 'seconds', 'milliseconds', '-headway_amount'], 'verbose_name': 'Self Balancing Result', 'verbose_name_plural': 'Self Balancing Results'},
        ),
        migrations.AddField(
            model_name='selfbalancingresult',
            name='stage2_milliseconds',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Stage2 Milliseconds'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='selfbalancingresult',
            name='stage2_minutes',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Stage2 Minutes'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='selfbalancingresult',
            name='stage2_seconds',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Stage2 Seconds'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='selfbalancingresult',
            name='headway_amount',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Headway Amount (mm)'),
            preserve_default=True,
        ),
    ]
