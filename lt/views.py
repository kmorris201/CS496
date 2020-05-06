from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.models import User
from lab_repo.models import LabTemplate 

def labTempDisplay(request):

    if request.user.is_authenticated:

        labtemp = LabTemplate.objects.all()

        return render(request, 'lab_temps/labtempdisplay.html', {'labtemp':labtemp})

    else:

        return redirect('user_extension:login')

def labTempJson(request):

    if request.user.is_authenticated:
        
        data = serializers.serialize('json', LabTemplate.objects.all().order_by('-pk'))

        return JsonResponse(data, safe = False)

    else:

        return redirect('user_extension:login') 
