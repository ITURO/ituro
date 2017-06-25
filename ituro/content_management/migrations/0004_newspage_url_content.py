# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content_management', '0003_auto_20170624_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspage',
            name='url_content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
