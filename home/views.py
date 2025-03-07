from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Movie
from .book_form import UserBooking
from diary.models import Booking
from django.contrib.auth.models import User


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
    image_index = "/static/images/"+ movie.movie_image +".jpg"

    if request.method == "POST":
        user_booking = UserBooking(data=request.POST)
        if user_booking.is_valid():
            booking = user_booking.save(commit=False)
            booking.which_user = request.user
            booking.which_movie = movie
            booking.save()
            messages.add_message(
                request, messages.SUCCESS,
                'You have successfully made a booking!'
            )
    else:
        user_booking = UserBooking()
    return render(
        request,
        "home/movie_detail.html",
        {
            "movie": movie,
            "image_index": image_index,
            "user_booking": user_booking,
        },
    )

def booking_edit(request, slug, booking_id):
    """
    view to edit booking
    """

    if request.method == "POST":

        queryset = Movie.objects.all()
        movie = get_object_or_404(queryset, slug=slug)
        booking = get_object_or_404(Booking, pk=booking_id)
        user_booking = UserBooking(data=request.POST, instance=booking)

        if user_booking.is_valid() and booking.which_user == request.user:
            booking = user_booking.save(commit=False)
            booking.which_movie = movie
            booking.save()
            messages.add_message(request, messages.SUCCESS, 'Booking Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating booking!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))