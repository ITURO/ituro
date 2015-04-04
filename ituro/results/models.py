from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from projects.models import Project
from orders.models import LineFollowerStage


@python_2_unicode_compatible
class BaseResult(models.Model):
    project = models.ForeignKey(Project)
    score = models.FloatField(verbose_name=_('Score'), blank=True)
    minutes = models.PositiveSmallIntegerField(verbose_name=_("Minutes"))
    seconds = models.PositiveSmallIntegerField(verbose_name=_("Seconds"))
    miliseconds = models.PositiveSmallIntegerField(
        verbose_name=_("Miliseconds"))
    is_attended = models.BooleanField(
        verbose_name=_('Is attended the race?'), default=False)
    order = models.IntegerField(verbose_name=_('Race Order'))
    disqualification = models.BooleanField(
        verbose_name=_('Disqualification'), default=False)
    is_best = models.BooleanField(
        verbose_name=_("Is best result?"), default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "{}: {}".format(self.project.category, self.project.name)

    def calculate_score(self):
        pass

    @property
    def duration(self):
        return "{} minutes, {} seconds, {} miliseconds".format(
            self.minutes, self.seconds, self.miliseconds)

    @property
    def total_seconds(self):
        return self.minutes * 60 + self.seconds + self.miliseconds * 0.01


class LineFollowerResult(BaseResult):
    stage = models.ForeignKey(
        LineFollowerStage, verbose_name=_("Line Follower Stage"))
    runway_out = models.PositiveSmallIntegerField(
        verbose_name=_("Runway Out Count"))

    class Meta:
        verbose_name = _("Line Follower Result")
        verbose_name_plural = _("Line Follower Results")
        ordering = ['score']


class FireFighterResult(BaseResult):
    extinguish_success = models.PositiveSmallIntegerField(
        verbose_name=_("Succesful Extinguish Count"))
    extinguish_failure = models.PositiveSmallIntegerField(
        verbose_name=_("Unsuccessful Extinguish Count"))

    class Meta:
        verbose_name = _("Fire Fighter Result")
        verbose_name_plural = _("Fire Fighter Results")
        ordering = ["-score", "minutes", "seconds", "miliseconds"]


class BasketballResult(BaseResult):
    basket1 = models.PositiveSmallIntegerField(verbose_name=_("Basket 1"))
    basket2 = models.PositiveSmallIntegerField(verbose_name=_("Basket 2"))
    basket3 = models.PositiveSmallIntegerField(verbose_name=_("Basket 3"))
    basket4 = models.PositiveSmallIntegerField(verbose_name=_("Basket 4"))
    total = models.PositiveSmallIntegerField(verbose_name=_("Total Basket"))

    class Meta:
        verbose_name = _("Basketball Result")
        verbose_name_plural = _("Basketball Results")
        ordering = ["-score", "total", "minutes", "seconds", "miliseconds"]


class StairClimbing(BaseResult):
    stair1 = models.BooleanField(verbose_name=_("Stair #1"), default=False)
    stair2 = models.BooleanField(verbose_name=_("Stair #2"), default=False)
    stair3 = models.BooleanField(verbose_name=_("Stair #3"), default=False)
    stair4 = models.BooleanField(verbose_name=_("Stair #4"), default=False)
    downstairs = models.PositiveSmallIntegerField(
        verbose_name=_("Downstairs Count"))

    class Meta:
        verbose_name = _("Stair Climbing Result")
        verbose_name_plural = _("Stair Climbing Results")
        ordering = ["-score", "minutes", "seconds", "miliseconds"]


class MazeResult(BaseResult):
    class Meta:
        verbose_name = _("Maze Result")
        verbose_name_plural = _("Maze Results")
        ordering = ["minutes", "seconds", "miliseconds"]


class ColorSelectingResult(BaseResult):
    obtain = models.PositiveSmallIntegerField(
        verbose_name=_("Cylinder Obtain Count"))
    place_success = models.PositiveSmallIntegerField(
        verbose_name=_("Cylinder Successful Placement Count"))
    place_failure = models.PositiveSmallIntegerField(
        verbose_name=_("Cylinder Unsuccessful Placement Count"))
    place_partial = models.PositiveSmallIntegerField(
        verbose_name=_("Cylinder Partial Placement Count"))

    class Meta:
        verbose_name = _("Color Selecting Result")
        verbose_name_plural = _("Color Selecting Results")
        ordering = ['-score', 'minutes', 'seconds', 'miliseconds']


class SelfBalancingResult(BaseResult):
    headway_amount = models.PositiveSmallIntegerField(
        verbose_name=_("Headway Amount (cm)"))
    impact = models.BooleanField(verbose_name=_("Impact Test"), default=False)
    headway_minutes = models.PositiveSmallIntegerField(
        verbose_name=_("Headway Minutes"))
    headway_seconds = models.PositiveSmallIntegerField(
        verbose_name=_("Headway Seconds"))
    headway_miliseconds = models.PositiveSmallIntegerField(
        verbose_name=_("Headway Miliseconds"))

    class Meta:
        verbose_name = _("Self Balancing Result")
        verbose_name_plural = _("Self Balancing Results")
        ordering = [
            "-score", "-seconds", "-miliseconds", "-headway_amount",
            "headway_minutes", "headway_seconds", "headway_miliseconds"]


class ScenarioResult(BaseResult):
    pass


class InnovativeResult(BaseResult):
    pass
