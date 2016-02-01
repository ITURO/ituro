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
from projects.models import Project
from projects.forms import ProjectCreateForm, ProjectUpdateForm, \
    ProjectConfirmForm


class ProjectListView(TemplateView):
    model = Project
    template_name = 'projects/project_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProjectListView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        projects = Project.objects.filter(manager=self.request.user)
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
        project.manager = self.request.user
        project.save()
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
           not settings.PROJECT_UPDATE or not project.manager==self.request.user:
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
           not settings.PROJECT_UPDATE or not project.manager==self.request.user:
            raise PermissionDenied
        return super(ProjectDeleteView, self).dispatch(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.info(request, _("Project deleted."))
        return super(ProjectDeleteView, self).delete(request, *args, **kwargs)


class ProjectDetailView(DetailView):
    model = Project

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        project = self.get_object()
        if not project.manager == self.request.user:
            raise PermissionDenied
        return super(ProjectDetailView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        project = self.get_object()
        update = settings.PROJECT_UPDATE and project.category in \
                 dict(settings.UPDATE_CATEGORIES).keys()
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['UPDATE_PERMISSION'] = update
        return context


class ProjectConfirmView(FormView):
    template_name = "projects/project_confirm.html"
    form_class = ProjectConfirmForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_staff:
            raise PermissionDenied
        return super(ProjectConfirmView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        category = form.cleaned_data.get('category')
        Project.objects.filter(name=name, category=category).update(
            is_confirmed=True)
        messages.success(self.request, _(
            "Project confirmation process completed successfully."))

        project = Project.objects.get(name=name, category=category)
        if project.design:
            messages.info(self.request, _(
                "Project will attend to Autodesk Design Contest."))
        return HttpResponseRedirect(reverse("project_qrcode",
                                                args=(project.id,)))


class ProjectQRCodeView(DetailView):
    model=Project
    template_name="projects/project_qrcode.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_staff:
            raise PermissionDenied
        return super(ProjectQRCodeView, self).dispatch(*args,**kwargs)

    def get_context_data(self, **kwargs):
        project = self.get_object()
        user_qr = project.manager.qrcode
        project_qr = project.qrcode
        context = super(ProjectQRCodeView, self).get_context_data(**kwargs)
        context["user_qr"] = user_qr
        context["project_qr"] = project_qr
        return context
