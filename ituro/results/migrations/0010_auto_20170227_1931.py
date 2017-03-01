# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0009_auto_20170227_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scenarioresult',
            name='is_finished',
            field=models.BooleanField(default=False, verbose_name='Is finish?'),
            preserve_default=True,
        ),
    ]
