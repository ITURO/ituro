# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import content_management.models


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('flatpage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='flatpages.FlatPage')),
                ('uid', models.PositiveIntegerField()),
                ('language', models.CharField(max_length=5, choices=[(b'tr', 'Turkish'), (b'en', 'English')])),
                ('page_type', models.CharField(blank=True, max_length=10, null=True, choices=[(b'about', 'About'), (b'sponsorship', 'Sponsorship')])),
                ('order', models.PositiveIntegerField()),
                ('is_public', models.BooleanField(default=False)),
                ('is_right', models.BooleanField(default=False)),
                ('is_divided', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('flatpages.flatpage',),
        ),
        migrations.CreateModel(
            name='CategoryPage',
            fields=[
                ('flatpage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='flatpages.FlatPage')),
                ('uid', models.PositiveIntegerField()),
                ('language', models.CharField(max_length=5, choices=[(b'tr', 'Turkish'), (b'en', 'English')])),
                ('page_type', models.CharField(blank=True, max_length=10, null=True, choices=[(b'about', 'About'), (b'sponsorship', 'Sponsorship')])),
                ('order', models.PositiveIntegerField()),
                ('is_public', models.BooleanField(default=False)),
                ('is_right', models.BooleanField(default=False)),
                ('is_divided', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('document', models.FileField(upload_to=content_management.models.get_document_upload_path)),
                ('video_url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
            bases=('flatpages.flatpage',),
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=5, choices=[(b'tr', 'Turkish'), (b'en', 'English')])),
                ('uid', models.PositiveIntegerField()),
                ('order', models.PositiveIntegerField()),
                ('is_public', models.BooleanField(default=False)),
                ('slug', models.SlugField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('flatpage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='flatpages.FlatPage')),
                ('uid', models.PositiveIntegerField()),
                ('language', models.CharField(max_length=5, choices=[(b'tr', 'Turkish'), (b'en', 'English')])),
                ('page_type', models.CharField(blank=True, max_length=10, null=True, choices=[(b'about', 'About'), (b'sponsorship', 'Sponsorship')])),
                ('order', models.PositiveIntegerField()),
                ('is_public', models.BooleanField(default=False)),
                ('is_right', models.BooleanField(default=False)),
                ('is_divided', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('video_url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
            bases=('flatpages.flatpage',),
        ),
        migrations.CreateModel(
            name='NewsPage',
            fields=[
                ('flatpage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='flatpages.FlatPage')),
                ('uid', models.PositiveIntegerField()),
                ('language', models.CharField(max_length=5, choices=[(b'tr', 'Turkish'), (b'en', 'English')])),
                ('page_type', models.CharField(blank=True, max_length=10, null=True, choices=[(b'about', 'About'), (b'sponsorship', 'Sponsorship')])),
                ('order', models.PositiveIntegerField()),
                ('is_public', models.BooleanField(default=False)),
                ('is_right', models.BooleanField(default=False)),
                ('is_divided', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('short_description', models.CharField(max_length=100)),
                ('types', models.CharField(max_length=50, choices=[(b'danger', 'Hot!'), (b'info', 'Information'), (b'primary', 'Important')])),
            ],
            options={
                'abstract': False,
            },
            bases=('flatpages.flatpage',),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=content_management.models.get_image_upload_path)),
                ('thumbnail', models.ImageField(upload_to=content_management.models.get_thumbnail_upload_path)),
                ('slug', models.SlugField(max_length=100)),
                ('is_important', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SponsorshipPage',
            fields=[
                ('flatpage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='flatpages.FlatPage')),
                ('uid', models.PositiveIntegerField()),
                ('language', models.CharField(max_length=5, choices=[(b'tr', 'Turkish'), (b'en', 'English')])),
                ('page_type', models.CharField(blank=True, max_length=10, null=True, choices=[(b'about', 'About'), (b'sponsorship', 'Sponsorship')])),
                ('order', models.PositiveIntegerField()),
                ('is_public', models.BooleanField(default=False)),
                ('is_right', models.BooleanField(default=False)),
                ('is_divided', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('flatpages.flatpage',),
        ),
        migrations.AddField(
            model_name='newspage',
            name='image',
            field=models.ForeignKey(to='content_management.Photo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallery',
            name='photos',
            field=models.ManyToManyField(to='content_management.Photo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='categorypage',
            name='gallery',
            field=models.ForeignKey(to='content_management.Gallery'),
            preserve_default=True,
        ),
    ]
