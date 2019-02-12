# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20170301_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(max_length=30, verbose_name='Category', choices=[(b'line_follower', 'Line Follower'), (b'line_follower_junior', 'Line Follower Junior'), (b'micro_sumo', 'Micro Sumo'), (b'construction', 'Construction'), (b'drone', 'Drone'), (b'stair_climbing', 'Stair Climbing'), (b'color_selecting', 'Color Selecting'), (b'scenario', 'Scenario'), (b'innovative', 'Innovative')]),
            preserve_default=True,
        ),
    ]
