from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('profile/', views.UserProfileView.as_view(), name='users'),
    path('registration/', views.UserRegistrationView.as_view(), name='user-registration'),
    # path('login/', views.LoginView, name='login'),
    path('verifi-otp/', views.VerifyOtpView, name='verifi-otp'),
    path('reset-password/', views.ResetPasswordView, name='reset-password'),
    path('forgot-password/', views.ForgotPasswordView, name='forgot-password'),
    path('user-profile/', views.UserProfileView.as_view(), name='user-profile'),
 
# ================================== JWT token =======================================

    path('login/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
