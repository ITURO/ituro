from django.db import models
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Survey(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(choices=settings.LANGUAGES, max_length=5)
    uid = models.PositiveIntegerField(blank=True, null=True)
    participant = models.CharField(_("Name"), max_length=100)
    slug = models.SlugField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_draft = models.BooleanField(default=False)

    def __unicode__(self):
        return self.participant + "-" + self.title


class TextQuestion(models.Model):
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=200, blank=True, null=True)
    survey = models.ForeignKey(Survey)
    order = models.PositiveIntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.question


class TextAreaQuestion(models.Model):
    question = models.CharField(max_length=250, blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    survey = models.ForeignKey(Survey)
    order = models.PositiveIntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.question


class Choice(models.Model):
    answer = models.CharField(max_length=100)

    def __unicode__(self):
        return self.answer


class ChoiceQuestion(models.Model):
    question = models.CharField(max_length=250)
    is_multiple = models.BooleanField(default=False)
    choices = models.ManyToManyField(Choice, blank=True,
                                     related_name="choice_list")
    answers = models.ManyToManyField(Choice, blank=True,
                                     related_name="answer_list")
    survey = models.ForeignKey(Survey)
    order = models.PositiveIntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.question


@receiver(pre_save, sender=Survey)
def survey_slug_handler(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)
