from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.BookingView, name='booking'),
    path('my-bookings/', views.getBookingsView, name='my-bookings'),
]
