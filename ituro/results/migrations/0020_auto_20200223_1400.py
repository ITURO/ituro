# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0019_auto_20200223_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='constructionresult',
            name='carried_block',
        ),
        migrations.RemoveField(
            model_name='constructionresult',
            name='refere_point',
        ),
    ]
