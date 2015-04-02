from django.views.generic.detail import SingleObjectMixin, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, \
    FormView
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from accounts.models import CustomUser
from projects.models import Project, Membership
from projects.forms import ProjectCreateForm, ProjectUpdateForm, \
    ProjectConfirmForm, MemberCreateForm


class ProjectListView(TemplateView):
    model = Project
    template_name = 'projects/project_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProjectListView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        ms = Membership.objects.filter(member=self.request.user)
        projects = list()
        for m in ms:
            projects.append(m.project)
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context['projects'] = projects
        return context


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = 'projects/project_create.html'
    success_url = reverse_lazy('project_list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not settings.PROJECT_CREATE:
            raise PermissionDenied
        return super(ProjectCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        project = form.save(commit=False)
        project.save()

        Membership.objects.create(
            member=self.request.user,
            project=project,
            is_manager=True
        )

        messages.success(self.request, _(
            "You have created a project successfully."))
        return super(ProjectCreateView, self).form_valid(form)


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectUpdateForm
    template_name = 'projects/project_update.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        project = self.get_object()
        if not project.category in dict(settings.UPDATE_CATEGORIES).keys() or \
           not settings.PROJECT_UPDATE or not Membership.objects.filter(
               project=project, member=self.request.user,
               is_manager=True).exists():
            raise PermissionDenied
        return super(ProjectUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.info(self.request, _(
            "You have updated the project successfully."))
        return super(ProjectUpdateView, self).form_valid(form)


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('project_list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        project = self.get_object()
        if not project.category in dict(settings.UPDATE_CATEGORIES).keys() or \
           not settings.PROJECT_UPDATE or not Membership.objects.filter(
               project=project, member=self.request.user,
               is_manager=True).exists():
            raise PermissionDenied
        return super(ProjectDeleteView, self).dispatch(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.info(request, _("Project deleted."))
        return super(ProjectDeleteView, self).delete(request, *args, **kwargs)


class ProjectDetailView(DetailView):
    model = Project

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not Membership.objects.filter(
               project=self.get_object(), member=self.request.user).exists():
            raise PermissionDenied
        return super(ProjectDetailView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        project = self.get_object()
        team = Membership.objects.filter(project=project)
        is_manager = team.get(member=self.request.user).is_manager
        update = settings.PROJECT_UPDATE and project.category in \
                 dict(settings.UPDATE_CATEGORIES).keys()
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['team'] = team
        context['is_manager'] = is_manager
        context['UPDATE_PERMISSION'] = update
        return context


class ProjectConfirmView(FormView):
    template_name = "projects/project_confirm.html"
    form_class = ProjectConfirmForm
    success_url = reverse_lazy("project_confirm")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_staff:
            raise PermissionDenied
        return super(ProjectConfirmView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        category = form.cleaned_data.get('category')
        project = Project.objects.filter(name=name, category=category).update(
            is_confirmed=True)
        messages.success(self.request, _(
            "Project confirmation process completed successfully."))
        return super(ProjectConfirmView, self).form_valid(form)


class MemberCreateView(FormView):
    template_name = "projects/member_create.html"
    form_class = MemberCreateForm

    def get_success_url(self):
        return reverse('project_detail', args=[self.kwargs.get('pk')])

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs.get("pk"))
        is_manager = Membership.objects.filter(
            member__pk=self.request.user.pk, project=project, is_manager=True
        ).exists()
        if not is_manager or not settings.PROJECT_UPDATE or \
           not project.category in dict(settings.UPDATE_CATEGORIES).keys():
            raise PermissionDenied
        return super(MemberCreateView, self).dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(MemberCreateView, self).get_form_kwargs()
        kwargs.update({'project_pk': self.kwargs.get('pk')})
        return kwargs

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        pk = int(self.kwargs.get('pk'))
        membership = Membership.objects.filter(
            project__pk=pk, member__email=email)
        project = Project.objects.get(pk=pk)
        member = CustomUser.objects.get(email=email)
        Membership.objects.create(project=project, member=member)
        messages.success(self.request, _("New member added to project."))
        return super(MemberCreateView, self).form_valid(form)


class MemberDeleteView(DeleteView):
    model = Membership
    template_name = "projects/member_delete.html"
    success_url = "/projects/"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        project = self.get_object().project
        if not project.category in dict(settings.UPDATE_CATEGORIES) or \
           not settings.PROJECT_UPDATE or not self.get_queryset().filter(
               member__email=self.request.user.email,
               is_manager=True).exists() or self.get_object().is_manager:
            raise PermissionDenied
        return super(MemberDeleteView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MemberDeleteView, self).get_context_data(**kwargs)
        context['project'] = self.get_object().project.name
        context['member'] = self.get_object().member.email
        return context


    def delete(self, request, *args, **kwargs):
        messages.info(request, _("Member deleted successfully."))
        return super(MemberDeleteView, self).delete(request, *args, **kwargs)
