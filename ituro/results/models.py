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
        verbose_name=_("Is best result?"), default=True)
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


@python_2_unicode_compatible
class FireFighterResult(BaseResult):
    project = models.ForeignKey(
        Project, limit_choices_to={"category": "fire_fighter"})
    extinguish_success = models.PositiveSmallIntegerField(
        verbose_name=_("Succesful Extinguish Count"))
    extinguish_failure = models.PositiveSmallIntegerField(
        verbose_name=_("Pre-extinguishing Count"))
    wall_hit = models.PositiveSmallIntegerField(
        verbose_name=_("Wall Hit Count"))
    interfering_robot = models.PositiveSmallIntegerField(
        verbose_name=_("Interfering Robot Count"))
    touching_candles = models.PositiveSmallIntegerField(
        verbose_name=_("Touching Candles Count"))
    extinguish_penalty = models.PositiveSmallIntegerField(
        verbose_name=_("Extinguish with penalty Count"))
    is_complete = models.BooleanField(
        verbose_name=_("Extinguished all candles"), default=False)

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
        instance.extinguish_success * 150,
        instance.extinguish_failure * (-50),
        instance.interfering_robot * (-30),
        instance.touching_candles * (-100),
        instance.extinguish_penalty * (50),
        instance.wall_hit * (-10)))
    if instance.is_complete:
        instance.score = instance.score + (300 - instance.duration) / 4


@python_2_unicode_compatible
class BasketballResult(BaseResult):
    project = models.ForeignKey(
        Project, limit_choices_to={"category": "basketball"})
    basket1 = models.PositiveSmallIntegerField(verbose_name=_("Basket 1"))
    basket2 = models.PositiveSmallIntegerField(verbose_name=_("Basket 2"))
    basket3 = models.PositiveSmallIntegerField(verbose_name=_("Basket 3"))
    basket4 = models.PositiveSmallIntegerField(verbose_name=_("Basket 4"))
    basket5 = models.PositiveSmallIntegerField(verbose_name=_("Basket 5"))
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
        instance.basket1, instance.basket2, instance.basket3, instance.basket4,
        instance.basket5))
    instance.score = sum((
        sum(range(6, 6 - instance.basket1, -1)),
        sum(range(6, 6 - instance.basket2, -1)),
        sum(range(6, 6 - instance.basket3, -1)),
        sum(range(6, 6 - instance.basket4, -1)),
        sum(range(6, 6 - instance.basket5, -1)))) * 10


@python_2_unicode_compatible
class StairClimbingResult(BaseResult):
    project = models.ForeignKey(
        Project, limit_choices_to={"category": "stair_climbing"})
    stair1 = models.BooleanField(verbose_name=_("Stair #1"), default=False)
    stair2 = models.BooleanField(verbose_name=_("Stair #2"), default=False)
    stair3 = models.BooleanField(verbose_name=_("Stair #3"), default=False)
    stair4 = models.BooleanField(verbose_name=_("Stair #4"), default=False)
    stair5 = models.BooleanField(verbose_name=_("Stair #5"), default=False)
    stair6 = models.BooleanField(verbose_name=_("Stair #6"), default=False)
    stair7 = models.BooleanField(verbose_name=_("Stair #7"), default=False)
    downstair1 = models.BooleanField(verbose_name=_("DownStair #1"), default=False)
    downstair2 = models.BooleanField(verbose_name=_("DownStair #2"), default=False)
    downstair3 = models.BooleanField(verbose_name=_("DownStair #3"), default=False)
    downstair4 = models.BooleanField(verbose_name=_("DownStair #4"), default=False)
    downstair5 = models.BooleanField(verbose_name=_("DownStair #5"), default=False)
    downstair6 = models.BooleanField(verbose_name=_("DownStair #6"), default=False)
    is_complete = models.BooleanField(
        verbose_name=_("Is Complete?"), default=False)
    touching_plexy = models.PositiveSmallIntegerField(
        verbose_name=_("Touching Plexy Count"))

    class Meta:
        verbose_name = _("Stair Climbing Result")
        verbose_name_plural = _("Stair Climbing Results")
        ordering = [
            "disqualification", "-score", "minutes", "seconds", "milliseconds"]

    def __str__(self):
        return self.project.name


@receiver(models.signals.pre_save, sender=StairClimbingResult)
def stair_climbing_result_calculate_score(sender, instance, *args, **kwargs):
    instance.score = sum((
        (int(instance.stair1) + int(instance.stair2) + int(instance.stair3)) * 10,
        (int(instance.stair4)) * 40,
        (int(instance.stair5)) * 80,
        (int(instance.stair6)) * 100,
        (int(instance.stair7)) * 120,
        (int(instance.downstair6)) * 20,
        (int(instance.downstair5)) * 20,
        (int(instance.downstair4)) * 20,
        (int(instance.downstair3)) * 10,
        (int(instance.downstair2)) * 10,
        (int(instance.downstair1)) * 10,
        (int(instance.is_complete)) * 40,
        (int(instance.touching_plexy)) * (-5)
        ))


