from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import InputForm, InstanceForm, ResourceTypeForm
from .models import TestSim, TestSimResource

import math
import os, sys
import pandas as pd
import matplotlib.pylab as plt
import numpy as np

def test_sim (request):

    if request.user.is_authenticated:

        user = get_object_or_404(User, username = request.user.username)

        if request.method == 'POST':

            form1 = InputForm(request.POST)
            form2 = InstanceForm(request.POST, user = request.user)
            form3 = ResourceTypeForm(request.POST)

            if form1.is_valid():

                loop_radius = form1.cleaned_data['loop_radius']
                b_zero = form1.cleaned_data['loop_radius']
                f = form1.cleaned_data['f']
                r = form1.cleaned_data['r']
                seconds = form1.cleaned_data['seconds']

                csv_string ='a,b,t\n'

                for t in range (1, seconds + 1, 1):

                    b = b_zero*math.sin(math.radians(2*math.pi*f*t))
                    a = (2*(math.pi**2)*(loop_radius**2)*b_zero*
                            math.cos(math.radians(2*math.pi*f*t)))/r

                    next_line = str(a)+','+str(b)+','+str(t)+'\n'

                    csv_string = csv_string + next_line

                count = 1

                file_name = '/wku_sims/static/media/csv/testsim' + request.user.username + str(count)
                media_path = '/csv/testsim' + request.user.username + str(count)
                while os.path.exists(file_name):

                    count = count + 1

                    file_name = '/wku_sims/static/media/csv/testsim' + request.user.username + str(count)
                    media_path = '/csv/testsim' + request.user.username + str(count)

                csv = open(file_name, 'w+')
                csv.write(csv_string)
                    
                testsim = TestSim(user = user, loop_radius = loop_radius, b_zero = b_zero, f = f, r = r, seconds = seconds , csv = media_path)
                testsim.save()

                pk = testsim.pk

                form1 = InputForm()
                form2 = InstanceForm(user = request.user)
                form3 = ResourceTypeForm()

                return render(request, 'test_sim/test_sim.html', {'form1':form1,'form2':form2, 'form3':form3, 'csv':media_path, 'pk':pk, 'loop_radius':loop_radius,'b_zero':b_zero,'f':f,'r':r,'seconds':seconds})

            elif form2.is_valid():

                selection = form2.cleaned_data['selection']

                loop_radius = getattr(selection,'loop_radius')
                b_zero = getattr(selection,'b_zero')
                f = getattr(selection,'f')
                r = getattr(selection,'r')
                seconds = getattr(selection,'seconds')
                csv = getattr(selection,'csv')
                pk = getattr(selection,'pk')

                form1 = InputForm()
                form2 = InstanceForm(user = request.user)
                form3 = ResourceTypeForm()

                return render(request, 'test_sim/test_sim.html', {'form1':form1,'form2':form2, 'form3':form3, 'csv':csv, 'pk':pk, 'loop_radius':loop_radius,'b_zero':b_zero,'f':f,'r':r,'seconds':seconds})

            elif form3.is_valid():

                res_type = form3.cleaned_data['res_type']

                pk = form3.cleaned_data['pk']

                if(res_type == 'line'):

                    return redirect('test_sim:make_line_resource', pk)

                else:

                    return redirect('test_sim:test_sim')

            else:

                form1 = InputForm()
                form2 = InstanceForm(user = request.user)
                form3 = ResourceTypeForm()

                return render(request, 'test_sim/test_sim.html', {'form1':form1,'form2':form2, 'form3':form3})

        else:

            form1 = InputForm()
            form2 = InstanceForm(user = request.user)
            form3 = ResourceTypeForm()

            return render(request, 'test_sim/test_sim.html', {'form1':form1,'form2':form2, 'form3':form3})

    else:

        return redirect('user_extension:login')

def makeLineResource(request, instance_id):

    if request.user.is_authenticated:

        user = get_object_or_404(User, username = request.user.username)
        csv = get_object_or_404(TestSim, id = instance_id)
        
        count = 1 

        file_path = '/wku_sims/static/media/resources/testsimresources' + request.user.username + str(count) + '.png'
        media_path = '/resources/testsimresources' + request.user.username + str(count) + '.png'

        while os.path.exists(file_path):

            count = count + 1

            file_path = '/wku_sims/static/media/resources/testsimresources' + request.user.username + str(count) + '.png'
            media_path = '/resources/testsimresources' + request.user.username + str(count) + '.png'

        csv_file_path = '/wku_sims/static/media' + str(csv.csv)

        df = pd.read_csv(csv_file_path)

        df = df.set_index("t")

        df.plot(title="A and B Over Time")

        plt.xlabel("Time in Seconds")

        plt.savefig(file_path)

        testsimresource = TestSimResource(user = user, res_type = "line", resource = media_path) 

        testsimresource.save()

        csv_path = csv.csv
        pk = csv.pk
        loop_radius = csv.loop_radius
        b_zero = csv.b_zero
        f = csv.f
        r = csv.r
        seconds = csv.seconds

        form1 = InputForm()
        form2 = InstanceForm(user = request.user)
        form3 = ResourceTypeForm()

        return render(request, 'test_sim/test_sim.html', {'form1':form1,'form2':form2, 'form3':form3, 'csv':csv_path, 'pk':pk, 'loop_radius':loop_radius,'b_zero':b_zero,'f':f,'r':r,'seconds':seconds})

  


 
        











