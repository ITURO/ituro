from django.views.generic.edit import CreateView, DeleteView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.conf import settings
from accounts.models import CustomUser
from projects.models import Project, Membership
from projects.forms import ProjectCreateForm, MemberCreateForm


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
        if membership.exists():
            membership.update(is_active=True)
        else:
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
                is_manager=True).exists() or \
            self.get_object().member == self.request.user:
            raise PermissionDenied
        return super(MemberDeleteView, self).dispatch(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(success_url)
