from django.urls import path
from . import views

urlpatterns = [
    path('bus_list/', views.getBusList)
]
