from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        # Authentication successful, generate a token
        token, created = Token.objects.get_or_create(user=user)
        # Send the token back as part of the response
        return JsonResponse({'token': token.key})
    else:
        # Authentication failed
        return JsonResponse({'error': 'Invalid credentials'}, status=400)