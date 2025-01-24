from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()

class CustomBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):

        if username is None or password is None:
            return None  # Retorna None caso username ou password não sejam fornecidos

        try:
            user = User.objects.get(email=username)  # Autentica pelo email
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