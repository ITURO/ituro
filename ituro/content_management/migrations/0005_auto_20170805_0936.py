# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content_management', '0004_newspage_url_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='language',
            field=models.CharField(max_length=5, choices=[(b'en', 'English'), (b'tr', 'Turkish')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='categorypage',
            name='language',
            field=models.CharField(max_length=5, choices=[(b'en', 'English'), (b'tr', 'Turkish')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='commonpage',
            name='language',
            field=models.CharField(max_length=5, choices=[(b'en', 'English'), (b'tr', 'Turkish')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gallery',
            name='language',
            field=models.CharField(max_length=5, choices=[(b'en', 'English'), (b'tr', 'Turkish')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='homepage',
            name='language',
            field=models.CharField(max_length=5, choices=[(b'en', 'English'), (b'tr', 'Turkish')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newspage',
            name='language',
            field=models.CharField(max_length=5, choices=[(b'en', 'English'), (b'tr', 'Turkish')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sponsorshippage',
            name='language',
            field=models.CharField(max_length=5, choices=[(b'en', 'English'), (b'tr', 'Turkish')]),
            preserve_default=True,
        ),
    ]
