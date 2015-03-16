from django.db import models
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
    name = models.CharField(
        verbose_name=_('Project Name'), max_length=50)
    description = models.TextField(verbose_name='Project Description')
    is_valid = models.BooleanField(
        verbose_name='Is project valid?', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(
        verbose_name=_('Is project active?'), default=True)

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return self.name

    def clean(self):
        if self.is_active:
            existing = self.__class__.objects.exclude(id=self.id).filter(
                name=self.name, category=self.category, is_active=True).count()
            if existing > 0:
                raise ValidationError(_("Project exists."))


@python_2_unicode_compatible
class Membership(models.Model):
    member = models.ForeignKey(CustomUser, verbose_name=_('User'))
    project = models.ForeignKey(Project, verbose_name=_('Project'))
    is_manager = models.BooleanField(
        verbose_name=_('Is project manager?'), default=False)
    is_active = models.BooleanField(
        verbose_name=_('Is project membership active?'), default=True)

    class Meta:
        unique_together = (("member", "project"),)

    def __str__(self):
        return self.member.email

    def clean(self):
        if self.is_manager and self.is_active:
            members = self.__class__.objects.filter(
                project=self.project).exclude(member=self.member).update(
                    is_manager=False)
        elif self.is_manager and not self.is_active:
            raise ValidationError(_("Manager cannot be deleted."))
