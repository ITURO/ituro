# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20170227_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(max_length=30, verbose_name='Category', choices=[(b'line_follower', 'Line Follower'), (b'line_follower_junior', 'Line Follower Junior'), (b'micro_sumo', 'Micro Sumo'), (b'fire_fighter', 'Fire Fighter'), (b'basketball', 'Basketball'), (b'stair_climbing', 'Stair Climbing'), (b'maze', 'Maze'), (b'color_selecting', 'Color Selecting'), (b'self_balancing', 'Self Balancing'), (b'scenario', 'Scenario'), (b'innovative', 'Innovative')]),
            preserve_default=True,
        ),
    ]
