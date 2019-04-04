# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20180207_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(max_length=30, verbose_name='Category', choices=[(b'line_follower_junior', 'Line Follower Junior'), (b'micro_sumo', 'Micro Sumo'), (b'construction', 'Construction'), (b'drone', 'Drone'), (b'stair_climbing', 'Stair Climbing'), (b'color_selecting', 'Color Selecting'), (b'traffic', 'Traffic'), (b'scenario', 'Scenario'), (b'innovative', 'Innovative'), (b'line_football', 'Line Football'), (b'Maze', 'Labirent')]),
            preserve_default=True,
        ),
    ]
