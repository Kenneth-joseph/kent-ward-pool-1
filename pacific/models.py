from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Voter(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    national_id = models.IntegerField(default=0)
    phone_number = models.IntegerField(default=0)
    ward = models.CharField(max_length=30)
    polling_station = models.CharField(max_length=30, default='gwasi')
    pub_date = models.DateTimeField(auto_now_add=True)

    # def number_of_voter(self):
    #     number= Voter.count()
    #     return self.number

    def __str__(self):
        return self.first_name


class Event(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.title
