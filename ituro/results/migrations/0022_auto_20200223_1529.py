# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0021_remove_stairclimbingresult_plexi_touch'),
    ]

    operations = [
        migrations.AddField(
            model_name='innovativejuryresult',
            name='digital_design',
            field=models.FloatField(default=0, verbose_name='Digital_Design', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trafficresult',
            name='is_stopped',
            field=models.BooleanField(default=False, verbose_name='Is fail parked?'),
            preserve_default=True,
        ),
    ]
