from django.shortcuts import render

from django.views.generic import TemplateView, FormView
from django.http import HttpResponse
from .forms import TodoInputForm
from .models import TodoModel
from django.db import models

class AddTodoView(FormView):
    template_name = "addTodo.html"
    form_class = TodoInputForm

    def get(self, request):
        form = self.form_class(initial = self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponse("succses")
        
        return HttpResponse("not success.(")

class HomeView(FormView):
    template_name = "index.html"

    def get(self, request):
        data = TodoModel.fiel.all()
        return render(request, self.template_name, context=data)
