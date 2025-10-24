from django.urls import path
from . import views
urlpatterns = [
    path('all-users/', views.UsersView.as_view(), name='users'),
    path('register-user/', views.UserRegistrationView.as_view(), name='register-user'),
    path('verify-otp/', views.VerifyOtpView.as_view(), name="verify-otp"),
    path('resend-otp/', views.ResendOtpView.as_view(), name="resend-otp"),
    path('login-user/', views.UserLoginView.as_view(), name='user-login'),
    path('forgot-password/', views.ForgotPasswordView.as_view(), name="forgot-password"),
    path('reset-password/', views.ResetPasswordView.as_view(), name="reset-password")
]
