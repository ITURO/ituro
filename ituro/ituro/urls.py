from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import get_language

urlpatterns = patterns(

    '',
    url(r'^$', 'content_management.views.HomepageRedirect', name="site-homepage"),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),

)

urlpatterns += i18n_patterns(
    '',
    url(r'^core/$', RedirectView.as_view(
        url=reverse_lazy('project_list')), name='homepage'),
    url(r'^core/accounts/', include('accounts.urls')),
    url(r'^core/lcd/', include('lcd.urls')),
    url(r'^core/orders/', include('orders.urls')),
    url(r'^core/projects/', include('projects.urls')),
    url(r'^core/referee/', include('referee.urls')),
    url(r'^core/results/', include('results.urls')),
    url(r'^', include('content_management.urls')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
