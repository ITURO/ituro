# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sumo', '0002_auto_20150409_0841'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sumogroupmatch',
            options={'ordering': ['group__order', 'order'], 'verbose_name': 'Sumo Group Match', 'verbose_name_plural': 'Sumo Group Matches'},
        ),
        migrations.AlterModelOptions(
            name='sumogroupteam',
            options={'ordering': ['-point', '-average', 'order'], 'verbose_name': 'Sumo Group Team', 'verbose_name_plural': 'Sumo Group Teams'},
        ),
        migrations.AddField(
            model_name='sumogroupteam',
            name='is_attended',
            field=models.BooleanField(default=True, verbose_name='Is attended?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sumogroupmatch',
            name='away_score',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Away Score'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sumogroupmatch',
            name='home_score',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Home Score'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sumostagematch',
            name='away_score',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Away Score'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sumostagematch',
            name='home_score',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Home Score'),
            preserve_default=True,
        ),
    ]
