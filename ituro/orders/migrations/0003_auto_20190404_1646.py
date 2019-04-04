# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0016_auto_20190404_1646'),
        ('orders', '0002_auto_20170223_1628'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='linefollowerraceorder',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='linefollowerraceorder',
            name='project',
        ),
        migrations.RemoveField(
            model_name='linefollowerraceorder',
            name='stage',
        ),
        migrations.DeleteModel(
            name='LineFollowerRaceOrder',
        ),
        migrations.DeleteModel(
            name='LineFollowerStage',
        ),
    ]
