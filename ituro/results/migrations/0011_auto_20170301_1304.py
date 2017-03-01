# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20170301_1304'),
        ('results', '0010_auto_20170301_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConstructionResult',
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
                'ordering': ['disqualification', '-score', 'minutes', 'seconds', 'milliseconds'],
                'verbose_name': 'Construction Result',
                'verbose_name_plural': 'Construction Results',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='firefighterresult',
            name='project',
        ),
        migrations.DeleteModel(
            name='FireFighterResult',
        ),
    ]
