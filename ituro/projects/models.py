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
    category = models.CharField(
        verbose_name=_('Category'), max_length=30,
        choices=settings.ALL_CATEGORIES)
    name = models.CharField(verbose_name=_('Project Name'), max_length=50)
    presentation = models.FileField(
        verbose_name=_("Project Presentation File"),
        upload_to='presentations', blank=True)
    design = models.BooleanField(
        verbose_name=_('I want to join Autodesk Digital Design Contest.'),
        default=False)
    is_valid = models.BooleanField(
        verbose_name=_('Is project valid?'), default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')
        unique_together = (('category', 'name'),)

    def __str__(self):
        return self.name

    def get_absoulte_url(self):
        return reverse('project_detail', args=[self.pk])


    def get_presentation_file_name(self):
        return self.presentation.name.split('/')[-1]


@python_2_unicode_compatible
class Membership(models.Model):
    member = models.ForeignKey(CustomUser, verbose_name=_('User'))
    project = models.ForeignKey(Project, verbose_name=_('Project'))
    is_manager = models.BooleanField(
        verbose_name=_('Is project manager?'), default=False)

    class Meta:
        unique_together = (("member", "project"),)

    def __str__(self):
        return self.member.email

    def clean(self):
        if self.is_manager:
            members = self.__class__.objects.filter(
                project=self.project).exclude(member=self.member).update(
                    is_manager=False)


@receiver(models.signals.pre_delete, sender=Project)
def project_delete_handler(sender, **kwargs):
    project = kwargs.get('instance')
    Membership.objects.delete(project=project)
    project.presentation.file.delete()
