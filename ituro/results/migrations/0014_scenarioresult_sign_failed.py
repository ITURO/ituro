# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0013_auto_20170404_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenarioresult',
            name='sign_failed',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Failed Signs'),
            preserve_default=True,
        ),
    ]
