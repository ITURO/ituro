# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20180207_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimulationStage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.PositiveIntegerField(verbose_name='Stage')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('create_orders', models.BooleanField(default=False)),
                ('remove_orders', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['number'],
                'verbose_name': 'Simulation Stage',
                'verbose_name_plural': 'Simulation Stages',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SimulationStageMatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(verbose_name='Order')),
                ('raund', models.PositiveSmallIntegerField(verbose_name='Raund')),
                ('is_played', models.BooleanField(default=False, verbose_name='Is played?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('cat', models.ForeignKey(related_name='cat', verbose_name='Cat', blank=True, to='projects.Project', null=True)),
                ('rat', models.ForeignKey(related_name='rat', verbose_name='Rat', blank=True, to='projects.Project', null=True)),
                ('stage', models.ForeignKey(verbose_name='Stage', to='simulation.SimulationStage')),
                ('won', models.ForeignKey(related_name='won', verbose_name='Winner', blank=True, to='projects.Project', null=True)),
            ],
            options={
                'ordering': ['order', 'stage__number'],
                'verbose_name': 'Simulation Stage Match',
                'verbose_name_plural': 'Simulation Stage Matches',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SimulationStageMatchResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('minutes', models.PositiveSmallIntegerField(verbose_name='Minutes')),
                ('seconds', models.PositiveSmallIntegerField(verbose_name='Seconds')),
                ('milliseconds', models.PositiveSmallIntegerField(verbose_name='Milliseconds')),
                ('distance', models.PositiveIntegerField(verbose_name='Distance')),
                ('is_caught', models.BooleanField(default=False, verbose_name='Is caught?')),
                ('is_cancelled', models.BooleanField(default=False, verbose_name='Is cancelled?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('match', models.ForeignKey(verbose_name='Match', to='simulation.SimulationStageMatch')),
            ],
            options={
                'ordering': ['is_cancelled', 'is_caught', 'distance'],
                'verbose_name': 'Simulation Stage Match Result',
                'verbose_name_plural': 'Simulation Stage Match Results',
            },
            bases=(models.Model,),
        ),
    ]
