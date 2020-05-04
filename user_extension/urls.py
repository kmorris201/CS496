from django.urls import path

from . import views

app_name = 'user_extension'

urlpatterns = [
        path('studentregistration/', views.studentRegistration, name='student_registration'),
        path('login/', views.login, name='login'),
        path('logoff/', views.logoff, name='logoff'),
        ]
