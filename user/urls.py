from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
)
urlpatterns = [
    path('', views.UsersView.as_view(), name='users'),
    path('registration/', views.UserRegistrationView.as_view(), name='user-registration'),
    path('login/', views.LoginView, name='login'),
    path('verifi-otp/', views.VerifyOtpView, name='verifi-otp'),
    path('reset-password/', views.ResetPasswordView, name='reset-password'),
    path('forgot-password/', views.ForgotPasswordView, name='forgot-password'),
 
# ================================== JWT token =======================================
    path('api/token/', TokenObtainSlidingView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshSlidingView.as_view(), name='token_refresh'),
    
]
