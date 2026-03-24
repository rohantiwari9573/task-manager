from django.urls import path
from .views import TaskListCreateView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view()),
]