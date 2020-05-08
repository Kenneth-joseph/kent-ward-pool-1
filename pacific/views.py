from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView)
from django.http import HttpResponse
from .models import Event, Voter


# Create your views here.
# def home(request):
#     return render(request, 'home')
class HomePageView(ListView):
    model = Event
    template_name = 'home.html'
    ordering = ['-pub_date']
    context_object_name = 'events'


class CreateEvents(CreateView):
    model = Event
    template_name = 'newevent.html'
    fields = ['title', 'content']


class CreateVoter(CreateView):
    model = Voter
    template_name = 'home.html'
    fields = '__all__'


class DetailView(DetailView):
    model = Voter
    template_name = "home.html"
