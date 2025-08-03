from django.urls import path
from .views import readiness, liveness

urlpatterns = [
    path("readiness", readiness, name="readiness"),
    path("liveness", liveness, name="liveness"),
]
