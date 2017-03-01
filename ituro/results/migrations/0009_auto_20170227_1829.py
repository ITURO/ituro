# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0008_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenarioresult',
            name='is_finished',
            field=models.BooleanField(default=False, verbose_name='Finished?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scenarioresult',
            name='is_parked',
            field=models.BooleanField(default=False, verbose_name='Parked?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scenarioresult',
            name='sign_failed',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Failed Signes'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scenarioresult',
            name='sign_successed',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Successed Signes'),
            preserve_default=True,
        ),
    ]
