from django.urls import path

from . import views

app_name = "files"

urlpatterns = [ 
        path('', views.files, name = "files"),
        path('studentdisplay/', views.studentDisplay, name = "student_display"),
        path('teacherdisplay/', views.teacherDisplay, name = "teacher_display"),
        path('testsimjson/', views.testSimJson, name = "testsim_json"),
        path('testsimdelete/<int:instance_id>/', views.testSimDelete, name = "testsim_delete"),
        path('testsimresourcejson/', views.testSimResourceJson, name = "testsimresource_json"),
        path('testsimresourcedelete/<int:instance_id>/', views.testSimResourceDelete, name = "testsimresource_delete"),
        ]

