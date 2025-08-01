from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from api.serializers import TodoListSerializer, TodoSerializer, UserSerializer
from lists.models import Todo, TodoList

from django.http import HttpResponse
from django.utils import timezone
import time

class IsCreatorOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `creator` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # If the object doesn't have a creator (i.e. anon) allow all methods.
        if not obj.creator:
            return True

        # Instance must have an attribute named `creator`.
        return obj.creator == request.user


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


class TodoListViewSet(viewsets.ModelViewSet):

    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = (IsCreatorOrReadOnly,)

    def perform_create(self, serializer):
        user = self.request.user
        creator = user if user.is_authenticated else None
        serializer.save(creator=creator)

class TodoViewSet(viewsets.ModelViewSet):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsCreatorOrReadOnly,)

    def perform_create(self, serializer):
        user = self.request.user
        creator = user if user.is_authenticated else None
        serializer.save(creator=creator)


# Add these imports at the top of the file (if not already present)
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.db import connection
from django.db.utils import DatabaseError


# Add these functions at the end of the file
@require_http_methods(["GET"])
def readiness_check(request):
    """
    Readiness probe endpoint - checks if the application is ready to serve traffic
    This includes checking database connectivity
    """
    try:
        # Check database connectivity
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()

        return JsonResponse({
            'status': 'ready',
            'message': 'Application is ready to serve traffic',
            'database': 'connected'
        }, status=200)

    except DatabaseError as e:
        return JsonResponse({
            'status': 'not ready',
            'message': 'Database connection failed',
            'error': str(e)
        }, status=503)

    except Exception as e:
        return JsonResponse({
            'status': 'not ready',
            'message': 'Application is not ready',
            'error': str(e)
        }, status=503)


@require_http_methods(["GET"])
def liveness_check(request):
    """
    Liveness probe endpoint - checks if the application is alive
    This is a simple check that the Django application is responding
    """
    try:
        return JsonResponse({
            'status': 'alive',
            'message': 'Application is alive and responding'
        }, status=200)

    except Exception as e:
        return JsonResponse({
            'status': 'dead',
            'message': 'Application is not responding',
            'error': str(e)
        }, status=500)