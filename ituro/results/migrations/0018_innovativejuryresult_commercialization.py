# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0017_linefootballresult_successful_ball_throws'),
    ]

    operations = [
        migrations.AddField(
            model_name='innovativejuryresult',
            name='commercialization',
            field=models.FloatField(default=0, verbose_name='Commercialization', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)]),
            preserve_default=True,
        ),
    ]
