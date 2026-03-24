from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated


# LIST + CREATE
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)

        completed = self.request.query_params.get('completed')
        if completed is not None:
            if completed.lower() == 'true':
                queryset = queryset.filter(completed=True)
            elif completed.lower() == 'false':
                queryset = queryset.filter(completed=False)

        title = self.request.query_params.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# RETRIEVE + UPDATE + DELETE
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)