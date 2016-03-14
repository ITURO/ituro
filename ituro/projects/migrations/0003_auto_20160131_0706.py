# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0002_auto_20150401_2057'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='membership',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='membership',
            name='member',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='project',
        ),
        migrations.DeleteModel(
            name='Membership',
        ),
        migrations.AddField(
            model_name='project',
            name='manager',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
