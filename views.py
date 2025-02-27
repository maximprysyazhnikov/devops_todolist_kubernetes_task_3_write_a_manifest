from django.http import JsonResponse

def readiness(request):
    """Ендпоінт для readiness probe"""
    return JsonResponse({"status": "ready"})

def liveness(request):
    """Ендпоінт для liveness probe"""
    return JsonResponse({"status": "alive"})
