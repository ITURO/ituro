from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible
from django.db.models.signals import pre_save, post_save
from projects.models import Project
import random


@python_2_unicode_compatible
class SimulationStage(models.Model):
    number = models.PositiveIntegerField(verbose_name=_("Stage"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    create_orders = models.BooleanField(default=False)
    remove_orders = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Simulation Stage"
        verbose_name_plural = "Simulation Stages"
        ordering = ["number"]

    def __str__(self):
        return "Stage: #" + str(self.number)


@python_2_unicode_compatible
class SimulationStageMatch(models.Model):
    stage = models.ForeignKey(SimulationStage, verbose_name=_("Stage"))
    order = models.PositiveIntegerField(verbose_name=_("Order"))
    raund = models.PositiveSmallIntegerField(verbose_name=_("Raund"))
    cat = models.ForeignKey(Project, verbose_name=_("Cat"), null=True, blank=True, related_name="cat")
    rat = models.ForeignKey(Project, verbose_name=_("Rat"), null=True, blank=True, related_name="rat")
    won = models.ForeignKey(Project, verbose_name=_("Winner"), null=True, blank=True, related_name="won")
    is_played = models.BooleanField(default=False, verbose_name=_("Is played?"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))

    class Meta:
        verbose_name = "Simulation Stage Match"
        verbose_name_plural = "Simulation Stage Matches"
        ordering = ["order", "stage__number"]

    def __str__(self):
        return "Stage: " + str(self.stage.number) + " Order: " + str(self.order) + " Raund: " + str(self.raund)

@python_2_unicode_compatible
class SimulationStageMatchResult(models.Model):
    match = models.ForeignKey(SimulationStageMatch, verbose_name=_("Match"))
    minutes = models.PositiveSmallIntegerField(verbose_name=_("Minutes"))
    seconds = models.PositiveSmallIntegerField(verbose_name=_("Seconds"))
    milliseconds = models.PositiveSmallIntegerField(verbose_name=_("Milliseconds"))
    distance = models.PositiveIntegerField(verbose_name=_("Distance"))
    is_caught = models.BooleanField(default=False, verbose_name=_("Is caught?"))
    is_cancelled = models.BooleanField(default=False, verbose_name=_("Is cancelled?"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))

    class Meta:
        verbose_name = "Simulation Stage Match Result"
        verbose_name_plural = "Simulation Stage Match Results"
        ordering = ["is_cancelled", "is_caught", "distance"]

    def __str__(self):
        return self.match

    def calculate_duration(self):
        return 6000*self.minutes + 100*self.seconds + self.milliseconds

    
@receiver(post_save, sender=SimulationStageMatchResult, dispatch_uid="simulation_winner")
def simulation_stage_match_winner_handler(sender, instance, created, **kwargs):
    results = SimulationStageMatchResult.objects.filter(match=instance.match)
    if results.count() == 2:
        if results.filter(is_cancelled=True).count() == 2:
            instance.match.won = None
        elif results.filter(is_caught=True).count() == 2:
            query = results.filter(is_caught=True)
            duration1 = query[0].calculate_duration()
            duration2 = query[1].calculate_duration()
            if duration1 > duration2:
                instance.match.won = query[0].cat
            elif duration2 > duration1:
                instance.match.won = query[1].cat
            else:
                secure_random = random.SystemRandom()
                instance.match.won = secure_random.choice(list(query)).cat
        elif results.filter(is_caught=True).count() == 1:
            instance.match.won = results.filter(is_caught=True)[0].cat
        elif results.filter(is_cancelled=False, is_caught=False).count() == 2:
            query = results.filter(is_cancelled=False, is_caught=False)
            distance1 = query[0].distance
            distance2 = query[1].distance
            if distance1 > distance2:
                instance.match.won = query[1].rat
            elif distance2 > distance1:
                instance.match.won = query[0].rat
            else:
                secure_random = random.SystemRandom()
                instance.match.won = secure_random.choice(list(query)).rat
 

@receiver(post_save, sender=SimulationStage, dispatch_uid="simulation_stage")
def simulation_stage_handler(sender, instance, created, **kwargs):
    from simulation.utils import create_orders, remove_orders
    if instance.create_orders and not instance.remove_orders:
        create_orders(instance.number)
    elif not instance.create_orders and instance.remove_orders:
        remove_orders(instance.number)

                
        


