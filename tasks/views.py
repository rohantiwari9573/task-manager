from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import AllowAny

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]   # 👈 no auth for now

    def get_queryset(self):
        queryset = Task.objects.all()   # 👈 REMOVE user filter completely

        completed = self.request.query_params.get('completed')

        if completed is not None:
            if completed.lower() == 'true':
                queryset = queryset.filter(completed=True)
            elif completed.lower() == 'false':
                queryset = queryset.filter(completed=False)

        return queryset

    def perform_create(self, serializer):
        serializer.save()   # 👈 no user assignment