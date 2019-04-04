# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20190404_1646'),
        ('results', '0015_auto_20180207_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineFootballResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.FloatField(verbose_name='Score', blank=True)),
                ('minutes', models.PositiveSmallIntegerField(verbose_name='Minutes')),
                ('seconds', models.PositiveSmallIntegerField(verbose_name='Seconds')),
                ('milliseconds', models.PositiveSmallIntegerField(verbose_name='Milliseconds')),
                ('dribble_minutes', models.PositiveSmallIntegerField(verbose_name='Dribble Minutes')),
                ('dribble_seconds', models.PositiveSmallIntegerField(verbose_name='Dribble Seconds')),
                ('dribble_milliseconds', models.PositiveSmallIntegerField(verbose_name='Dribble Milliseconds')),
                ('fails', models.PositiveSmallIntegerField(default=0, verbose_name='Fails')),
                ('goals', models.PositiveSmallIntegerField(default=0, verbose_name='Goals')),
                ('disqualification', models.BooleanField(default=False, verbose_name='Disqualification')),
                ('is_best', models.BooleanField(default=True, verbose_name='Is best result?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(to='projects.Project')),
            ],
            options={
                'ordering': ['disqualification', 'score'],
                'verbose_name': 'Line Football Result',
                'verbose_name_plural': 'Line Football Results',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MazeResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.FloatField(verbose_name='Score', blank=True)),
                ('minutes', models.PositiveSmallIntegerField(verbose_name='Minutes')),
                ('seconds', models.PositiveSmallIntegerField(verbose_name='Seconds')),
                ('milliseconds', models.PositiveSmallIntegerField(verbose_name='Milliseconds')),
                ('disqualification', models.BooleanField(default=False, verbose_name='Disqualification')),
                ('is_best', models.BooleanField(default=True, verbose_name='Is best result?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(to='projects.Project')),
            ],
            options={
                'ordering': ['disqualification', 'score'],
                'verbose_name': 'Maze Result',
                'verbose_name_plural': 'Maze Results',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TrafficResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.FloatField(verbose_name='Score', blank=True)),
                ('minutes', models.PositiveSmallIntegerField(verbose_name='Minutes')),
                ('seconds', models.PositiveSmallIntegerField(verbose_name='Seconds')),
                ('milliseconds', models.PositiveSmallIntegerField(verbose_name='Milliseconds')),
                ('disqualification', models.BooleanField(default=False, verbose_name='Disqualification')),
                ('is_best', models.BooleanField(default=True, verbose_name='Is best result?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_stopped', models.BooleanField(default=False, verbose_name='Is stopped?')),
                ('is_parked', models.BooleanField(default=False, verbose_name='Is parked?')),
                ('sign_succeed', models.PositiveSmallIntegerField(default=0, verbose_name='Succeed Signs')),
                ('sign_failed', models.PositiveSmallIntegerField(default=0, verbose_name='Failed Signs')),
                ('project', models.ForeignKey(to='projects.Project')),
            ],
            options={
                'ordering': ['disqualification', '-score', 'minutes', 'seconds', 'milliseconds'],
                'verbose_name': 'Traffic Result',
                'verbose_name_plural': 'Traffic Results',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='linefollowerresult',
            name='project',
        ),
        migrations.RemoveField(
            model_name='linefollowerresult',
            name='stage',
        ),
        migrations.DeleteModel(
            name='LineFollowerResult',
        ),
        migrations.RemoveField(
            model_name='scenarioresult',
            name='is_parked',
        ),
        migrations.RemoveField(
            model_name='scenarioresult',
            name='is_stopped',
        ),
        migrations.RemoveField(
            model_name='scenarioresult',
            name='sign_failed',
        ),
        migrations.RemoveField(
            model_name='scenarioresult',
            name='sign_succeed',
        ),
        migrations.AddField(
            model_name='scenarioresult',
            name='fails',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Fails'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scenarioresult',
            name='place_success',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Successful Block Placements'),
            preserve_default=True,
        ),
    ]
