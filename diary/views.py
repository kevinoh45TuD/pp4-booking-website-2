from django.shortcuts import render, get_object_or_404,reverse
from django.contrib.auth.models import User
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Detail
from .models import Booking
from home.book_form import UserBooking
from home.models import Movie

# Create your views here.
def my_details(request):
    """
    Renders the users details
    """

    user = get_object_or_404(User, id=request.user.id)
    bookings = user.booker.all().order_by('-created_on')
    detail = user.details.first()
    
    if detail:
        fname = detail.first_name
        lname = detail.last_name
    else:
        fname = "FirstName"
        lname = "LastName"

    return render(
        request,
        "diary/diary.html",
        {
            "user": user,
            "bookings": bookings,
            "fname": fname,
            "lname": lname,
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