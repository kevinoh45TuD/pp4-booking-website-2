from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Movie(models.Model):
    movie_title = models.CharField(max_length=200, unique=True)
    listing_author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="movie_title"
    )
    movie_desc = models.TextField()
    meal_name = models.CharField(max_length=200, unique=True)
    listed_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
