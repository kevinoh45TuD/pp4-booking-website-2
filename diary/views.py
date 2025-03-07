from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Detail
from .models import Booking

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