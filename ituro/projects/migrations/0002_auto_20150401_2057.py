# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='is_valid',
        ),
        migrations.AddField(
            model_name='project',
            name='is_confirmed',
            field=models.BooleanField(default=False, verbose_name='Is project confirmed?'),
            preserve_default=True,
        ),
    ]
