# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20170223_1628'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineFollowerJuniorRaceOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveSmallIntegerField(verbose_name='Race Order')),
                ('project', models.ForeignKey(verbose_name='Project', to='projects.Project')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': 'Line Follower Junior Race Order',
                'verbose_name_plural': 'Line Follower Junior Race Orders',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LineFollowerJuniorStage',
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
                'verbose_name': 'Line Follower Junior Stage',
                'verbose_name_plural': 'Line Follower Junior Stages',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='linefollowerjuniorraceorder',
            name='stage',
            field=models.ForeignKey(verbose_name='Line Follower Junior Stage', to='orders.LineFollowerJuniorStage'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='linefollowerjuniorraceorder',
            unique_together=set([('project', 'stage')]),
        ),
    ]
