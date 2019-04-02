from django.shortcuts import render

from django.views.generic import TemplateView, FormView
from .forms import TodoInputForm


class HomeView(FormView):
    template_name = "index.html"
    form_class = TodoInputForm

    