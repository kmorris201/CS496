from django.urls import path

from . import views

app_name = "home"

urlpatterns = [ 
        path('', views.home, name = "home"),
        path('student/', views.studentHome, name = "student_home"),
        path('teacher/', views.teacherHome, name = "teacher_home"),
        ]
