from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


def home(request):
    return JsonResponse({
        "message": "Task Manager API",
        "endpoints": [
            "/api/tasks/",
            "/api/token/",
            "/swagger/"
        ]
    })


schema_view = get_schema_view(
    openapi.Info(
        title="Task Manager API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),

    path('api/', include('tasks.urls')),

    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
]