from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from mainapp import views

urlpatterns = [
    path('api/', views.api_root),
    path('api/todos/', views.TodoList.as_view(), name='todo-list'),
    path('api/todos/<int:pk>/', views.TodoDetails.as_view(), name='todo-detail'),
    path('api/users/', views.UserList.as_view(), name='user-list'),
    path('api/users/<int:pk>', views.UserDetails.as_view(), name='user-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)