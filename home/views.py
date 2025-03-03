from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Movie


# Create your views here.

class MovieList(generic.ListView):
    queryset = Movie.objects.all()
    template_name = "home/index.html"
    #paginate_by = 6

def movie_detail(request, slug):
    """
    Display and individual :model:`home.Movie`.

    **Context**

    ``movie``
        An instance of :model:`home.Movie`.

    **Template**

    :template:`blog/movie_detail.html`
    """

    queryset = Movie.objects.all()
    movie = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "home/movie_detail.html",
        {"movie": movie},
    )
