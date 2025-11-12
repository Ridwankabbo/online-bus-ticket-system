from django.urls import path
from . import views
urlpatterns = [
    path('users/', views.UsersView.as_view(), name='users'),
    path('user-registration/', views.UserRegistrationView.as_view(), name='user-registration')
    
]
