from django.urls import path
from . import views
urlpatterns = [
    path('', views.UsersView.as_view(), name='users'),
    path('registration/', views.UserRegistrationView.as_view(), name='user-registration')
    
]
