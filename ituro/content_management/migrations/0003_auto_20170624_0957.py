# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content_management', '0002_auto_20170624_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutpage',
            name='page_type',
        ),
        migrations.RemoveField(
            model_name='categorypage',
            name='page_type',
        ),
        migrations.RemoveField(
            model_name='commonpage',
            name='page_type',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='page_type',
        ),
        migrations.RemoveField(
            model_name='newspage',
            name='page_type',
        ),
        migrations.RemoveField(
            model_name='sponsorshippage',
            name='page_type',
        ),
    ]
