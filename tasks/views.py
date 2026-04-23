from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.models import User
import traceback

from .models import Task
from .serializers import TaskSerializer, RegisterSerializer


# =========================
# USER REGISTRATION API
# =========================
@swagger_auto_schema(
    method='post',
    request_body=RegisterSerializer
)
@api_view(['POST'])
def register_user(request):
    try:
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            if User.objects.filter(username=username).exists():
                return Response(
                    {"error": "User already exists"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            User.objects.create_user(username=username, password=password)

            return Response(
                {"message": "User created successfully"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({
            "error": str(e),
            "trace": traceback.format_exc()
        }, status=500)


# =========================
# LIST + CREATE TASKS
# =========================
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # 🔥 FIX: prevent AnonymousUser crash
        if user.is_anonymous:
            return Task.objects.none()

        queryset = Task.objects.filter(user=user)

        # Filter by completed
        completed = self.request.query_params.get('completed')
        if completed is not None:
            if completed.lower() == 'true':
                queryset = queryset.filter(completed=True)
            elif completed.lower() == 'false':
                queryset = queryset.filter(completed=False)

        # Search by title
        title = self.request.query_params.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# =========================
# RETRIEVE + UPDATE + DELETE
# =========================
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # 🔥 FIX: prevent AnonymousUser crash
        if user.is_anonymous:
            return Task.objects.none()

        return Task.objects.filter(user=user)