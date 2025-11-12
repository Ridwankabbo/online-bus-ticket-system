import random
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings


def generate_otp():
    return str(random.randint(100000 - 999999))

def send_verification_mail(user, code):
    main_subject = "Your account verification otp code "
    message = f"Hi, {user.username} your verification code is {code}"
    
    mail = send_mail(
        main_subject,
        message,
        settings.EMAIL_USER_HOST,
        [user.email],
        fail_silently=False
    )
    
    return mail