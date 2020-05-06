from django.urls import path

from . import views

app_name = "lab_temps"

urlpatterns = [ 
        path('', views.labTempDisplay, name = "labtempdisplay"),
        path('labtempjson/', views.labTempJson, name = "labtempjson"),
        ]

