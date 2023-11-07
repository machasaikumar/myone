from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from adminapp.models import Drivers

@csrf_exempt
def register_drivers(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            aadhar = request.POST.get('aadhar')
            licience = request.POST.get('licience')
            number = request.POST.get('number')
            shift = request.POST.get('shift')
            drivertype = request.POST.get('drivertype')
            isactive = 1
            createdby = request.POST.get('id')
            Drivers.objects.create(name=name, aadhar=aadhar,  licience=licience, number=number, shift=shift,drivertype=drivertype, isactive=isactive, createdby=createdby)
            response = {'success': 'true', 'message': 'driver details successfully', 'status' : 201}
            return JsonResponse(response)
        except Exception as e:
            # return JsonResponse({'error': str(e)}, status=500)
            response = {'success': 'false', 'message': 'something went wrong', 'status': 500}
            return JsonResponse(response)

def drivers_list(request):
    try:
        drivers = Drivers.objects.all().order_by('-id')
        serialized_drivers = [{'id' : driver.id, 'name': driver.name, 'number': driver.number,'aadhar': driver.aadhar, 'licience' : driver.licience, 'drivertype' : driver.drivertype, 'shift' : driver.shift} for driver in drivers]
        return JsonResponse({'success': 'true', 'drivers': serialized_drivers, 'status':200})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

