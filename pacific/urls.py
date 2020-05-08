from django.urls import path
from .views import (HomePageView,
                    CreateEvents,
                    CreateVoter)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('newevent/', CreateEvents.as_view(), name='newevent'),
    path('newvoter/', CreateVoter.as_view(), name='newvoter'),
]
