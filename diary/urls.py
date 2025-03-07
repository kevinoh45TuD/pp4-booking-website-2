from . import views
from django.urls import path

urlpatterns = [
    path('', views.my_details, name='diary'),
    path('<slug:slug>/edit_booking/<int:booking_id>', views.booking_edit, name='booking_edit'),
]