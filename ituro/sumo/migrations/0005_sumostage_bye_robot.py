# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20180220_1921'),
        ('sumo', '0004_auto_20150410_0222'),
    ]

    operations = [
        migrations.AddField(
            model_name='sumostage',
            name='bye_robot',
            field=models.ForeignKey(related_name='bye_robot', to='projects.Project', null=True),
            preserve_default=True,
        ),
    ]
