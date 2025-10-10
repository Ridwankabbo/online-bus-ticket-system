from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register(r"bus_list", views.BusSearchAPIView)

urlpatterns = [
    path('bus_list/', views.BusSearchAPIView.as_view(), name="bus-list")
    # path("", include(router.urls))
]
