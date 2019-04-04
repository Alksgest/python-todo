from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from mainapp import views

urlpatterns = [
    path('todos/', views.TodoList.as_view()),
    path('todos/<int:pk>/', views.TodoDetails.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetails.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)