from simulation.models import SimulationStage, SimulationStageMatch
from projects.models import Project
import random


def create_orders(stage_number):
    stage = SimulationStage.objects.get(number=stage_number)
    if stage_number == 1:
        query = list(Project.objects.filter(category="simulation", is_confirmed=True))
        if len(query) %2 == 1:
            query.insert(0, None)
        for i in range(len(query)/2):
                secure_random = random.SystemRandom()
                cat = secure_random.choice(query)
                query.remove(cat)
                rat = secure_random.choice(query)
                query.remove(rat)
                SimulationStageMatch.objects.create(
                    stage=stage,
                    order=2*i+1,
                    raund=1,
                    cat=cat,
                    rat=rat)
                SimulationStageMatch.objects.create(
                    stage=stage,
                    order=2*i+2,
                    raund=2,
                    cat=rat,
                    rat=cat)
    else:
        previous_stage = SimulationStage.objects.get(number=stage_number-1)
        query = SimulationStageMatch.objects.filter(stage=previous_stage).exclude(won=None).values_list("won", flat=True)
        winners = list(Project.objects.filter(id__in=query))
        if len(winners) %2 == 1:
            winners.insert(0, None)
        for i in range(len(winners)/2):
                secure_random = random.SystemRandom()
                cat = secure_random.choice(winners)
                winners.remove(cat)
                rat = secure_random.choice(winners)
                winners.remove(rat)
                SimulationStageMatch.objects.create(
                    stage=stage,
                    order=2*i+1,
                    raund=1,
                    cat=cat,
                    rat=rat)
                SimulationStageMatch.objects.create(
                    stage=stage,
                    order=2*i+2,
                    raund=2,
                    cat=rat,
                    rat=cat)

def remove_orders(stage_number):
    stage = SimulationStage.objects.get(number=stage_number)
    SimulationStageMatch.objects.filter(stage__number=stage_number).delete()