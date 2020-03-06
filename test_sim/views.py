from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import InputForm
from .models import TestSim

import math

'''
Change this functions name to the name of your experiment. 
'''
def test_sim (request):

    if request.user.is_authenticated:
        user = get_object_or_404(User, username = request.user.username)

        if request.method == 'POST':

            form = InputForm(request.POST)

            if form.is_valid():

                loop_radius = form.cleaned_data['loop_radius']
                b_zero = form.cleaned_data['loop_radius']
                f = form.cleaned_data['f']
                r = form.cleaned_data['r']
                seconds = form.cleaned_data['seconds']

                input_string = '"loop_radius,b_zero,f,r,seconds"\n"' + str(loop_radius) +','+str(b_zero)+','+str(f)+','+str(r)+','+str(seconds)+'"\n'

                csv_string ='"a,b,t"\n'

                for t in range (1, seconds + 1, 1):

                    b = b_zero*math.sin(math.radians(2*math.pi*f*t))
                    a = (2*(math.pi**2)*(loop_radius**2)*b_zero*
                            math.cos(math.radians(2*math.pi*f*t)))/r

                    next_line = '"'+str(a)+','+str(b)+','+str(t)+'"\n'

                    csv_string = csv_string + next_line

                count = TestSim.objects.filter(user = user).count() + 1

                file_name = '/home/caleb/Documents/CS496/static/media/csv/testsim' + request.user.username + str(count)
                media_path = '/csv/testsim' + request.user.username + str(count)

                csv = open(file_name, 'w+')
                csv.write(csv_string)
                    
                testsim = TestSim(user = user, inputs = input_string, csv = media_path)
                testsim.save()

                form = InputForm()

                return render(request, 'test_sim/test_sim.html', {'form':form,'csv_string': csv_string})

            else:

                form = InputForm()
                return render(request, 'test_sim/test_sim.html', {})

        else:

            form = InputForm()
            return render(request, 'test_sim/test_sim.html', {'form':form})

    else:

        return redirect('login')








