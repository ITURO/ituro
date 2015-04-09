# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20150401_2057'),
    ]

    operations = [
        migrations.CreateModel(
            name='SumoGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveSmallIntegerField(verbose_name='Order')),
                ('is_final', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': 'Sumo Group',
                'verbose_name_plural': 'Sumo Groups',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SumoGroupMatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_played', models.BooleanField(default=False, verbose_name='Game played?')),
                ('home_score', models.PositiveSmallIntegerField(verbose_name='Home Score')),
                ('away_score', models.PositiveSmallIntegerField(verbose_name='Away Score')),
                ('away', models.ForeignKey(related_name='group_away', to='projects.Project', null=True)),
                ('group', models.ForeignKey(verbose_name='Sumo Group', to='sumo.SumoGroup')),
                ('home', models.ForeignKey(related_name='group_home', to='projects.Project')),
            ],
            options={
                'ordering': ['group__order'],
                'verbose_name': 'Sumo Group Match',
                'verbose_name_plural': 'Sumo Group Matches',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SumoGroupTeam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('point', models.PositiveSmallIntegerField(verbose_name='Point')),
                ('order', models.PositiveSmallIntegerField(verbose_name='Order')),
                ('average', models.IntegerField(verbose_name='Average')),
                ('group', models.ForeignKey(verbose_name='Sumo Group', to='sumo.SumoGroup')),
                ('robot', models.ForeignKey(verbose_name='Sumo Robot', to='projects.Project')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': 'Sumo Group Team',
                'verbose_name_plural': 'Sumo Group Teams',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SumoStage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveSmallIntegerField(verbose_name='Order')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SumoStageMatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_played', models.BooleanField(default=False, verbose_name='Game played?')),
                ('home_score', models.PositiveSmallIntegerField(verbose_name='Home Score')),
                ('away_score', models.PositiveSmallIntegerField(verbose_name='Away Score')),
                ('away', models.ForeignKey(related_name='stage_away', to='projects.Project', null=True)),
                ('home', models.ForeignKey(related_name='stage_home', to='projects.Project')),
                ('stage', models.ForeignKey(verbose_name='Sumo Stage', to='sumo.SumoStage')),
            ],
            options={
                'ordering': ['stage__order'],
                'verbose_name': 'Sumo Stage Match',
                'verbose_name_plural': 'Sumo Stage Matches',
            },
            bases=(models.Model,),
        ),
    ]
