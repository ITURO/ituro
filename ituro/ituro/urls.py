from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView

urlpatterns = patterns(
    '',
    url(r'^$', RedirectView.as_view(
        url=reverse_lazy('project_list')), name='homepage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^projects/', include('projects.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^captcha/', include('captcha.urls')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
