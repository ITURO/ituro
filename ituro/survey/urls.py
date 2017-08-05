from django.conf.urls import url
from survey.views import SurveyCreateView

urlpatterns = [
    url(r'^(?P<slug>[-_\w]+)/$', SurveyCreateView.as_view(),
        name="survey_create"),
]
