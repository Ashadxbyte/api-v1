from django.http.response import JsonResponse


# Create your views here.
def index(request):
    return JsonResponse({'Hello': 'World'})
