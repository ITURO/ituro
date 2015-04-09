from django.db import models
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from projects.models import Project
from orders.models import LineFollowerStage


class BaseResult(models.Model):
    score = models.FloatField(verbose_name=_('Score'), blank=True)
    minutes = models.PositiveSmallIntegerField(verbose_name=_("Minutes"))
    seconds = models.PositiveSmallIntegerField(verbose_name=_("Seconds"))
    milliseconds = models.PositiveSmallIntegerField(
        verbose_name=_("Milliseconds"))
    disqualification = models.BooleanField(
        verbose_name=_('Disqualification'), default=False)
    is_best = models.BooleanField(
        verbose_name=_("Is best result?"), default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    @property
    def duration(self):
        return self.minutes * 60 + self.seconds + self.milliseconds * 0.01

    @property
    def duration_pretty(self):
        return "{} minutes, {} seconds, {} milliseconds".format(
            self.minutes, self.seconds, self.milliseconds)


@python_2_unicode_compatible
class LineFollowerResult(BaseResult):
    project = models.ForeignKey(
        Project, limit_choices_to={"category": "line_follower"})
    stage = models.ForeignKey(
        LineFollowerStage, verbose_name=_("Line Follower Stage"))
    runway_out = models.PositiveSmallIntegerField(
        verbose_name=_("Runway Out Count"), default=0)

    class Meta:
        verbose_name = _("Line Follower Result")
        verbose_name_plural = _("Line Follower Results")
        ordering = ['disqualification', 'score']

    def __str__(self):
        return self.project.name


@receiver(models.signals.pre_save, sender=LineFollowerResult)
def line_follower_result_calculate_score(sender, instance, *args, **kwargs):
    instance.score = instance.duration * (1 + 0.2 * instance.runway_out)
    import ipdb;ipdb.set_trace()


@python_2_unicode_compatible
class FireFighterResult(BaseResult):
    project = models.ForeignKey(
        Project, limit_choices_to={"category": "fire_fighter"})
    extinguish_success = models.PositiveSmallIntegerField(
        verbose_name=_("Succesful Extinguish Count"))
    extinguish_failure = models.PositiveSmallIntegerField(
        verbose_name=_("Unsuccessful Extinguish Count"))
    wall_hit = models.PositiveSmallIntegerField(
        verbose_name=_("Wall Hit Count"))

    class Meta:
        verbose_name = _("Fire Fighter Result")
        verbose_name_plural = _("Fire Fighter Results")
        ordering = [
            "disqualification", "-score", "minutes", "seconds", "milliseconds"]

    def __str__(self):
        return self.project.name


@receiver(models.signals.pre_save, sender=FireFighterResult)
def fire_fighter_result_calculate_score(sender, instance, *args, **kwargs):
    instance.score = sum((
        instance.extinguish_success * 100,
        instance.extinguish_failure * (-50),
        instance.wall_hit * (-15)))


@python_2_unicode_compatible
class BasketballResult(BaseResult):
    project = models.ForeignKey(
        Project, limit_choices_to={"category": "basketball"})
    basket1 = models.PositiveSmallIntegerField(verbose_name=_("Basket 1"))
    basket2 = models.PositiveSmallIntegerField(verbose_name=_("Basket 2"))
    basket3 = models.PositiveSmallIntegerField(verbose_name=_("Basket 3"))
    basket4 = models.PositiveSmallIntegerField(verbose_name=_("Basket 4"))
    total = models.PositiveSmallIntegerField(
        verbose_name=_("Total Basket"), blank=True)

    class Meta:
        verbose_name = _("Basketball Result")
        verbose_name_plural = _("Basketball Results")
        ordering = [
            "disqualification", "-score", "total", "minutes", "seconds", "milliseconds"]

    def __str__(self):
        return self.project.name


@receiver(models.signals.pre_save, sender=BasketballResult)
def basketball_result_calculate_score(sender, instance, *args, **kwargs):
    instance.total = sum((
        instance.basket1, instance.basket2, instance.basket3, instance.basket4))
    instance.score = sum((
        sum(range(5, 5 - instance.basket1, -1)),
        sum(range(6, 6 - instance.basket2, -1)),
        sum(range(6, 6 - instance.basket3, -1)),
        sum(range(5, 5 - instance.basket4, -1)))) * 10


@python_2_unicode_compatible
class StairClimbingResult(BaseResult):
    project = models.ForeignKey(
        Project, limit_choices_to={"category": "stair_climbing"})
    stair1 = models.BooleanField(verbose_name=_("Stair #1"), default=False)
    stair2 = models.BooleanField(verbose_name=_("Stair #2"), default=False)
    stair3 = models.BooleanField(verbose_name=_("Stair #3"), default=False)
    stair4 = models.BooleanField(verbose_name=_("Stair #4"), default=False)
    downstairs = models.PositiveSmallIntegerField(
        verbose_name=_("Downstairs Count"))

    class Meta:
        verbose_name = _("Stair Climbing Result")
        verbose_name_plural = _("Stair Climbing Results")
        ordering = [
            "disqualification", "-score", "minutes", "seconds", "milliseconds"]

    def __str__(self):
        return self.project.name


@receiver(models.signals.pre_save, sender=StairClimbingResult)
def stair_climbing_result_calculate_score(sender, instance, *args, **kwargs):
    instance.score = sum(
        (int(instance.stair1) + int(instance.stair2)) * 10,
        (int(instance.stair3) + int(instance.stair4)) * 20,
        instance.downstairs * 10)


@python_2_unicode_compatible
class MazeResult(BaseResult):
    project = models.ForeignKey(
        Project, limit_choices_to={"category": "maze"})

    class Meta:
        verbose_name = _("Maze Result")
        verbose_name_plural = _("Maze Results")
        ordering = ["disqualification", "minutes", "seconds", "milliseconds"]

    def __str__(self):
        return self.project.name


@python_2_unicode_compatible
class ColorSelectingResult(BaseResult):
    project = models.ForeignKey(
        Project, limit_choices_to={"category": "color_selecting"})
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
        ordering = [
            "disqualification", "-score", "minutes", "seconds", "milliseconds"]

    def __str__(self):
        return self.project.name


@receiver(models.signals.pre_save, sender=ColorSelectingResult)
def color_selecting_result_calculate_score(sender, instance, *args, **kwargs):
    instance.score = sum(
        instance.obtain * 100,
        instance.place_success * 400,
        instance.place_failure * 50,
        instance.place_partial * 100)


@python_2_unicode_compatible
class SelfBalancingResult(BaseResult):
    project = models.ForeignKey(
        Project, limit_choices_to={"category": "self_balancing"})
    headway_amount = models.PositiveSmallIntegerField(
        verbose_name=_("Headway Amount (cm)"))
    impact = models.BooleanField(verbose_name=_("Impact Test"), default=False)
    headway_minutes = models.PositiveSmallIntegerField(
        verbose_name=_("Headway Minutes"))
    headway_seconds = models.PositiveSmallIntegerField(
        verbose_name=_("Headway Seconds"))
    headway_milliseconds = models.PositiveSmallIntegerField(
        verbose_name=_("Headway Milliseconds"))

    class Meta:
        verbose_name = _("Self Balancing Result")
        verbose_name_plural = _("Self Balancing Results")
        ordering = [
            "disqualification", "-score", "-seconds", "-milliseconds",
            "-headway_amount", "headway_minutes", "headway_seconds",
            "headway_milliseconds"]

    def __str__(self):
        return self.project.name


@receiver(models.signals.pre_save, sender=SelfBalancingResult)
def self_balancing_result_calculate_score(sender, instance, *args, **kwargs):
    instance.score = sum(
        instance.duration, instance.headway_amount, 30 * int(instance.impact))


@python_2_unicode_compatible
class ScenarioResult(BaseResult):
    project = models.ForeignKey(
        Project, limit_choices_to={"category": "scenario"})

    class Meta:
        verbose_name = _("Scenario Result")
        verbose_name_plural = _("Scenario Results")
        ordering = ["disqualification", "-score"]

    def __str__(self):
        return self.project.name


@python_2_unicode_compatible
class InnovativeResult(BaseResult):
    project = models.ForeignKey(
        Project, limit_choices_to={"category": "innovative"})

    class Meta:
        verbose_name = _("Innovative Result")
        verbose_name_plural = _("Innovative Results")
        ordering = ["disqualification", "-score"]

    def __str__(self):
        return self.project.name