@python_2_unicode_compatible
class MazeResult(BaseResult):
    project = models.ForeignKey(
        Project, limit_choices_to={"category": "maze"})

    class Meta:
        verbose_name = _("Maze Result")
        verbose_name_plural = _("Maze Results")
        ordering = ["disqualification", "score"]

    def __str__(self):
        return self.project.name


@receiver(models.signals.pre_save, sender=MazeResult)
def maze_result_calculate_score(sender, instance, *args, **kwargs):
    instance.score = sum((
        instance.minutes * 60,
        instance.seconds,
        instance.milliseconds * 0.01))


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

    class Meta:
        verbose_name = _("Color Selecting Result")
        verbose_name_plural = _("Color Selecting Results")
        ordering = [
            "disqualification", "-score", "minutes", "seconds", "milliseconds"]

    def __str__(self):
        return self.project.name


@receiver(models.signals.pre_save, sender=ColorSelectingResult)
def color_selecting_result_calculate_score(sender, instance, *args, **kwargs):
    instance.score = sum((
        instance.obtain * 100,
        instance.place_success * 200,
        instance.place_failure * (-50)))


@python_2_unicode_compatible
class SelfBalancingResult(BaseResult):
    project = models.ForeignKey(
        Project, limit_choices_to={"category": "self_balancing"})
    headway_amount = models.PositiveSmallIntegerField(
        verbose_name=_("Headway Amount (cm)"))
    parcour3_minutes = models.PositiveSmallIntegerField(
        verbose_name=_("Parcour-3 Minutes"))
    parcour3_seconds = models.PositiveSmallIntegerField(
        verbose_name=_("Parcour-3 Seconds"))
    parcour3_milliseconds = models.PositiveSmallIntegerField(
        verbose_name=_("Parcour-3 Milliseconds"))

    class Meta:
        verbose_name = _("Self Balancing Result")
        verbose_name_plural = _("Self Balancing Results")
        ordering = [
            "disqualification", "-score", "-seconds", "-milliseconds",
            "-headway_amount", "parcour3_minutes", "parcour3_seconds",
            "parcour3_milliseconds"]

    def __str__(self):
        return self.project.name


@receiver(models.signals.pre_save, sender=SelfBalancingResult)
def self_balancing_result_calculate_score(sender, instance, *args, **kwargs):
    instance.score = sum((
        instance.duration, instance.headway_amount * 15,
        instance.parcour3_minutes*60, instance.parcour3_seconds,
        instance.parcour3_milliseconds*0.01
        ))


@python_2_unicode_compatible
class ScenarioResult(BaseResult):
    project = models.ForeignKey(
        Project, limit_choices_to={"category": "scenario"})
    obtain_block = models.PositiveSmallIntegerField(
        verbose_name=_("Obtained Block Count"))
    total_referee_point = models.PositiveSmallIntegerField(
        verbose_name=_("Total Referee Point"))

    class Meta:
        verbose_name = _("Scenario Result")
        verbose_name_plural = _("Scenario Results")
        ordering = ["disqualification", "-score"]

    def __str__(self):
        return self.project.name


@receiver(models.signals.pre_save, sender=ScenarioResult)
def scenario_result_calculate_score(sender, instance, *args, **kwargs):
    instance.score = sum((
        instance.obtain_block,
        instance.total_referee_point,
        ))


@python_2_unicode_compatible
class InnovativeResult(BaseResult):
    project = models.ForeignKey(
        Project, limit_choices_to={"category": "innovative"})
    design = models.PositiveSmallIntegerField(
        verbose_name=_("Design"), default=0)
    digital_design = models.PositiveSmallIntegerField(
        verbose_name=_("Digital Design"), default=0)
    innovative = models.PositiveSmallIntegerField(
        verbose_name=_("Innovative"), default=0)
    technical = models.PositiveSmallIntegerField(
        verbose_name=_("Technical"), default=0)
    presentation = models.PositiveSmallIntegerField(
        verbose_name=_("Presentation"), default=0)
    opinion = models.PositiveSmallIntegerField(
        verbose_name=_("Opinion"), default=0)

    class Meta:
        verbose_name = _("Innovative Result")
        verbose_name_plural = _("Innovative Results")
        ordering = ["disqualification", "-score"]

    def __str__(self):
        return self.project.name


@receiver(models.signals.pre_save, sender=InnovativeResult)
def innovative_result_calculate_score(sender, instance, *args, **kwargs):
    instance.score = sum((
        instance.design * 0.2,
        instance.digital_design * 0.1,
        instance.innovative * 0.3,
        instance.technical * 0.25,
        instance.presentation * 0.1,
        instance.opinion * 0.05))
