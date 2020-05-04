from django.shortcuts import render, get_object_or_404, redirect

def home(request):

    if request.user.is_authenticated:

        if request.user.groups.filter(name = 'teachers').exists():

            return redirect('home:teacher_home')

        else:

            return redirect('home:student_home')

    else:

        return redirect('user_extension:login')

def studentHome(request):

    return render(request, 'home/studenthome.html', {})

def teacherHome(request):

    return render(request, 'home/teacherhome.html', {})

