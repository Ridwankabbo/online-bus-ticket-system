from django.urls import path
from . import views
urlpatterns = [
    path('all-bus/', views.BusView, name='bus-api'),
    path('shidules/', views.ShiduleView, name='shidules'),
    path('locations/', views.LocationView, name='locations'),
    path('routes/', views.RouteView, name="routes")
]
