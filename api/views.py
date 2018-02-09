from django.views.generic.edit import FormView
from django.views.generic import TemplateView

from .forms import TextForm


class MainView(FormView):
    form_class = TextForm
    template_name = 'main.html'


class AllView(TemplateView):
    template_name = 'all.html'
