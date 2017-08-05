from django.conf.urls import patterns, url, include
from content_management.views import set_language, GalleryDetailView
from django.utils.translation import ugettext_lazy as _

urlpatterns = patterns(
    '',
    url(r'^set_language/$', set_language, name="set_language"),
    url(_(r'^gallery/(?P<slug>[-_\w]+)/$'), GalleryDetailView.as_view(),
        name="gallery_detail"),
    url(_(r'^survey/'), include("survey.urls", namespace="survey")),
)
