# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_auto_20150408_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='basketballresult',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 8, 22, 17, 34, 513981, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='colorselectingresult',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 8, 22, 17, 44, 865760, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='firefighterresult',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 8, 22, 17, 47, 943957, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='innovativeresult',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 8, 22, 17, 51, 97336, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='linefollowerresult',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 8, 22, 17, 54, 484920, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mazeresult',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 8, 22, 17, 58, 919759, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scenarioresult',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 8, 22, 18, 2, 414045, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='selfbalancingresult',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 8, 22, 18, 6, 209239, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stairclimbingresult',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 8, 22, 18, 10, 268990, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
