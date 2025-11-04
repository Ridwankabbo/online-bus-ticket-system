from django.urls import path
from . import views


urlpatterns = [
    path('all-bus/', views.BusView, name='bus-api'),
    path('search/', views.SearchBusView, name='search-view'),
    path('shidules/', views.ShiduleView, name='shidules'),
    path('locations/', views.LocationView, name='locations'),
    path('routes/', views.RouteView, name="routes"),
    path('bus/search/seats/', views.SeatsView, name="seats-view")
]
