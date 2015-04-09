from django.db import models
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from projects.models import Project


@python_2_unicode_compatible
class SumoMatch(models.Model):
    is_played = models.BooleanField(
        verbose_name=_('Game played?'), default=False)
    home_score = models.PositiveSmallIntegerField(
        verbose_name=_('Home Score'), default=0)
    away_score = models.PositiveSmallIntegerField(
        verbose_name=_('Away Score'), default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return " vs. ".join([self.home.name, self.away.name])


@python_2_unicode_compatible
class SumoGroup(models.Model):
    order = models.PositiveSmallIntegerField(verbose_name=_("Order"))
    is_final = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Sumo Group")
        verbose_name_plural = _("Sumo Groups")
        ordering = ["order"]

    def __str__(self):
        return "Group #{}".format(self.order)


@python_2_unicode_compatible
class SumoGroupTeam(models.Model):
    group = models.ForeignKey(SumoGroup, verbose_name=_("Sumo Group"))
    robot = models.ForeignKey(Project, verbose_name=_("Sumo Robot"))
    point = models.PositiveSmallIntegerField(verbose_name=_("Point"), default=0)
    order = models.PositiveSmallIntegerField(verbose_name=_("Order"), default=0)
    average = models.IntegerField(verbose_name=_("Average"), default=0)
    is_attended = models.BooleanField(
         verbose_name=_("Is attended?"), default=True)

    class Meta:
        verbose_name = _("Sumo Group Team")
        verbose_name_plural = _("Sumo Group Teams")
        ordering = ["-point", "-average", "order"]

    def __str__(self):
        return "Group {}: {}".format(self.group.order, self.robot.name)


class SumoGroupMatch(SumoMatch):
    home = models.ForeignKey(Project, related_name="group_home")
    away = models.ForeignKey(Project, related_name="group_away", null=True)
    group = models.ForeignKey(SumoGroup, verbose_name=_("Sumo Group"))
    order = models.PositiveSmallIntegerField(
        verbose_name=_("Order"), default=0)

    class Meta:
        verbose_name = _("Sumo Group Match")
        verbose_name_plural = _("Sumo Group Matches")
        ordering = ["group__order", "order"]


class SumoStage(models.Model):
    order = models.PositiveSmallIntegerField(verbose_name=_("Order"))


class SumoStageMatch(SumoMatch):
    home = models.ForeignKey(Project, related_name="stage_home")
    away = models.ForeignKey(Project, related_name="stage_away", null=True)
    stage = models.ForeignKey(SumoStage, verbose_name=_("Sumo Stage"))


    class Meta:
        verbose_name = _("Sumo Stage Match")
        verbose_name_plural = _("Sumo Stage Matches")
        ordering = ["stage__order"]
