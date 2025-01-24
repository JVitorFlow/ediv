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
    list_display = ('email', 'name', 'is_active', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')


    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Informações Pessoais", {"fields": ("name",)}),
        ("Permissões", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Datas Importantes", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "name", "password1", "password2", "is_active", "is_staff"),
        }),
    )

    search_fields = ("email", "name")
    ordering = ("email",)
