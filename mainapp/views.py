from django.db import models
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.core.exceptions import ObjectDoesNotExist

from .forms import TodoInputForm
from .models import TodoModel
from .serializers import TodoSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'todos': reverse('todo-list', request=request, format=format)
    })

class RedirectView(FormView):
    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        return HttpResponsePermanentRedirect("/todos/{0}".format(id))


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
            item.title = request.POST.get("title")
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

class TodoDetailsView(FormView):
    template_name = "todoDetails.html"
    errot_template_name = "todoNotFound.html"
    
    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        try:
            data = TodoModel.objects.get(id=id)
        except ObjectDoesNotExist:
             return render(request, self.errot_template_name)

        return render(request, self.template_name, {"data": data})


class TodoList(generics.ListCreateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TodoDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

