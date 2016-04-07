# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_remove_project_design'),
        ('results', '0005_auto_20150411_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='InnovativeJury',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jury', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InnovativeJuryResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('design', models.PositiveSmallIntegerField(default=0, verbose_name='Design')),
                ('innovative', models.PositiveSmallIntegerField(default=0, verbose_name='Innovative')),
                ('technical', models.PositiveSmallIntegerField(default=0, verbose_name='Technical')),
                ('presentation', models.PositiveSmallIntegerField(default=0, verbose_name='Presentation')),
                ('opinion', models.PositiveSmallIntegerField(default=0, verbose_name='Opinion')),
                ('jury', models.ForeignKey(to='results.InnovativeJury')),
                ('project', models.ForeignKey(to='projects.Project')),
            ],
            options={
                'verbose_name': 'Innovative Result',
                'verbose_name_plural': 'Innovative Results',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='innovativeresult',
            name='project',
        ),
        migrations.DeleteModel(
            name='InnovativeResult',
        ),
    ]
