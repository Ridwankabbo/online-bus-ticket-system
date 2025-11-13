import random
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type

class TokenGenerator(PasswordResetTokenGenerator):
    
    def _make_hash_value(self, user, timestamp):
        return (
            text_type(user.pk)+text_type(timestamp)+text_type(user.is_active)
        )

account_activation_token = TokenGenerator()

def generate_otp():
    return str(random.randint(100000, 999999))

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