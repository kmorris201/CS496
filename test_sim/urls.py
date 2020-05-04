from django.urls import path

from . import views

app_name = "test_sim"

urlpatterns = [
        path('', views.test_sim, name = "test_sim"),
        path('linearresource/<int:instance_id>', views.makeLineResource, name = "make_line_resource"),
        ]
