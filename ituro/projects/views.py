from django.views.generic.detail import SingleObjectMixin, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, \
    FormView
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.conf import settings
from accounts.models import CustomUser
from projects.models import Project, Membership
from projects.forms import ProjectCreateForm, ProjectUpdateForm, \
    MemberCreateForm


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
    success_url = "/projects/"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProjectCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        project = form.save(commit=False)
        project.save()

        Membership.objects.create(
            member=self.request.user,
            project=project,
            is_manager=True
        )

        return super(ProjectCreateView, self).form_valid(form)


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectUpdateForm
    template_name = 'projects/project_update.html'
    success_url = '/projects/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_staff and \
           not Membership.objects.filter(
                project=self.get_object(), member=self.request.user,
                is_manager=True).exists():
            raise PermissionDenied
        return super(ProjectUpdateView, self).dispatch(*args, **kwargs)


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = "/projects/"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_staff and \
           not Membership.objects.filter(
                project=self.get_object(), member=self.request.user,
                is_manager=True).exists():
            raise PermissionDenied
        return super(ProjectDeleteView, self).dispatch(*args, **kwargs)


class ProjectDetailView(DetailView):
    model = Project

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_staff and \
           not Membership.objects.filter(
               project=self.get_object(), member=sefl.request.user).exists():
            raise PermissionDenied
        return super(ProjectDetailView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        team = Membership.objects.filter(project=self.get_object())
        is_manager = team.get(member=self.request.user).is_manager
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['team'] = team
        context['is_manager'] = is_manager
        return context

class MemberCreateView(FormView):
    template_name = "projects/member_create.html"
    form_class = MemberCreateForm
    success_url = "/projects/"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        pk = int(self.kwargs.get("pk"))
        membership = Membership.objects.filter(
            member__pk=self.request.user.pk, project__pk=pk, is_manager=True)
        if not membership.exists():
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
        return super(MemberCreateView, self).form_valid(form)


class MemberDeleteView(DeleteView):
    model = Membership
    template_name = "projects/member_delete.html"
    success_url = "/projects/"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.get_queryset().filter(
                member__email=self.request.user.email,
                is_manager=True).exists() or self.get_object().is_manager:
            raise PermissionDenied
        return super(MemberDeleteView, self).dispatch(*args, **kwargs)
