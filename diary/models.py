from django.db import models
from django.contrib.auth.models import User
from home.models import Movie

# Create your models here.
class Detail(models.Model):
    this_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="details")
    first_name = models.CharField(max_length=200, default="FirstName")
    last_name = models.CharField(max_length=200, default="LastName")
    updated_on = models.DateTimeField(auto_now=True)

class Booking(models.Model):
    which_movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="bookings")
    which_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booker")
    which_day = models.CharField(max_length=200, unique=True, default="1st Jan 2025")
    created_on = models.DateTimeField(auto_now=True)