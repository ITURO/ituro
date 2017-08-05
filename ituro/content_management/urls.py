from django.conf.urls import patterns, url
from content_management.views import set_language, GalleryDetailView

urlpatterns = patterns(
    '',
    url(r'^set_language/$', set_language, name="set_language"),
    url(r'^gallery/(?P<slug>[-_\w]+)/$', GalleryDetailView.as_view(),
        name="gallery_detail"),
)
