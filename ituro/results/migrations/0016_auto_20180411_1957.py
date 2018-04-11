# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0015_auto_20180207_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scenarioresult',
            name='is_stopped',
            field=models.BooleanField(default=False, verbose_name='Is parked wrongly?'),
            preserve_default=True,
        ),
    ]
