from allauth.socialaccount.signals import pre_social_login
from django.contrib.auth import get_user_model

User = get_user_model()

def pre_social_login_receiver(request, sociallogin):
    print('ini request', request)
    print(sociallogin)

pre_social_login.connect(pre_social_login_receiver, sender=User)