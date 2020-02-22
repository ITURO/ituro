# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0018_innovativejuryresult_commercialization_potential'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mazeresult',
            name='project',
        ),
        migrations.DeleteModel(
            name='MazeResult',
        ),
    ]
