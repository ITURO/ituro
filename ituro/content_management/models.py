import StringIO
from django.db import models
from django.contrib.flatpages.models import FlatPage
from django.conf import settings
from PIL import Image as Img
from django.dispatch import receiver
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db.models.signals import pre_save, post_save
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible


def get_document_upload_path(instance, filename):
    print instance.title, filename
    return "documents/{}/{}".format(slugify(instance.title), filename)

def get_image_upload_path(instance, filename):
    return "images/photos/{}".format(filename)

def get_thumbnail_upload_path(instance, filename):
    return "images/thumbnails/{}".format(filename)


class CustomPage(FlatPage):
    uid = models.PositiveIntegerField()
    language = models.CharField(max_length=5, choices=settings.LANGUAGES)
    order = models.PositiveIntegerField()
    is_public = models.BooleanField(default=False)
    is_divided = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title


class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=get_image_upload_path)
    thumbnail = models.ImageField(upload_to=get_thumbnail_upload_path)
    slug = models.SlugField(max_length=100)
    is_important = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def preview(self):
        return u'<img src="%s" width="80" height="80"/>' % (self.image.url)

    preview.allow_tags = True
    preview.short_description = "Photo"


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    language = models.CharField(max_length=5, choices=settings.LANGUAGES)
    uid = models.PositiveIntegerField()
    order = models.PositiveIntegerField()
    is_public = models.BooleanField(default=False)
    photos = models.ManyToManyField(Photo)
    slug = models.SlugField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("order",)

    def __unicode__(self):
        return self.title


class CategoryPage(CustomPage):
    document = models.FileField(upload_to=get_document_upload_path)
    video_url = models.URLField()
    gallery = models.ForeignKey(Gallery)


class NewsPage(CustomPage):
    short_description = models.CharField(max_length=100)
    url_content = models.TextField()
    types = models.CharField(max_length=50, choices=settings.NEWS_TYPES)
    image = models.ForeignKey(Photo)


class HomePage(CustomPage):
    video_url = models.URLField()


class SponsorshipPage(CustomPage):
    pass


class AboutPage(CustomPage):
    pass


class CommonPage(CustomPage):
    pass


@receiver(pre_save, sender=Photo)
def photo_resizing(sender, instance, *args, **kwargs):
    photo = Img.open(StringIO.StringIO(instance.image.read()))
    if photo.mode == 'CMYK':
        photo = photo.convert("RGB")
    photo.thumbnail((1080, 1080), Img.ANTIALIAS)
    output = StringIO.StringIO()
    photo.save(output, format='PNG', optimize=True)
    output.seek(0)
    instance.image = InMemoryUploadedFile(output,
                                          'ImageField',
                                          "%s.png"
                                          % instance.image.name.split(".")[0],
                                          'image/png', output.len, None)


@receiver(pre_save, sender=Photo)
def photo_thumbnail_handler(sender, instance, *args, **kwargs):
    photo = Img.open(StringIO.StringIO(instance.image.read()))
    if photo.mode == 'CMYK':
        photo = photo.convert("RGB")
    photo.thumbnail((100, 100), Img.ANTIALIAS)
    output = StringIO.StringIO()
    photo.save(output, format='PNG', optimize=True)
    output.seek(0)
    instance.thumbnail = InMemoryUploadedFile(
        output,
        'ImageField',
        "%s.png"
        % instance.image.name.split(".")[0],
        'image/png', output.len, None
        )


@receiver(pre_save, sender=Gallery)
def gallery_slug_handler(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)


@receiver(pre_save, sender=Photo)
def Photo_slug_handler(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)
