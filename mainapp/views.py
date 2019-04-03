from django.db import models
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.views.generic import FormView, TemplateView

from .forms import TodoInputForm
from .models import TodoModel


class AddTodoView(FormView):
    template_name = "addTodo.html"
    form_class = TodoInputForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial = self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            item = TodoModel()
            item.date = request.POST.get("date")
            item.content = request.POST.get("content")
            item.save()
            # d = request.POST.get("date")
            # c = request.POST.get("content")
            # TodoModel.objects.create(date=d, content=c)
            return HttpResponsePermanentRedirect("/")
        
        return HttpResponse("not success.(")


class HomeView(FormView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        #data = TodoModel.objeсts.all()
        # data = {
        #     "data" : [TodoModel(), TodoModel()]
        # }
        # data = { 
        #     "data" : TodoModel.objects.all()
        # }
       # data = TodoModel.objects.order_by('date')
        data = TodoModel.objects.all()
        
        return render(request, self.template_name, {"data" : data})
