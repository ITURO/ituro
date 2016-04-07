from django.db import models
from django.dispatch import receiver
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.conf import settings
from django.core.exceptions import ValidationError
from accounts.models import CustomUser


@python_2_unicode_compatible
class Project(models.Model):
    manager = models.ForeignKey(CustomUser)
    category = models.CharField(
        verbose_name=_('Category'), max_length=30,
        choices=settings.ALL_CATEGORIES)
    name = models.CharField(verbose_name=_('Project Name'), max_length=50)
    presentation = models.FileField(
        verbose_name=_("Project Presentation File"),
        upload_to='presentations', blank=True)
    is_confirmed = models.BooleanField(
        verbose_name=_('Is project confirmed?'), default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')
        unique_together = (('category', 'name'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project_detail', args=[self.pk])

    def get_presentation_file_name(self):
        return self.presentation.name.split('/')[-1]

    @property
    def results(self):
        RESULTS_DICT = {
            "line_follower": self.linefollowerresult_set,
            "fire_fighter": self.firefighterresult_set,
            "basketball": self.basketballresult_set,
            "stair_climbing": self.stairclimbingresult_set,
            "maze": self.mazeresult_set,
            "color_selecting": self.colorselectingresult_set,
            "self_balancing": self.selfbalancingresult_set,
            "scenario": self.scenarioresult_set,
            "innovative": self.innovativejuryresult_set,
        }
        return RESULTS_DICT[self.category]

    @property
    def qrcode(self):
        return "{}-{}-{}-{}".format(
                self.manager.id,self.created_at.year,self.category,self.id)

    def get_results_count(self):
        return self.results.count()



@receiver(models.signals.pre_delete, sender=Project)
def project_delete_handler(sender, **kwargs):
    project = kwargs.get('instance')
    if project.presentation:
        project.presentation.delete()
