from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
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


class VoterPageView(LoginRequiredMixin, ListView):
    model = Voter
    template_name = 'voter.html'
    ordering = ['-pub_date']
    context_object_name = 'voters'


class CreateEvents(LoginRequiredMixin, CreateView):
    model = Event
    template_name = 'newevent.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CreateVoter(LoginRequiredMixin, CreateView):
    model = Voter
    template_name = 'voter.html'
    fields = '__all__'


class VoterDetailView(LoginRequiredMixin, DetailView):
    model = Voter
    template_name = "voter.html"
