from django.shortcuts import render
from django.views import generic
from .models import Movie


# Create your views here.

class MovieList(generic.ListView):
    model = Movie

#def index(request):
    #""" A view to return the index page """
    


    #return render(request, 'home/index.html')
