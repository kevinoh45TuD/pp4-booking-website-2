from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Free-Space"), (1, "Fully-Booked"))

# Create your models here.
class Movie(models.Model):
    movie_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, default="tempSlug")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="movie_title"
    )
    movie_desc = models.TextField()
    movie_image = models.TextField(max_length=200, unique=True, default="tempImg")
    movie_image_desc = models.TextField(max_length=200, unique=True, default="tempImgDesc")
    meal_name = models.CharField(max_length=200, unique=True)
    listed_on = models.DateTimeField(auto_now_add=True)
    available = models.IntegerField(choices=STATUS, default=0)
