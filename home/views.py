from django.shortcuts import render
from django.views import generic
from .models import Movie


# Create your views here.

class MovieList(generic.ListView):
    queryset = Movie.objects.all()
    template_name = "home/index.html"
    #paginate_by = 6

#def index(request):
    #""" A view to return the index page """
    


    #return render(request, 'home/index.html')
