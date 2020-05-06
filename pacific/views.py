from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.http import HttpResponse
from .models import Event,Voter


# Create your views here.
# def home(request):
#     return render(request, 'home')
class HomePageView(ListView):
    model= Event
    template_name = 'home.html'
    ordering = ['-pub_date']

