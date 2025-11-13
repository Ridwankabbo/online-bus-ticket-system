from django.urls import path
from . import views
urlpatterns = [
    path('locations/', views.LocationView, name='locations'),
    path('bus-seats/', views.BusSeatsView, name='bus-seats'),
    path('shidules/', views.BusShiduleView, name='shidules')
    
]
