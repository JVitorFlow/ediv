from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import UserManager as BaseUserManager

class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Super usuário deve ter is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Super usuário deve ter is_superuser=True")
        
        return self._create_user(email, password, **extra_fields)
    
class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"  # Define o email como campo principal para login
    REQUIRED_FIELDS = ['username']  # Campos obrigatórios além do USERNAME_FIELD
    objects = UserManager()

    def __str__(self):
        return self.email