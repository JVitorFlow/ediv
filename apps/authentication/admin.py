from django.contrib import admin
from .models import Users
from django.contrib.auth import admin as admin_auth_django
from .forms import UserChangeForm, UserCreationForm

@admin.register(Users)
class UserAdmin(admin_auth_django.UserAdmin):
    form = UserChangeForm
    add_form =  UserCreationForm
    model = Users

    # Campos exibidos na listagem de usuários no Django Admin
    list_display = ("email", "username", "is_staff", "is_active")
    list_filter = ("is_staff", "is_superuser", "is_active")


    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Informações Pessoais", {"fields": ("username",)}),
        ("Permissões", {"fields": ("is_staff", "is_superuser", "is_active", "groups", "user_permissions")}),
        ("Datas Importantes", {"fields": ("last_login",)}),
    )

    # Campos exibidos no formulário de criação do usuário
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "password1", "password2", "is_staff", "is_superuser", "is_active"),
        }),
    )

    search_fields = ("email", "username")
    ordering = ("email",)
