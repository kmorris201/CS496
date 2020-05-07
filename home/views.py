from django.shortcuts import render, get_object_or_404, redirect

# This is the entry view into the app, it redirects users to the 
# correct home page based on their students or teachers group 
# membership

def home(request):

    if request.user.is_authenticated:

        if request.user.groups.filter(name = 'teachers').exists():

            return redirect('home:teacher_home')

        # Defaults to student user after teachers group check
        else:

            return redirect('home:student_home')

    else:

        return redirect('user_extension:login')

# The following views simply redirect the user the their home 
# html page, either student or teacher

def studentHome(request):

    return render(request, 'home/studenthome.html', {})

def teacherHome(request):

    return render(request, 'home/teacherhome.html', {})

