from django.urls import path
from .views import (HomePageView,
                    CreateEvents,
                    CreateVoter,
                    VoterPageView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('newevent/', CreateEvents.as_view(), name='newevent'),
    path('voter/', VoterPageView.as_view(), name='voter'),
    path('voter/new', CreateVoter.as_view(), name='newvoter'),

]
