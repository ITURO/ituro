# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0001_initial'),
        ('content_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonPage',
            fields=[
                ('flatpage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='flatpages.FlatPage')),
                ('uid', models.PositiveIntegerField()),
                ('language', models.CharField(max_length=5, choices=[(b'tr', 'Turkish'), (b'en', 'English')])),
                ('page_type', models.CharField(blank=True, max_length=10, null=True, choices=[(b'about', 'About'), (b'sponsorship', 'Sponsorship')])),
                ('order', models.PositiveIntegerField()),
                ('is_public', models.BooleanField(default=False)),
                ('is_divided', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('flatpages.flatpage',),
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='is_right',
        ),
        migrations.RemoveField(
            model_name='categorypage',
            name='is_right',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='is_right',
        ),
        migrations.RemoveField(
            model_name='newspage',
            name='is_right',
        ),
        migrations.RemoveField(
            model_name='sponsorshippage',
            name='is_right',
        ),
    ]
