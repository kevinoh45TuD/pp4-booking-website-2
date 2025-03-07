from django.db import models
from django.contrib.auth.models import User
from home.models import Movie

DAY = ((0, "Monday"), (1, "Tuesday"), (2, "Wednesday"), (3, "Thursday"), (4, "Friday"))

# Create your models here.
class Detail(models.Model):
    this_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="details")
    first_name = models.CharField(max_length=200, default="FirstName")
    last_name = models.CharField(max_length=200, default="LastName")
    updated_on = models.DateTimeField(auto_now=True)

class Booking(models.Model):
    which_movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="bookings")
    which_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booker")
    which_day = models.IntegerField(max_length=200, choices=DAY, default=0)
    created_on = models.DateTimeField(auto_now=True)