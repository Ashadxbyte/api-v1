from django.http.response import JsonResponse
import socket, requests

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)


message = f"Your Computer Name is: {hostname}\n Your Computer IP Address is: {IPAddr}"


# Create your views here.
def index(request):

    return JsonResponse({'Hello': 'World'})
