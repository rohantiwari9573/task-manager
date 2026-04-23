from django.urls import path
from .views import TaskListCreateView, TaskDetailView, register_user

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view()),
    path('tasks/<int:pk>/', TaskDetailView.as_view()),
    path('register/', register_user),

  
]