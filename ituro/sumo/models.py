from django.db import models
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from projects.models import Project


@python_2_unicode_compatible
class SumoMatch(models.Model):
    home = models.ForeignKey(Project, related_name='home')
    away = models.ForeignKey(Project, related_name='away', null=True)
    is_played = models.BooleanField(verbose_name='Game played?')
    home_score = models.PositiveSmallIntegerField(verbose_name=_('Home Score'))
    away_score = models.PositiveSmallIntegerField(verbose_name=_('Away Score'))

    class Meta:
        abstract = True

    def __str__(self):
        return " vs. ".join([self.home.name, self.away.name])

    @property
    def winner(self):
        if self.away is None:
            return self.home

        if self.home_score > self.away_score:
            return self.home
        elif self.home_score < self.away_score:
            return self.away

        return None


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


class SumoGroupTeam(models.Model):
    group = models.ForeignKey(SumoGroup, verbose_name=_("Sumo Group"))
    robot = models.ForeignKey(Project, verbose_name=_("Sumo Robot"))
    point = models.PositiveSmallIntegerField(verbose_name=_("Point"))
    order = models.PositiveSmallIntegerField(verbose_name=_("Order"))
    average = models.IntegerField(verbose_name=_("Average"))

    class Meta:
        verbose_name = _("Sumo Group Team")
        verbose_name_plural = _("Sumo Group Teams")
        ordering = ["order"]

    def __str__(self):
        return "Group {}: {}".format(self.group.order, self.robot.name)


class SumoGroupMatch(SumoMatch):
    group = models.ForeignKey(SumoGroup, verbose_name=_("Sumo Group"))

    class Meta:
        verbose_name = _("Sumo Group Match")
        verbose_name_plural = _("Sumo Group Matches")
        ordering = ["group__order"]


@receiver(models.signals.post_save, sender=SumoGroupMatch)
def sumo_group_calculate_points(sender, instance, *args, **kwargs):
    pass


class SumoStage(models.Model):
    order = models.PositiveSmallIntegerField(verbose_name=_("Order"))


class SumoStageMatch(SumoMatch):
    stage = models.ForeignKey(SumoStage, verbose_name=_("Sumo Stage"))

    class Meta:
        verbose_name = _("Sumo Stage Match")
        verbose_name_plural = _("Sumo Stage Matches")
        ordering = ["stage__order"]
