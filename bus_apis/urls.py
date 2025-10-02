from django.urls import path
from . import views

urlpatterns = [
    path('bus_list/', views.BusSearchAPIView.as_view(), name="bus-list")
]
