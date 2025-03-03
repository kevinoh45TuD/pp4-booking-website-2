from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MovieList.as_view(), name='home'),
    path('<slug:slug>/', views.movie_detail, name="movie_detail"),
]