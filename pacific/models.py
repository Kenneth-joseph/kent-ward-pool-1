from django.db import models

# Create your models here.

class Voter(models.Model):
    first_name = models.CharField(max_length = 30)
    second_name = models.CharField(max_length = 30)
    national_id = models.IntegerField(default=0)
    phone_number = models.IntegerField(default=0)
    ward = models.CharField(max_length= 30)


    def __str__(self):
        return self.national_id

class Event(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)