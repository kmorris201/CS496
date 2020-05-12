from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import Group
from . forms import RegistrationForm

# studentRegistration passes the registration form to the 
# student_registartion.html page and on POST creates a user and adds them
# to the student group, which will need to be created upon installation of 
# the website by the admin or through the shell. 

def studentRegistration(request):

    # Check to see if the form has been submitted
    if request.method == 'POST':

        form = RegistrationForm(request.POST)

        # See if the form is vaild
        if form.is_valid():

            # Save the data from the form
            form.save()

            # Get all of the data from the form and put all the data into
            # variables to be used for user creation
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')

            # Create the user
            user = authenticate(username=username, password=raw_password, email=email, first_name=first_name, last_name=last_name)

            # Get the group and put the new student into it
            students = Group.objects.get(name='students')
            students.user_set.add(user)

            # Log the student in and send them to the home page
            login(user)
            return redirect('home:home')

        else:

            form = RegistrationForm()

            return render(request, 'user_extension/registration.html', {'form':form})

    else:

        # No data, so just pass the form back to the html page be filled in 
        form = RegistrationForm()

        return render(request, 'user_extension/registration.html', {'form': form})

# login is just a method that passes the user on to the Django provided
# login system, this method is just for organization so all user related
# url calls are from the user_extension application
def login(request):
    return redirect('/accounts/login/')
    
# This just calls th django provided logout method, here for scoping of the 
# user related urls calls to the user_extension application
def logoff(request):
    logout(request)
    return redirect('/accounts/login/')
