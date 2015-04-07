# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20150401_2057'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineFollowerRaceOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveSmallIntegerField(verbose_name='Race Order')),
                ('project', models.ForeignKey(verbose_name='Project', to='projects.Project')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': 'Line Follower Race Order',
                'verbose_name_plural': 'Line Follower Race Orders',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LineFollowerStage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveSmallIntegerField(verbose_name='Stage Order')),
                ('is_current', models.BooleanField(default=False, verbose_name='Is current stage?')),
                ('is_final', models.BooleanField(default=False, verbose_name='Is final stage?')),
                ('orders_available', models.BooleanField(default=False, verbose_name='Race Orders Availability')),
                ('results_available', models.BooleanField(default=False, verbose_name='Race Results Availability')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': 'Line Follower Stage',
                'verbose_name_plural': 'Line Follower Stages',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RaceOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveSmallIntegerField(verbose_name='Race Order')),
                ('project', models.OneToOneField(verbose_name='Project', to='projects.Project')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': 'Race Order',
                'verbose_name_plural': 'Race Orders',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='linefollowerraceorder',
            name='stage',
            field=models.ForeignKey(verbose_name='Line Follower Stage', to='orders.LineFollowerStage'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='linefollowerraceorder',
            unique_together=set([('project', 'stage')]),
        ),
    ]
