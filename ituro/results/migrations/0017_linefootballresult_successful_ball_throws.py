# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0016_auto_20190404_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='linefootballresult',
            name='successful_ball_throws',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Successful Ball Throws'),
            preserve_default=True,
        ),
    ]
