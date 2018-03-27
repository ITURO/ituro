from django.db import models, Error
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible
from django.db.models.signals import post_save, post_delete, pre_save
from projects.models import Project
import random
import requests
import uuid
from django.conf import settings


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
    cat_password = models.CharField(max_length=100, verbose_name=_("Cat Password"), default=str(uuid.uuid4())[:8])
    rat_password = models.CharField(max_length=100, verbose_name=_("Rat Password"), default=str(uuid.uuid4())[:8])
    system_password = models.CharField(max_length=100, verbose_name=_("System Password"), default=str(uuid.uuid4())[:8])    
    rat = models.ForeignKey(Project, verbose_name=_("Rat"), null=True, blank=True, related_name="rat")
    won = models.ForeignKey(Project, verbose_name=_("Winner"), null=True, blank=True, related_name="won")
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
        return "Stage: " + str(self.match.stage.number) + " Order: " + str(self.match.order) + " Raund: " + str(self.match.raund)


    def calculate_duration(self):
        return 6000*self.minutes + 100*self.seconds + self.milliseconds

    
@receiver(post_save, sender=SimulationStageMatchResult, dispatch_uid="simulation_winner")
def simulation_stage_match_winner_handler(sender, instance, created, **kwargs):
    stage_matches = SimulationStageMatchResult.objects.filter(match__stage=instance.match.stage)
    results = stage_matches.filter(match__cat=instance.match.cat) | stage_matches.filter(match__rat=instance.match.cat)
    matches = SimulationStageMatch.objects.filter(id__in=results.values_list("match__id", flat=True))
    if results.count() == 2:
        match1 = results[0]
        match2 = results[1]
        if match1.is_cancelled and match2.is_cancelled:
            matches.update(won=None)
        elif match1.is_cancelled and match2.is_caught:
            matches.update(won=match2.match.cat)
        elif match1.is_cancelled and not match2.is_caught:
            matches.update(won=match2.match.rat)
        elif match2.is_cancelled and match1.is_caught:
            matches.update(won=match1.match.cat)
        elif match2.is_cancelled and not match1.is_caught:
            matches.update(won=match1.match.rat)
        elif match1.is_caught and not match2.is_caught:
            matches.update(won=match1.match.cat)
        elif not match1.is_caught and match2.is_caught:
            matches.update(won=match2.match.cat)
        elif match1.is_caught and match2.is_caught:
            match1_time = match1.calculate_duration()
            match2_time = match2.calculate_duration()
            if match1_time > match2_time:
                matches.update(won=match1.match.cat)
            elif match2_time > match1_time:
                matches.update(won=match2.match.cat)
            else:
                secure_random = random.SystemRandom()
                won = secure_random.choice([match1.match.cat, match2.match.cat])
                matches.update(won=won)
        elif not match1.is_caught and not match2.is_caught:
            match1_dist = match1.distance
            match2_dist = match2.distance
            if match1_dist > match2_dist:
                matches.update(won=match2.match.cat)
            elif match2_dist > match1_dist:
                matches.update(won=match1.match.cat)
            else:
                secure_random = random.SystemRandom()
                won = secure_random.choice([match1.match.cat, match2.match.cat])
                matches.update(won=won)
        
@receiver(pre_save, sender=SimulationStage)
def simulation_stage_checker(sender, instance, *args, **kwargs):
    ids = SimulationStageMatch.objects.filter(stage__number=instance.number-1).exclude(won=None).values_list("won", flat=True)
    projects = Project.objects.filter(id__in=ids)
    if projects.count() == 1:
        raise Error("Competition is over. Winner is chosen.")
                
@receiver(post_save, sender=SimulationStage, dispatch_uid="simulation_stage")
def simulation_stage_handler(sender, instance, created, **kwargs):
    from simulation.utils import create_orders, remove_orders
    if instance.create_orders and not instance.remove_orders:
        create_orders(instance.number)
    elif not instance.create_orders and instance.remove_orders:
        remove_orders(instance.number)


@receiver(post_save, sender=SimulationStageMatch, dispatch_uid="simulation_match")
def simulation_match_handler(sender, instance, created, **kwargs):
    if settings.SIMULATION_GAME_ENABLED:
        headers = {"Authorization": "Token " + settings.SIMULATION_TOKEN}
        if instance.cat is None and instance.rat is not None:
            organization = instance.rat.organization
            cat_name = "---"
            rat_name = instance.rat.name
        elif instance.rat is None and instance.cat is not None:
            organization = instance.cat.organization
            cat_name = instance.cat.name
            rat_name = "---"
        elif instance.rat is not None and instance.cat is not None:
            organization = instance.cat.organization
            cat_name = instance.cat.name
            rat_name = instance.rat.name
        data = {
            "organization": organization,
            "order": instance.order,
            "cat_name": cat_name,
            "rat_name": rat_name,
            "cat_password": instance.cat_password,
            "rat_password": instance.rat_password,
            "system_password": instance.system_password,
            "match_id": instance.pk}
        if created:
            url = settings.SIMULATION_GAME_URL + "match/create/"
            r = requests.post(url, headers=headers, data=data)
        else:
            url = settings.SIMULATION_GAME_URL + instance.cat.organization + "/match/" + str(instance.pk) + "/"
            r = requests.patch(url, headers=headers, data=data)

@receiver(post_delete, sender=SimulationStageMatch, dispatch_uid="simulation_match")
def simulation_match_delete_handler(sender, instance, *args, **kwargs):
    if settings.SIMULATION_GAME_ENABLED:
        headers = {"Authorization": "Token " + settings.SIMULATION_TOKEN}
        if instance.cat is None:
            organization = instance.rat.organization
        elif instance.rat is None:
            organization = instance.cat.organization
        elif instance.rat is not None and instance.cat is not None:
            organization = instance.cat.organization
        url = settings.SIMULATION_GAME_URL + organization + "/match/" + str(instance.pk) + "/"
        r = requests.delete(url, headers=headers)


