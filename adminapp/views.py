from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Supervisor
from django.http import JsonResponse
# from corsheaders.decorators import require_CORS


# from corsheaders.decorators import require_CORS

# @require_CORS

# Create your views here.
@csrf_exempt
def create_supervisor(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            aadhar = request.POST.get('aadhar')
            number = request.POST.get('number')
            isactive = 1
            createdby = request.POST.get('id')
            Supervisor.objects.create(name=name, email=email, password=password, number=number,isactive=isactive, createdby=createdby)
            response = {'success': 'true', 'message': 'supervisor inserted successfully'}
            return JsonResponse(response)
        except Exception as e:
            response = {'success': 'false', 'message': 'something went wrong'}
            return JsonResponse(response)
def list_supervisor(request):
    try:
        supervisors = Supervisor.objects.all().order_by('-id')
        serialized_supervisors = [{'id' : supervisor.id, 'name': supervisor.name, 'email': supervisor.email,'number': supervisor.number} for supervisor in supervisors]
        return JsonResponse({'success': 'true', 'supervisors': serialized_supervisors, 'status':'200'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)



