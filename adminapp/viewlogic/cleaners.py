from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from adminapp.models import Cleaners

@csrf_exempt
def register_cleaners(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            aadhar = request.POST.get('aadhar')
            licience = request.POST.get('licience')
            number = request.POST.get('number')
            shift = request.POST.get('shift')
            isactive = 1
            createdby = request.POST.get('id')
            Cleaners.objects.create(name=name, aadhar=aadhar,  licience=licience, number=number, shift=shift, isactive=isactive, createdby=createdby)
            response = {'success': 'true', 'message': 'cleaner details inserted successfully', 'status' : 201}
            return JsonResponse(response)
        except Exception as e:
            # return JsonResponse({'error': str(e)}, status=500)
            response = {'success': 'false', 'message': 'something went wrong', 'status' : 500}
            return JsonResponse(response)

def cleaners_list(request):
    try:
        cleaners = Cleaners.objects.all().order_by('-id')
        serialized_cleaners = [{'id' : cleaner.id, 'name': cleaner.name, 'number': cleaner.number, 'aadhar': cleaner.aadhar, 'licience' : cleaner.licience, 'shift' : cleaner.shift} for cleaner in cleaners]
        return JsonResponse({'success': 'true', 'cleaners': serialized_cleaners, 'status': 200})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)