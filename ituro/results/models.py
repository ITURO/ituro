from django.db import models
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from projects.models import Project
from orders.models import LineFollowerStage, LineFollowerJuniorStage


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
class LineFollowerJuniorResult(BaseResult):
    project = models.ForeignKey(
        Project, limit_choices_to={"category": "line_follower_junior"})
    stage = models.ForeignKey(
        LineFollowerJuniorStage, verbose_name=_("Line Follower Junior Stage"))
    runway_out = models.PositiveSmallIntegerField(
        verbose_name=_("Runway Out Count"), default=0)

    class Meta:
        verbose_name = _("Line Follower Junior Result")
        verbose_name_plural = _("Line Follower Junior Results")
        ordering = ['disqualification', 'score']

    def __str__(self):
        return self.project.name


@receiver(models.signals.pre_save, sender=LineFollowerJuniorResult)
def line_follower_junior_result_calculate_score(sender, instance, *args,
                                                **kwargs):
    instance.score = instance.duration * (1 + 0.2 * instance.runway_out)


@python_2_unicode_compatible
class ConstructionResult(BaseResult):
    project = models.ForeignKey(
        Project, limit_choices_to={"category": "construction"})

    class Meta:
        verbose_name = _("Construction Result")
        verbose_name_plural = _("Construction Results")
        ordering = [
            "disqualification", "-score", "minutes", "seconds", "milliseconds"]

    def __str__(self):
        return self.project.name


@python_2_unicode_compatible
class BasketballResult(BaseResult):
    project = models.ForeignKey(
        Project, limit_choices_to={"category": "basketball"})
    basket1 = models.PositiveSmallIntegerField(verbose_name=_("Basket 1"))
    basket2 = models.PositiveSmallIntegerField(verbose_name=_("Basket 2"))
    basket3 = models.PositiveSmallIntegerField(verbose_name=_("Basket 3"))
    basket4 = models.PositiveSmallIntegerField(
        verbose_name=_("Moving Basket 1"))
    basket5 = models.PositiveSmallIntegerField(
        verbose_name=_("Moving Basket 2"))

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
        sum(range(6, 6 - instance.basket4, -1)) * 2,
        sum(range(6, 6 - instance.basket5, -1)) * 2)) * 10


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
    plexi_touch = models.PositiveSmallIntegerField(
        verbose_name=_("Plexi Touch Count"), default=0)
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
        (int(instance.stair1) + int(instance.stair2) +
         int(instance.stair3)) * 10,
        (int(instance.stair4)) * 40,
        (int(instance.stair5) + int(instance.stair6) +
         int(instance.stair7)) * 80,
        (int(instance.down6) + int(instance.down5) + int(instance.down4)) * 30,
        (int(instance.down3)) * 50,
        (int(instance.down1) + int(instance.down2)) * 20,
        (int(instance.is_complete)) * 40,
        instance.plexi_touch * (-10)
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
        verbose_name=_("Headway Amount (mm)"), default=0)
    stage2_minutes = models.PositiveSmallIntegerField(
        verbose_name=_("Stage2 Minutes"), default=0)
    stage2_seconds = models.PositiveSmallIntegerField(
        verbose_name=_("Stage2 Seconds"), default=0)
    stage2_milliseconds = models.PositiveSmallIntegerField(
        verbose_name=_("Stage2 Milliseconds"), default=0)

    class Meta:
        verbose_name = _("Self Balancing Result")
        verbose_name_plural = _("Self Balancing Results")
        ordering = [
            "disqualification", "-score", "minutes",
            "seconds", "milliseconds", "-headway_amount"]

    def __str__(self):
        return self.project.name


@receiver(models.signals.pre_save, sender=SelfBalancingResult)
def self_balancing_result_calculate_score(sender, instance, *args, **kwargs):
    instance.score = sum((
        instance.headway_amount * 0.1,
        (instance.stage2_minutes * 60 + instance.stage2_seconds +
         instance.stage2_milliseconds * 0.01) * 3))


@python_2_unicode_compatible
class ScenarioResult(BaseResult):
    project = models.ForeignKey(
        Project, limit_choices_to={"category": "scenario"})
    is_stopped = models.BooleanField(
        verbose_name=_("Is stopped?"), default=False)
    is_parked = models.BooleanField(
        verbose_name=_("Is parked?"), default=False)
    sign_succeed = models.PositiveSmallIntegerField(
        verbose_name=_("Succeed Signs"), default=0)

    class Meta:
        verbose_name = _("Scenario Result")
        verbose_name_plural = _("Scenario Results")
        ordering = ["disqualification", "-score",
                    "minutes", "seconds", "milliseconds"]

    def __str__(self):
        return self.project.name


@receiver(models.signals.pre_save, sender=ScenarioResult)
def scenario_result_calculate_score(sender, instance, *args, **kwargs):
    instance.score = sum((
        int(instance.is_stopped) * 30,
        int(instance.is_parked) * 100,
        instance.sign_succeed * 10))


@python_2_unicode_compatible
class InnovativeJury(models.Model):
    jury = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name = _("Innovative Jury")
        verbose_name_plural = _("Innovative Juries")
        ordering = ["jury"]

    def __str__(self):
        return self.jury


@python_2_unicode_compatible
class InnovativeJuryResult(models.Model):
    project = models.ForeignKey(
        Project, limit_choices_to={"category": "innovative"})
    jury = models.ForeignKey(InnovativeJury)
    jury_score = models.FloatField(
        verbose_name=_('Jury Score'), blank=True, default=0)
    design = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        verbose_name=_("Design"), default=0)
    innovative = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        verbose_name=_("Innovative"), default=0)
    technical = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        verbose_name=_("Technical"), default=0)
    presentation = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        verbose_name=_("Presentation"), default=0)
    opinion = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        verbose_name=_("Opinion"), default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Innovative Result")
        verbose_name_plural = _("Innovative Results")
        ordering = ["project", "jury"]
        unique_together = ('project', 'jury')

    def __str__(self):
        return self.project.name


@python_2_unicode_compatible
class InnovativeTotalResult(models.Model):
    project = models.ForeignKey(
        Project, limit_choices_to={"category": "innovative"}, unique=True)
    score = models.FloatField(verbose_name=_('Score'), default=0)

    class Meta:
        verbose_name = _("Innovative Total Result")
        verbose_name_plural = _("Innovative Total Results")
        ordering = ["project"]

    def __str__(self):
        return self.project.name


@receiver(models.signals.pre_save, sender=InnovativeJuryResult)
def innovative_jury_result_calculate_score(sender, instance, *args, **kwargs):
    instance.jury_score = sum((
        instance.design * 0.2,
        instance.innovative * 0.3,
        instance.technical * 0.25,
        instance.presentation * 0.1,
        instance.opinion * 0.05))
