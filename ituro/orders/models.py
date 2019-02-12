from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from projects.models import Project


@python_2_unicode_compatible
class LineFollowerStage(models.Model):
    order = models.PositiveSmallIntegerField(verbose_name=_("Stage Order"))
    is_current = models.BooleanField(
        verbose_name=_("Is current stage?"), default=False)
    is_final = models.BooleanField(
        verbose_name=_("Is final stage?"), default=False)
    orders_available = models.BooleanField(
        verbose_name=_("Race Orders Availability"), default=False)
    results_available = models.BooleanField(
        verbose_name=_("Race Results Availability"), default=False)

    class Meta:
        verbose_name = _("Line Follower Stage")
        verbose_name_plural = _("Line Follower Stages")
        ordering = ["order"]

    def __str__(self):
        return "Stage #{}".format(self.order)


@python_2_unicode_compatible
class LineFollowerJuniorStage(models.Model):
    order = models.PositiveSmallIntegerField(verbose_name=_("Stage Order"))
    is_current = models.BooleanField(
        verbose_name=_("Is current stage?"), default=False)
    is_final = models.BooleanField(
        verbose_name=_("Is final stage?"), default=False)
    orders_available = models.BooleanField(
        verbose_name=_("Race Orders Availability"), default=False)
    results_available = models.BooleanField(
        verbose_name=_("Race Results Availability"), default=False)

    class Meta:
        verbose_name = _("Line Follower Junior Stage")
        verbose_name_plural = _("Line Follower Junior Stages")
        ordering = ["order"]

    def __str__(self):
        return "Stage #{}".format(self.order)


@python_2_unicode_compatible
class BaseOrder(models.Model):
    order = models.PositiveSmallIntegerField(verbose_name=_("Race Order"))

    class Meta:
        abstract = True

    def __str__(self):
        return self.project.name


class LineFollowerRaceOrder(BaseOrder):
    stage = models.ForeignKey(
        LineFollowerStage, verbose_name=_("Line Follower Stage"))
    project = models.ForeignKey(Project, verbose_name=_("Project"))

    class Meta:
        verbose_name = _("Line Follower Race Order")
        verbose_name_plural = _("Line Follower Race Orders")
        ordering = ["order"]
        unique_together = (("project", "stage"),)


class LineFollowerJuniorRaceOrder(BaseOrder):
    stage = models.ForeignKey(
        LineFollowerJuniorStage, verbose_name=_("Line Follower Junior Stage"))
    project = models.ForeignKey(Project, verbose_name=_("Project"))

    class Meta:
        verbose_name = _("Line Follower Junior Race Order")
        verbose_name_plural = _("Line Follower Junior Race Orders")
        ordering = ["order"]
        unique_together = (("project", "stage"),)


class RaceOrder(BaseOrder):
    project = models.OneToOneField(Project, verbose_name=_("Project"))

    class Meta:
        verbose_name = _("Race Order")
        verbose_name_plural = _("Race Orders")
        ordering = ["order"]
