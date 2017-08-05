from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from survey.forms import SurveyForm
from survey.models import Survey, TextQuestion, TextAreaQuestion, \
    ChoiceQuestion, Choice
from django.contrib import messages
from django.utils.translation import ugettext as _


class SurveyCreateView(UpdateView):
    model = Survey
    form_class = SurveyForm
    template_name = "content_management/survey/survey_create.html"

    def get_object(self, queryset=None):
        obj = Survey.objects.get(slug=self.kwargs.get("slug"), is_draft=True)
        return obj

    def get_success_url(self):
        slug = self.kwargs.get('slug')
        return reverse_lazy("survey:survey_create", kwargs={'slug': slug})

    def form_valid(self, form):
        participant = form['participant'].value()
        field_count = len(form.fields.items())
        current_survey = self.get_object()
        form.instance.participant = current_survey.participant
        if not participant == '':
            survey = Survey.objects.create(
                title=current_survey.title,
                description=current_survey.description,
                language=current_survey.language,
                participant=participant
            )
            for i in range(1, field_count):
                widget = form.fields.items()[i][1].widget
                widget_type = widget.__class__.__name__
                key = form.fields.items()[i][0]
                val = form[key].value()
                if widget_type == 'TextInput':
                    TextQuestion.objects.create(question=key, answer=val,
                                                survey=survey)
                elif widget_type == 'Textarea':
                    TextAreaQuestion.objects.create(question=key, answer=val,
                                                    survey=survey)
                elif widget_type == 'CheckboxSelectMultiple':
                    current_choices = form[key].field.choices
                    obj = ChoiceQuestion.objects.create(question=key,
                                                        survey=survey)
                    for choice in current_choices:
                        choice = Choice.objects.get(answer=choice[0])
                        obj.choices.add(choice)
                    for value in val:
                        answer = Choice.objects.get(answer=value)
                        obj.answers.add(answer)
                elif widget_type == 'Select':
                    current_choices = form[key].field.choices
                    obj = ChoiceQuestion.objects.create(question=key,
                                                        survey=survey)
                    for choice in current_choices:
                        choice = Choice.objects.get(answer=choice[0])
                        obj.choices.add(choice)
                    answer = Choice.objects.get(answer=val)
                    obj.answers.add(answer)
        messages.success(self.request, _("Saved successfully!"))
        return super(SurveyCreateView, self).form_valid(form)
