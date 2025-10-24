from django.urls import path
from . import views
urlpatterns = [
    path('all-users/', views.UsersView.as_view(), name='users'),
    path('register-user/', views.UserRegistrationView.as_view(), name='register-user')
]
