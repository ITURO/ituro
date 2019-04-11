from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, \
    FormView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.shortcuts import redirect
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
        category = form.instance.category
        project.manager = self.request.user
        manager_projects = Project.objects.filter(manager=project.manager,
                                                    category=category)
        if category in ("line_follower", "line_follower_junior") and \
            manager_projects.exists():
            messages.error(self.request,
                _("You can not have more than 1 project in Line Follower categories."))
            return HttpResponseRedirect(reverse("project_create"))
        else:
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
           not settings.PROJECT_UPDATE or project.is_confirmed or \
           not project.manager==self.request.user:
            raise PermissionDenied
        return super(ProjectUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        messages.info(self.request, _(
            "You have updated the project successfully."))
        return super(ProjectUpdateView,self).form_valid(form)

    def get_success_url(self):
        return reverse("project_list")


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('project_list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        project = self.get_object()
        if not project.category in dict(settings.UPDATE_CATEGORIES).keys() or \
           not settings.PROJECT_UPDATE or \
           not project.manager==self.request.user:
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
        if category in ("line_follower", "line_follower_junior", "micro_sumo"):
            return HttpResponseRedirect(
                reverse("qrcode_detail", args=(project.id,)))
        return redirect(reverse("project_confirm"))


class QRCodeDetailView(DetailView):
    model=Project
    template_name="projects/qrcode_detail.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_staff:
            raise PermissionDenied
        return super(QRCodeDetailView, self).dispatch(*args,**kwargs)

    def get_context_data(self, **kwargs):
        project = self.get_object()
        user_qr = project.manager.qrcode
        project_qr = project.qrcode
        context = super(QRCodeDetailView, self).get_context_data(**kwargs)
        context["user_qr"] = user_qr
        context["project_qr"] = project_qr
        return context
