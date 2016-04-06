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
        verbose_name=_("Penalty Extinguish Count"))
    wall_hit = models.PositiveSmallIntegerField(
        verbose_name=_("Wall Touching Count"))
    interfering_robot = models.PositiveSmallIntegerField(
        verbose_name=_("Interfering Robot Count"))
    touching_candles = models.PositiveSmallIntegerField(
        verbose_name=_("Touching Candles Count"))
    pre_extinguish = models.PositiveSmallIntegerField(
        verbose_name=_("Pre-Start Systems Count"))
    is_complete = models.BooleanField(
        verbose_name=_("Extinguish all candles"),default=False)


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
        instance.extinguish_failure * 50,
        instance.wall_hit * (-10),
        instance.touching_candles * (-100),
        instance.pre_extinguish * (-50),
        instance.interfering_robot * (-30),
        int(instance.is_complete) * ((300 - instance.duration)/4)))


@python_2_unicode_compatible
class BasketballResult(BaseResult):
    project = models.ForeignKey(
        Project, limit_choices_to={"category": "basketball"})
    basket1 = models.PositiveSmallIntegerField(verbose_name=_("Basket 1"))
    basket2 = models.PositiveSmallIntegerField(verbose_name=_("Basket 2"))
    basket3 = models.PositiveSmallIntegerField(verbose_name=_("Basket 3"))
    basket4 = models.PositiveSmallIntegerField(verbose_name=_("Basket 4"))
    basket5 = models.PositiveSmallIntegerField(verbose_name=_("Basket 5"))

    class Meta:
        verbose_name = _("Basketball Result")
        verbose_name_plural = _("Basketball Results")
        ordering = [
            "disqualification", "-score", "minutes", "seconds", "milliseconds"]

    def __str__(self):
        return self.project.name


@receiver(models.signals.pre_save, sender=BasketballResult)
def basketball_result_calculate_score(sender, instance, *args, **kwargs):
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
    down6 = models.BooleanField(verbose_name=_("Down #6"), default=False)
    down5 = models.BooleanField(verbose_name=_("Down #5"), default=False)
    down4 = models.BooleanField(verbose_name=_("Down #4"), default=False)
    down3 = models.BooleanField(verbose_name=_("Down #3"), default=False)
    down2 = models.BooleanField(verbose_name=_("Down #2"), default=False)
    down1 = models.BooleanField(verbose_name=_("Down #1"), default=False)
    is_complete = models.BooleanField(
        verbose_name=_("Is finish?"), default=False)

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
        (int(instance.stair5))* 80,
        (int(instance.stair6))* 100,
        (int(instance.stair7))* 120,
        (int(instance.down6) + int(instance.down5) + int(instance.down4)) * 20,
        (int(instance.down1) + int(instance.down2) + int(instance.down3)) * 10,
        (int(instance.is_complete)) * 40,
        instance.duration * (-5)
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
    stage3_minutes = models.PositiveSmallIntegerField(
        verbose_name=_("Stage3 Minutes"))
    stage3_seconds = models.PositiveSmallIntegerField(
        verbose_name=_("Stage3 Seconds"))
    stage3_milliseconds = models.PositiveSmallIntegerField(
        verbose_name=_("Stage3 Milliseconds"))

    class Meta:
        verbose_name = _("Self Balancing Result")
        verbose_name_plural = _("Self Balancing Results")
        ordering = [
            "disqualification", "-score", "-seconds", "-milliseconds",
            "-headway_amount", "stage3_minutes", "stage3_seconds",
            "stage3_milliseconds"]

    def __str__(self):
        return self.project.name


@receiver(models.signals.pre_save, sender=SelfBalancingResult)
def self_balancing_result_calculate_score(sender, instance, *args, **kwargs):
    instance.score = sum((
        instance.duration, instance.headway_amount * 1.5,
        (instance.stage3_minutes * 60 + instance.stage3_seconds +
        instance.stage3_milliseconds * 0.01) * 2))


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
