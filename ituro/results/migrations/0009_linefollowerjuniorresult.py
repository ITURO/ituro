# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20170223_1628'),
        ('projects', '0005_auto_20170223_1628'),
        ('results', '0008_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineFollowerJuniorResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.FloatField(verbose_name='Score', blank=True)),
                ('minutes', models.PositiveSmallIntegerField(verbose_name='Minutes')),
                ('seconds', models.PositiveSmallIntegerField(verbose_name='Seconds')),
                ('milliseconds', models.PositiveSmallIntegerField(verbose_name='Milliseconds')),
                ('disqualification', models.BooleanField(default=False, verbose_name='Disqualification')),
                ('is_best', models.BooleanField(default=True, verbose_name='Is best result?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('runway_out', models.PositiveSmallIntegerField(default=0, verbose_name='Runway Out Count')),
                ('project', models.ForeignKey(to='projects.Project')),
                ('stage', models.ForeignKey(verbose_name='Line Follower Junior Stage', to='orders.LineFollowerJuniorStage')),
            ],
            options={
                'ordering': ['disqualification', 'score'],
                'verbose_name': 'Line Follower Junior Result',
                'verbose_name_plural': 'Line Follower Junior Results',
            },
            bases=(models.Model,),
        ),
    ]
