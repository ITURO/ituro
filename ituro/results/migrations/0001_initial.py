# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20150401_2057'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorSelectingResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(verbose_name='Score', blank=True)),
                ('minutes', models.PositiveSmallIntegerField(verbose_name='Minutes')),
                ('seconds', models.PositiveSmallIntegerField(verbose_name='Seconds')),
                ('miliseconds', models.PositiveSmallIntegerField(verbose_name='Miliseconds')),
                ('is_attended', models.BooleanField(default=False, verbose_name='Is attended the race?')),
                ('order', models.IntegerField(verbose_name='Race Order')),
                ('disqualification', models.BooleanField(default=False, verbose_name='Disqualification')),
                ('is_best', models.BooleanField(default=True, verbose_name='Is best result?')),
                ('obtain', models.PositiveSmallIntegerField(verbose_name='Cylinder Obtain Count')),
                ('place_success', models.PositiveSmallIntegerField(verbose_name='Cylinder Successful Placement Count')),
                ('place_failure', models.PositiveSmallIntegerField(verbose_name='Cylinder Unsuccessful Placement Count')),
                ('place_partial', models.PositiveSmallIntegerField(verbose_name='Cylinder Partial Placement Count')),
                ('project', models.ForeignKey(to='projects.Project')),
            ],
            options={
                'ordering': ['-score', 'minutes', 'seconds', 'miliseconds'],
                'verbose_name': 'Color Selecting Result',
                'verbose_name_plural': 'Color Selecting Results',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FireFighterResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(verbose_name='Score', blank=True)),
                ('minutes', models.PositiveSmallIntegerField(verbose_name='Minutes')),
                ('seconds', models.PositiveSmallIntegerField(verbose_name='Seconds')),
                ('miliseconds', models.PositiveSmallIntegerField(verbose_name='Miliseconds')),
                ('is_attended', models.BooleanField(default=False, verbose_name='Is attended the race?')),
                ('order', models.IntegerField(verbose_name='Race Order')),
                ('disqualification', models.BooleanField(default=False, verbose_name='Disqualification')),
                ('is_best', models.BooleanField(default=True, verbose_name='Is best result?')),
                ('extinguish_success', models.PositiveSmallIntegerField(verbose_name='Succesful Extinguish Count')),
                ('extinguish_failure', models.PositiveSmallIntegerField(verbose_name='Unsuccessful Extinguish Count')),
                ('project', models.ForeignKey(to='projects.Project')),
            ],
            options={
                'ordering': ['-score', 'minutes', 'seconds', 'miliseconds'],
                'verbose_name': 'Fire Fighter Result',
                'verbose_name_plural': 'Fire Fighter Results',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LineFollowerResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(verbose_name='Score', blank=True)),
                ('minutes', models.PositiveSmallIntegerField(verbose_name='Minutes')),
                ('seconds', models.PositiveSmallIntegerField(verbose_name='Seconds')),
                ('miliseconds', models.PositiveSmallIntegerField(verbose_name='Miliseconds')),
                ('is_attended', models.BooleanField(default=False, verbose_name='Is attended the race?')),
                ('order', models.IntegerField(verbose_name='Race Order')),
                ('disqualification', models.BooleanField(default=False, verbose_name='Disqualification')),
                ('is_best', models.BooleanField(default=True, verbose_name='Is best result?')),
                ('runway_out', models.PositiveSmallIntegerField(verbose_name='Runway Out Count')),
                ('project', models.ForeignKey(to='projects.Project')),
                ('stage', models.ForeignKey(verbose_name='Line Follower Stage', to='orders.LineFollowerStage')),
            ],
            options={
                'ordering': ['score'],
                'verbose_name': 'Line Follower Result',
                'verbose_name_plural': 'Line Follower Results',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MazeResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(verbose_name='Score', blank=True)),
                ('minutes', models.PositiveSmallIntegerField(verbose_name='Minutes')),
                ('seconds', models.PositiveSmallIntegerField(verbose_name='Seconds')),
                ('miliseconds', models.PositiveSmallIntegerField(verbose_name='Miliseconds')),
                ('is_attended', models.BooleanField(default=False, verbose_name='Is attended the race?')),
                ('order', models.IntegerField(verbose_name='Race Order')),
                ('disqualification', models.BooleanField(default=False, verbose_name='Disqualification')),
                ('is_best', models.BooleanField(default=True, verbose_name='Is best result?')),
                ('project', models.ForeignKey(to='projects.Project')),
            ],
            options={
                'ordering': ['minutes', 'seconds', 'miliseconds'],
                'verbose_name': 'Maze Result',
                'verbose_name_plural': 'Maze Results',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SelfBalancingResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(verbose_name='Score', blank=True)),
                ('minutes', models.PositiveSmallIntegerField(verbose_name='Minutes')),
                ('seconds', models.PositiveSmallIntegerField(verbose_name='Seconds')),
                ('miliseconds', models.PositiveSmallIntegerField(verbose_name='Miliseconds')),
                ('is_attended', models.BooleanField(default=False, verbose_name='Is attended the race?')),
                ('order', models.IntegerField(verbose_name='Race Order')),
                ('disqualification', models.BooleanField(default=False, verbose_name='Disqualification')),
                ('is_best', models.BooleanField(default=True, verbose_name='Is best result?')),
                ('headway_amount', models.PositiveSmallIntegerField(verbose_name='Headway Amount (cm)')),
                ('impact', models.BooleanField(default=False, verbose_name='Impact Test')),
                ('headway_minutes', models.PositiveSmallIntegerField(verbose_name='Headway Minutes')),
                ('headway_seconds', models.PositiveSmallIntegerField(verbose_name='Headway Seconds')),
                ('headway_miliseconds', models.PositiveSmallIntegerField(verbose_name='Headway Miliseconds')),
                ('project', models.ForeignKey(to='projects.Project')),
            ],
            options={
                'ordering': ['-score', '-seconds', '-miliseconds', '-headway_amount', 'headway_minutes', 'headway_seconds', 'headway_miliseconds'],
                'verbose_name': 'Self Balancing Result',
                'verbose_name_plural': 'Self Balancing Results',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StairClimbing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(verbose_name='Score', blank=True)),
                ('minutes', models.PositiveSmallIntegerField(verbose_name='Minutes')),
                ('seconds', models.PositiveSmallIntegerField(verbose_name='Seconds')),
                ('miliseconds', models.PositiveSmallIntegerField(verbose_name='Miliseconds')),
                ('is_attended', models.BooleanField(default=False, verbose_name='Is attended the race?')),
                ('order', models.IntegerField(verbose_name='Race Order')),
                ('disqualification', models.BooleanField(default=False, verbose_name='Disqualification')),
                ('is_best', models.BooleanField(default=True, verbose_name='Is best result?')),
                ('stair1', models.BooleanField(default=False, verbose_name='Stair #1')),
                ('stair2', models.BooleanField(default=False, verbose_name='Stair #2')),
                ('stair3', models.BooleanField(default=False, verbose_name='Stair #3')),
                ('stair4', models.BooleanField(default=False, verbose_name='Stair #4')),
                ('downstairs', models.PositiveSmallIntegerField(verbose_name='Downstairs Count')),
                ('project', models.ForeignKey(to='projects.Project')),
            ],
            options={
                'ordering': ['-score', 'minutes', 'seconds', 'miliseconds'],
                'verbose_name': 'Stair Climbing Result',
                'verbose_name_plural': 'Stair Climbing Results',
            },
            bases=(models.Model,),
        ),
    ]
