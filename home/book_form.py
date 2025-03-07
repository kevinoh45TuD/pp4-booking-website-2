from diary.models import Booking
from .models import Movie
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django import forms

class UserBooking(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('which_day',)