from django.urls import path
from . import views

app_name = "lab_repo"

urlpatterns = [
        path('',views.draft_start, name = 'draft_start'),
        path('draftedit/',views.draft_edit, name = 'draft_edit'),
        path('draftdelete/',views.draft_delete, name = 'draft_delete'),
        path('elementdelete/<int:pk>/',views.element_delete, name = 'element_delete'),
        ]
