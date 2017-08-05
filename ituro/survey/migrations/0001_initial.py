# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ChoiceQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=250)),
                ('is_multiple', models.BooleanField(default=False)),
                ('order', models.PositiveIntegerField(null=True, blank=True)),
                ('answers', models.ManyToManyField(related_name='answer_list', to='survey.Choice', blank=True)),
                ('choices', models.ManyToManyField(related_name='choice_list', to='survey.Choice', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100, null=True, blank=True)),
                ('language', models.CharField(max_length=5, choices=[(b'en', 'English'), (b'tr', 'Turkish')])),
                ('uid', models.PositiveIntegerField(null=True, blank=True)),
                ('participant', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_draft', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextAreaQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=250, null=True, blank=True)),
                ('answer', models.TextField(null=True, blank=True)),
                ('order', models.PositiveIntegerField(null=True, blank=True)),
                ('survey', models.ForeignKey(to='survey.Survey')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=250)),
                ('answer', models.CharField(max_length=200, null=True, blank=True)),
                ('order', models.PositiveIntegerField(null=True, blank=True)),
                ('survey', models.ForeignKey(to='survey.Survey')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='choicequestion',
            name='survey',
            field=models.ForeignKey(to='survey.Survey'),
            preserve_default=True,
        ),
    ]
