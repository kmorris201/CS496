from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Count
from django.views.generic import UpdateView, ListView, CreateView

def home(request):
    return render(request, 'home.html')
