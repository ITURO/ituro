# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20180207_1426'),
        ('results', '0014_scenarioresult_sign_failed'),
    ]

    operations = [
        migrations.CreateModel(
            name='DroneResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.FloatField(verbose_name='Score', blank=True)),
                ('disqualification', models.BooleanField(default=False, verbose_name='Disqualification')),
                ('is_best', models.BooleanField(default=True, verbose_name='Is best result?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('laps', models.FloatField(default=0, verbose_name='Laps')),
                ('shortcuts', models.PositiveSmallIntegerField(default=0, verbose_name='Shortcuts')),
                ('project', models.ForeignKey(to='projects.Project')),
            ],
            options={
                'ordering': ['disqualification', '-score'],
                'verbose_name': 'Drone Result',
                'verbose_name_plural': 'Drone Results',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='basketballresult',
            name='project',
        ),
        migrations.DeleteModel(
            name='BasketballResult',
        ),
        migrations.RemoveField(
            model_name='mazeresult',
            name='project',
        ),
        migrations.DeleteModel(
            name='MazeResult',
        ),
        migrations.RemoveField(
            model_name='selfbalancingresult',
            name='project',
        ),
        migrations.DeleteModel(
            name='SelfBalancingResult',
        ),
    ]
