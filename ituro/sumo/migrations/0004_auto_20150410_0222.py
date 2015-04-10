# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sumo', '0003_auto_20150409_2006'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sumostage',
            options={'ordering': ['order'], 'verbose_name': 'Sumo Stage', 'verbose_name_plural': 'Sumo Stages'},
        ),
    ]
