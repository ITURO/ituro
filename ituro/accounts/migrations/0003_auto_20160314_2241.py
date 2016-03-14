# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150410_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='name',
            field=models.CharField(max_length=60, verbose_name='full name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='phone'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='school',
            field=models.CharField(max_length=50, verbose_name='school'),
            preserve_default=True,
        ),
    ]
