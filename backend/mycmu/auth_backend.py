from .models import User 
from django.conf import settings
from django.contrib.auth.backends import BaseBackend


# requires to define two functions authenticate and get_user

class AuthWithEmail(BaseBackend):  
    def authenticate(self, request, email=None):
        try:
            user = User.objects.get(email=email)
            return user
        except User.DoesNotExist:
            return None
        
    def get_user(self, user_id):
        try:
            user = User.objects.filter(id=user_id)
            return user
        except User.DoesNotExist:
            return None
    
