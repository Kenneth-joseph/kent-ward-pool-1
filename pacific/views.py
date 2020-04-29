from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


# Create your views here.
# def home(request):
#     return render(request, 'home')
class HomePageView(TemplateView):
    template_name = 'home.html'
