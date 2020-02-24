# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0020_auto_20200223_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stairclimbingresult',
            name='plexi_touch',
        ),
    ]
