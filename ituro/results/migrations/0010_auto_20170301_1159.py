# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0009_linefollowerjuniorresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenarioresult',
            name='is_finished',
            field=models.BooleanField(default=False, verbose_name='Is finish?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scenarioresult',
            name='is_parked',
            field=models.BooleanField(default=False, verbose_name='Is Parked?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scenarioresult',
            name='sign_failed',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Failed Signs'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scenarioresult',
            name='sign_succeed',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Succeed Signs'),
            preserve_default=True,
        ),
    ]
