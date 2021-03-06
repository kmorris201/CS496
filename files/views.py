# TODO: Not all of these imports are necessary and should be optimized
# in the future
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.models import User
from test_sim.models import TestSim, TestSimResource 
from lab_repo.models import LabDraft, LabTemplate
import datetime
import random
import os

# This method directs the user to the approriate view for their group 
# membership either teachers or students
def files(request):

    if request.user.is_authenticated:

        if request.user.groups.filter(name='teachers').exists():

            return redirect('files:teacher_display')

        # If the user is not a teacher, they must be a student user, so
        # the view defaults to student display
        else:

            return redirect('files:student_display')

    else:

        return redirect('user_extension:login')

def teacherDisplay(request):

    user = get_object_or_404(User, username = request.user.username)

    # All objects that could be displayed for the user are queried here
    # and passed to the template so that the template will be able to 
    # determine if there are any files to display for each section
    testsim = TestSim.objects.filter(user=user)

    testsimresource = TestSimResource.objects.filter(user=user)

    drafts = LabDraft.objects.filter(user=user)

    templates = LabTemplate.objects.filter(user=user)

    return render(request, 'files/teacherdisplay.html', {'testsim':testsim, 'testsimresource':testsimresource, 'drafts':drafts, 'templates':templates})
    
def studentDisplay(request):

    user = get_object_or_404(User, username = request.user.username)

    # All objects that could be displayed for the user are queried here and
    # passed to the template so that the template will be able to determine if
    # there are any files to display for each section
    testsim = TestSim.objects.filter(user=user)

    testsimresource = TestSimResource.objects.filter(user=user)

    return render(request, 'files/studentdisplay.html', {'testsim':testsim, 'testsimresource':testsimresource})

# The rest of the views follow a similar pattern. Each object type which could
# be displayed or deleted has a json and delete view. The json view passes back
# the objects query in json form while delete deletes the model instance and 
# all files associated with it in the file system.

# Currently the objects with methods are: testSim, testSimResource, labDraft,
# and labTemplate

def testSimJson(request):

    if request.user.is_authenticated:
        
        user = get_object_or_404(User, username = request.user.username)

        data = serializers.serialize('json', TestSim.objects.filter(user=user))

        return JsonResponse(data, safe = False)

    else:

        return redirect('files:files') 

def testSimDelete(request, instance_id):
    
    instance = get_object_or_404(TestSim, id = instance_id)

    path = "/wku_sims/static/media" + str(instance.csv)

    instance.delete()

    os.remove(path)

    return redirect('files:files')

def testSimResourceJson(request):

    if request.user.is_authenticated:
        
        user = get_object_or_404(User, username = request.user.username)

        data = serializers.serialize('json', TestSimResource.objects.filter(user=user))

        return JsonResponse(data, safe = False)

    else:

        return redirect('files:files') 

def testSimResourceDelete(request, instance_id):
    
    instance = get_object_or_404(TestSimResource, id = instance_id)

    path = "/wku_sims/static/media" + str(instance.resource)

    instance.delete()

    os.remove(path)

    return redirect('files:files')

def labDraftJson(request):

    if request.user.is_authenticated:
        
        user = get_object_or_404(User, username = request.user.username)

        data = serializers.serialize('json', LabDraft.objects.filter(user=user))
        return JsonResponse(data, safe = False)

    else:

        return redirect('files:files') 

def labDraftDelete(request, instance_id):
    
    instance = get_object_or_404(LabDraft, id = instance_id)

    path = "/wku_sims/static/media" + str(instance.draft)

    instance.delete()

    os.remove(path)

    return redirect('files:files')

def labTemplateJson(request):

    if request.user.is_authenticated:
        
        user = get_object_or_404(User, username = request.user.username)

        data = serializers.serialize('json', LabTemplate.objects.filter(user=user))
        return JsonResponse(data, safe = False)

    else:

        return redirect('files:files') 

def labTemplateDelete(request, instance_id):
    
    instance = get_object_or_404(LabTemplate, id = instance_id)

    path = "/wku_sims/static/media" + str(instance.template)

    instance.delete()

    os.remove(path)

    return redirect('files:files')
