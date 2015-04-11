# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0004_auto_20150410_0223'),
    ]

    operations = [
        migrations.AddField(
            model_name='innovativeresult',
            name='design',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Design'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='innovativeresult',
            name='digital_design',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Digital Design'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='innovativeresult',
            name='innovative',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Innovative'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='innovativeresult',
            name='opinion',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Opinion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='innovativeresult',
            name='presentation',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Presentation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='innovativeresult',
            name='technical',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Technical'),
            preserve_default=True,
        ),
    ]
