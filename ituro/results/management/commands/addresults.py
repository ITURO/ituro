from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from optparse import make_option
from results.models import InnovativeJuryResult, InnovativeTotalResult, \
    InnovativeJury, Project


class Command(BaseCommand):
    help = 'Calculates the total result.'

    def handle(self, *args, **options):
        number_of_juries = len(InnovativeJury.objects.all())
        for innovative_project in Project.objects.filter(category="innovative", is_confirmed=True):
            total_score = 0
            project = InnovativeJuryResult.objects.filter(project_id = innovative_project.id)

            if len(project) == number_of_juries:
                for result in project:                    
                    total_score += result.jury_score
                total_result = InnovativeTotalResult(project = project[0].project, score = total_score)
                total_result.save()               
            else:              
                try:
                    for total_result in InnovativeTotalResult.objects.all():
                        total_result.delete()
                    break
                except InnovativeTotalResult.DoesNotExist:
                    pass

        for jury in InnovativeJury.objects.all():
            for innovative_project in Project.objects.filter(category="innovative", is_confirmed=True):               
                try:
                    uncertain_project = InnovativeJuryResult.objects.get(project = innovative_project, jury = jury)
                except InnovativeJuryResult.DoesNotExist:
                    print jury.jury + " didn't give a score for " + innovative_project.name

        if len(InnovativeTotalResult.objects.all()) == 0:           
            self.stderr.write("Total results could not be added. There are juries who didn't give a score.")
        else:
            self.stdout.write("Total results are added.")

                

                
                
        
            
