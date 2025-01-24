from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()

class CustomBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):

        email = username or kwargs.get('email')
        if not email or not password:
            return None

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        
        # Verifica a senha e se o usuário está ativo
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None