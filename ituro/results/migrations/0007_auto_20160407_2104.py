# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_remove_project_design'),
        ('results', '0006_auto_20160402_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='InnovativeTotalResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.FloatField(default=0, verbose_name='Score')),
                ('project', models.ForeignKey(to='projects.Project', unique=True)),
            ],
            options={
                'ordering': ['project'],
                'verbose_name': 'Innovative Total Result',
                'verbose_name_plural': 'Innovative Total Results',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='innovativejury',
            options={'ordering': ['jury'], 'verbose_name': 'Innovative Jury', 'verbose_name_plural': 'Innovative Juries'},
        ),
        migrations.AlterModelOptions(
            name='innovativejuryresult',
            options={'ordering': ['project', 'jury'], 'verbose_name': 'Innovative Result', 'verbose_name_plural': 'Innovative Results'},
        ),
        migrations.AddField(
            model_name='innovativejuryresult',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 7, 21, 4, 17, 324949, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='innovativejuryresult',
            name='jury_score',
            field=models.FloatField(default=0, verbose_name='Jury Score', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='innovativejury',
            name='jury',
            field=models.CharField(unique=True, max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='innovativejuryresult',
            name='design',
            field=models.FloatField(default=0, verbose_name='Design', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='innovativejuryresult',
            name='innovative',
            field=models.FloatField(default=0, verbose_name='Innovative', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='innovativejuryresult',
            name='opinion',
            field=models.FloatField(default=0, verbose_name='Opinion', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='innovativejuryresult',
            name='presentation',
            field=models.FloatField(default=0, verbose_name='Presentation', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='innovativejuryresult',
            name='technical',
            field=models.FloatField(default=0, verbose_name='Technical', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)]),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='innovativejuryresult',
            unique_together=set([('project', 'jury')]),
        ),
    ]
