# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='phone', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='school',
            field=models.CharField(max_length=50, verbose_name='school', blank=True),
            preserve_default=True,
        ),
    ]
