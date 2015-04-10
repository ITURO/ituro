# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0003_auto_20150408_2218'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mazeresult',
            options={'ordering': ['disqualification', 'score'], 'verbose_name': 'Maze Result', 'verbose_name_plural': 'Maze Results'},
        ),
    ]
